"""
文件处理模块
作用：处理各种格式的输入输出文件，提供统一的数据接口
"""
import csv
import pandas as pd
import os
from typing import List, Dict, Any
from .utils import setup_logger


class FileProcessor:
    """文件处理器 - 数据输入输出的桥梁"""

    def __init__(self):
        self.logger = setup_logger()

    def read_text_file(self, file_path: str) -> List[str]:
        """
        读取文本文件 - 处理.txt格式
        作用：从文本文件中读取内容，自动过滤空行和空白字符
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = [line.strip() for line in file if line.strip()]
            self.logger.info(f"从 {file_path} 读取了 {len(lines)} 行文本")
            return lines
        except Exception as e:
            self.logger.error(f"读取文件失败: {e}")
            return []

    def read_csv_file(self, file_path: str, text_column: str = "text") -> List[str]:
        """
        读取CSV文件 - 处理.csv格式
        作用：从CSV文件中提取指定列的文本数据，支持自动编码检测
        """
        try:
            df = pd.read_csv(file_path)
            if text_column not in df.columns:
                raise ValueError(f"CSV文件中找不到列: {text_column}")

            texts = df[text_column].dropna().astype(str).tolist()
            self.logger.info(f"从 {file_path} 读取了 {len(texts)} 条文本")
            return texts
        except Exception as e:
            self.logger.error(f"读取CSV文件失败: {e}")
            return []

    def save_results(self, results: List[Dict[str, Any]], output_path: str):
        """
        保存分析结果 - 支持多种输出格式
        作用：将分析结果保存为CSV或JSON格式，便于后续分析
        """
        try:
            # 转换为DataFrame便于保存
            df = pd.DataFrame(results)

            if output_path.endswith('.csv'):
                df.to_csv(output_path, index=False, encoding='utf-8-sig')
            elif output_path.endswith('.json'):
                df.to_json(output_path, orient='records', force_ascii=False, indent=2)
            else:
                # 默认保存为CSV
                df.to_csv(output_path, index=False, encoding='utf-8-sig')

            self.logger.info(f"结果已保存到: {output_path}")
        except Exception as e:
            self.logger.error(f"保存结果失败: {e}")

    def get_file_type(self, file_path: str) -> str:
        """获取文件类型 - 自动识别输入文件格式"""
        if file_path.endswith('.txt'):
            return 'text'
        elif file_path.endswith('.csv'):
            return 'csv'
        else:
            raise ValueError("不支持的文件格式，请使用 .txt 或 .csv 文件")