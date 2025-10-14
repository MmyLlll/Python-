"""
情感分析核心模块
作用：封装所有情感分析相关逻辑，包括API调用、批量处理、错误处理等
"""
import os
import requests
import json
from typing import Dict, List, Any
from configparser import ConfigParser

from .utils import clean_text, parse_json_response, validate_text_length, setup_logger
from config.prompt_templates import get_prompt


class SentimentAnalyzer:
    """情感分析器 - 项目的核心大脑"""

    def __init__(self, config_path: str = "config/config.ini"):
        self.logger = setup_logger()
        self.config = self._load_config(config_path)
        self.api_key = os.getenv("DEEPSEEK_API_KEY")

        if not self.api_key:
            raise ValueError("请设置 DEEPSEEK_API_KEY 环境变量")

    def _load_config(self, config_path: str) -> ConfigParser:
        """加载配置文件 - 初始化时读取所有配置参数"""
        config = ConfigParser()
        config.read(config_path, encoding='utf-8')
        return config

    def analyze_single_text(self, text: str, language: str = "zh") -> Dict[str, Any]:
        """
        分析单个文本的情感 - 核心分析方法
        作用：处理单条文本的完整分析流程（清洗→调用API→解析结果）
        """
        try:
            # 文本预处理
            cleaned_text = clean_text(text)

            if not validate_text_length(cleaned_text):
                self.logger.warning("文本过长，已自动截断")
                cleaned_text = cleaned_text[:2000]

            # 构建API请求
            prompt = get_prompt(cleaned_text, language)

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": self.config.get("api", "model"),
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.1  # 低温度保证输出稳定性
            }

            # 发送请求
            response = requests.post(
                f"{self.config.get('api', 'base_url')}/chat/completions",
                headers=headers,
                json=data,
                timeout=self.config.getint("api", "timeout")
            )
            response.raise_for_status()

            # 解析响应
            result = response.json()
            content = result["choices"][0]["message"]["content"]

            # 解析JSON结果
            sentiment_result = parse_json_response(content)
            sentiment_result["original_text"] = text[:100] + "..." if len(text) > 100 else text

            self.logger.info(f"情感分析完成: {sentiment_result['sentiment']}")
            return sentiment_result

        except requests.exceptions.RequestException as e:
            self.logger.error(f"API请求失败: {e}")
            return {
                "sentiment": "错误",
                "confidence": 0.0,
                "reason": f"API请求失败: {str(e)}",
                "original_text": text
            }
        except Exception as e:
            self.logger.error(f"分析过程出错: {e}")
            return {
                "sentiment": "错误",
                "confidence": 0.0,
                "reason": f"分析错误: {str(e)}",
                "original_text": text
            }

    def analyze_batch(self, texts: List[str], language: str = "zh") -> List[Dict[str, Any]]:
        """
        批量分析文本情感 - 处理大量数据
        作用：高效处理文本列表，支持分批处理避免API限制
        """
        results = []
        batch_size = self.config.getint("analysis", "default_batch_size")

        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            self.logger.info(f"处理批次 {i // batch_size + 1}/{(len(texts) - 1) // batch_size + 1}")

            for text in batch:
                result = self.analyze_single_text(text, language)
                results.append(result)

        return results