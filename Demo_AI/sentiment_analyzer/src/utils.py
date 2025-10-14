"""
工具函数模块
作用：提供文本处理、JSON解析、日志配置等通用功能，避免代码重复
"""
import re
import json
import logging
from typing import Dict, Any

def setup_logger():
    """设置日志配置 - 用于调试和运行状态监控"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """
    文本清洗函数 - 预处理输入文本，提高分析准确性
    作用：移除特殊字符、多余空格，保留中英文和基本标点
    """
    # 移除多余空白字符
    text = re.sub(r'\s+', ' ', text)
    # 移除特殊字符但保留中文、英文、数字和基本标点
    text = re.sub(r'[^\w\s\u4e00-\u9fff，。！？；：""''（）《》]', '', text)
    return text.strip()

def parse_json_response(response_text: str) -> Dict[str, Any]:
    """
    解析API返回的JSON响应 - 处理AI返回的各种格式
    作用：从AI响应中提取结构化数据，处理格式不一致的情况
    """
    try:
        # 尝试提取JSON部分（处理可能包含其他文本的情况）
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            return {
                "sentiment": "中性",
                "confidence": 0.5,
                "reason": "无法解析响应"
            }
    except json.JSONDecodeError:
        return {
            "sentiment": "中性",
            "confidence": 0.5,
            "reason": "JSON解析错误"
        }

def validate_text_length(text: str, max_length: int = 2000) -> bool:
    """验证文本长度 - 防止API调用失败"""
    return len(text) <= max_length