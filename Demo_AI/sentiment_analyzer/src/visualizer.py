"""
结果可视化模块
作用：将分析结果以图表和表格形式直观展示，提供数据洞察
"""
import matplotlib.pyplot as plt
from tabulate import tabulate
from collections import Counter
from typing import List, Dict, Any
from .utils import setup_logger
import platform  # ← 新增导入
import os        # ← 新增导入


class ResultVisualizer:
    """结果可视化器 - 数据展示专家"""

    def __init__(self, style: str = 'ggplot'):
        self.logger = setup_logger()
        plt.style.use(style)
        self._setup_chinese_font()  # ← 新增这行

    def _setup_chinese_font(self):  # ← 新增这个函数
        """设置中文字体支持"""
        try:
            if platform.system() == 'Windows':
                plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
            elif platform.system() == 'Darwin':
                plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Heiti SC', 'DejaVu Sans']
            else:
                plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'DejaVu Sans']
            plt.rcParams['axes.unicode_minus'] = False
        except Exception as e:
            self.logger.warning(f"字体设置失败: {e}")

    def generate_summary_table(self, results: List[Dict[str, Any]]) -> str:
        """生成汇总表格"""
        # 统计情感分布
        sentiment_counts = Counter([r['sentiment'] for r in results])
        total = len(results)

        table_data = []
        for sentiment, count in sentiment_counts.items():
            percentage = (count / total) * 100
            table_data.append([sentiment, count, f"{percentage:.1f}%"])

        # 按数量排序
        table_data.sort(key=lambda x: x[1], reverse=True)

        headers = ["情感类别", "数量", "百分比"]
        return tabulate(table_data, headers=headers, tablefmt="grid")

    def plot_sentiment_distribution(self, results: List[Dict[str, Any]], save_path: str = None):
        """绘制情感分布饼图"""
        sentiment_counts = Counter([r['sentiment'] for r in results])

        # 准备数据
        labels = list(sentiment_counts.keys())
        sizes = list(sentiment_counts.values())

        # 创建饼图
        fig, ax = plt.subplots(figsize=(10, 8))
        wedges, texts, autotexts = ax.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90,
            colors=plt.cm.Set3.colors
        )

        # 美化文本
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        ax.set_title('情感分析结果分布', fontsize=16, fontweight='bold')
        plt.tight_layout()

        if save_path:
            try:
                # 确保目录存在 ← 修改这里
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                self.logger.info(f"图表已保存到: {save_path}")
            except Exception as e:
                self.logger.error(f"保存图表失败: {e}")

        plt.show()

    def print_detailed_results(self, results: List[Dict[str, Any]], limit: int = 10):
        """打印详细结果"""
        table_data = []
        for i, result in enumerate(results[:limit]):
            table_data.append([
                i + 1,
                result['original_text'][:50] + '...' if len(result['original_text']) > 50 else result['original_text'],
                result['sentiment'],
                f"{result.get('confidence', 0):.2f}",
                result.get('reason', '')[:30] + '...' if len(result.get('reason', '')) > 30 else result.get('reason', '')
            ])

        headers = ["序号", "文本预览", "情感", "置信度", "分析理由"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        if len(results) > limit:
            print(f"\n... 还有 {len(results) - limit} 条结果未显示")