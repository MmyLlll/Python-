# 💖 项目三：情感分析工具

## 📋 项目概述
一个专业的文本情感分析系统，能够自动识别文本的情感倾向，支持批量处理和可视化分析。

## 🎯 核心功能
- **情感分类**: 识别积极、消极、中性等情感
- **多语言支持**: 中英文情感分析
- **批量处理**: 支持TXT、CSV文件批量分析
- **数据可视化**: 情感分布图表和统计报表
- **结果导出**: CSV、JSON格式数据导出

## 🛠️ 技术栈
- **后端框架**: FastAPI + Python
- **AI服务**: DeepSeek API
- **数据处理**: pandas, numpy
- **可视化**: matplotlib, seaborn
- **文本处理**: jieba, sklearn

## 📁 项目结构
sentiment_analyzer/
├── config/
│ ├── config.ini
│ └── prompt_templates.py
├── src/
│ ├── analyzer.py
│ ├── file_processor.py
│ ├── visualizer.py
│ └── utils.py
├── data/
│ ├── input/
│ └── output/
├── tests/
├── requirements.txt
└── main.py


## 💻 使用方法
# 单文本分析
python main.py --text "这个产品很棒！" --language zh

# 文件批量分析
python main.py --file data/input/reviews.csv --output results.csv

# 英文文本分析
python main.py --text "This is amazing!" --language en

# 禁用图表生成
python main.py --file data.txt --no-chart

情感分析结果汇总
+------------+------+--------+
| 情感类别   | 数量 | 百分比  |
+============+======+========+
| 积极       | 8    | 40.0%  |
| 消极       | 6    | 30.0%  |
| 中性       | 6    | 30.0%  |
+------------+------+--------+

## 🎓 学习价值
✅ 自然语言处理实战

✅ 数据可视化技术

✅ 批量文件处理

✅ 生产级项目架构设计

✅ 完整的错误处理机制