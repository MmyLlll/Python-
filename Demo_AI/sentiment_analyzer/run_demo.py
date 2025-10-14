#!/usr/bin/env python3
"""
直接运行演示文件 - 双击或在PyCharm中直接运行
"""
import os
import sys

# 添加项目路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import main


def run_demo():
    """运行演示程序"""
    print("🚀 启动情感分析演示...")

    # 设置演示参数
    sys.argv = [
        'main.py',
        '--text', '这个AI工具真是太神奇了，完全改变了我的工作方式！',
        '--output', 'data/output/demo_result.csv'
    ]

    # 执行主程序
    main()


if __name__ == "__main__":
    run_demo()