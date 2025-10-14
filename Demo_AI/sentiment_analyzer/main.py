#!/usr/bin/env python3
"""
情感分析工具主程序
作用：程序入口点，协调各个模块协同工作，处理用户交互
"""
import argparse
import os
import sys
from datetime import datetime

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.analyzer import SentimentAnalyzer
from src.file_processor import FileProcessor
from src.visualizer import ResultVisualizer


def main():
    parser = argparse.ArgumentParser(description="情感分析工具")
    parser.add_argument("--text", "-t", type=str, help="直接分析单个文本")
    parser.add_argument("--file", "-f", type=str, help="分析文件路径 (.txt 或 .csv)")
    parser.add_argument("--csv-column", "-c", type=str, default="text",
                        help="CSV文件中的文本列名 (默认: text)")
    parser.add_argument("--language", "-l", type=str, default="zh",
                        choices=["zh", "en"], help="文本语言 (默认: 中文)")
    parser.add_argument("--output", "-o", type=str, help="结果输出路径")
    parser.add_argument("--no-chart", action="store_true", help="不生成图表")

    args = parser.parse_args()

    if not args.text and not args.file:
        parser.error("必须提供 --text 或 --file 参数")

    try:
        # 初始化组件
        analyzer = SentimentAnalyzer()
        processor = FileProcessor()
        visualizer = ResultVisualizer()

        texts = []

        # 处理输入
        if args.text:
            texts = [args.text]
            print(f"分析单个文本: {args.text[:50]}...")
        elif args.file:
            file_type = processor.get_file_type(args.file)
            if file_type == 'text':
                texts = processor.read_text_file(args.file)
            else:  # csv
                texts = processor.read_csv_file(args.file, args.csv_column)

            if not texts:
                print("错误: 无法从文件中读取文本")
                return

        # 执行分析
        print(f"开始分析 {len(texts)} 条文本...")
        results = analyzer.analyze_batch(texts, args.language)

        # 显示结果
        print("\n" + "=" * 50)
        print("情感分析结果汇总")
        print("=" * 50)

        # 显示汇总表格
        summary_table = visualizer.generate_summary_table(results)
        print(summary_table)

        # 显示详细结果
        print(f"\n详细结果 (前{min(10, len(results))}条):")
        visualizer.print_detailed_results(results)

        # 生成图表
        if not args.no_chart and len(results) > 1:
            chart_path = None
            if args.output:
                chart_name = f"sentiment_chart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                chart_path = os.path.join(os.path.dirname(args.output), chart_name)

            visualizer.plot_sentiment_distribution(results, chart_path)

        # 保存结果
        if args.output:
            processor.save_results(results, args.output)
            print(f"\n完整结果已保存到: {args.output}")

        print(f"\n分析完成! 共处理 {len(results)} 条文本")

    except Exception as e:
        print(f"程序执行出错: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()