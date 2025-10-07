import os
from dotenv import load_dotenv


class Config:
    """
    配置管理类 - 适配DeepSeek API
    """

    def __init__(self):
        # 加载.env文件
        load_dotenv()

        # 获取DeepSeek API密钥
        self.api_key = os.getenv('DEEPSEEK_API_KEY')
        self.history_file = 'conversation_history.json'
        self.model = 'deepseek-chat'  # DeepSeek模型名称
        self.api_base = 'https://api.deepseek.com/v1'  # DeepSeek API地址

        # 验证配置
        self._validate_config()

    def _validate_config(self):
        """验证配置是否完整"""
        if not self.api_key:
            raise ValueError("❌ 错误：请在.env文件中配置DEEPSEEK_API_KEY")

        print("✅ DeepSeek配置验证通过")