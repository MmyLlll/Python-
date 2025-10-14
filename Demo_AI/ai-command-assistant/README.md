# 🚀 项目一：智能命令行助手

## 📋 项目概述
一个基于AI的智能命令行工具，能够理解自然语言命令并执行相应的系统操作或提供智能回答。

## 🎯 核心功能
- **自然语言理解**: 解析用户的自然语言命令
- **系统命令执行**: 执行文件操作、系统查询等
- **智能问答**: 基于AI的知识库回答问题
- **对话记忆**: 支持多轮对话上下文

## 🛠️ 技术栈
- **编程语言**: Python 3.9+
- **AI服务**: DeepSeek API
- **命令行框架**: argparse
- **配置管理**: configparser + python-dotenv
- **文件操作**: os, subprocess 模块

## 📁 项目结构
smart_cli/
├── config/
│ ├── config.ini
│ └── command_mappings.py
├── src/
│ ├── cli_engine.py
│ ├── command_parser.py
│ └── api_client.py
├── requirements.txt
└── main.py

## 💻 使用方法
# 安装依赖
pip install -r requirements.txt

# 设置API密钥
export DEEPSEEK_API_KEY="your_api_key"

# 运行程序
python main.py "帮我列出当前目录的文件"
python main.py "今天的天气怎么样？"

## 🎓 学习价值
✅ Python命令行应用开发

✅ API集成与调用

✅ 自然语言处理基础

✅ 配置管理和错误处理

✅ 面向对象编程实践