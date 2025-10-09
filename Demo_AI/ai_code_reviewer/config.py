import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

class Config:
    load_dotenv()

    API_KEY = os.getenv('DEEPSEEK_API_KEY')
    API_BASE = os.getenv('API_BASE', 'https://api.deepseek.com/v1')
    DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'deepseek-chat')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', '2000'))
    REPORT_OUTPUT_DIR = os.getenv('REPORT_OUTPUT_DIR', 'review_reports')

    REVIEW_MODES = {
        "basic": "基础代码审查",
        "advanced": "高级代码优化",
        "security": "安全漏洞扫描",
        "performance": "性能分析"
    }

    @classmethod
    def validate_config(cls):
        if not cls.API_KEY:
            raise ValueError("❌ 请在.env文件中配置DEEPSEEK_API_KEY")
        Path(cls.REPORT_OUTPUT_DIR).mkdir(exist_ok=True)
        return True
        # """增强的配置验证"""
        # if not cls.API_KEY:
        #     raise ValueError("❌ 请在.env文件中配置DEEPSEEK_API_KEY")
        #
        # # 可选：测试API连通性
        # try:
        #     test_client = OpenAI(api_key=cls.API_KEY, base_url=cls.API_BASE)
        #     response = test_client.chat.completions.create(
        #         model=cls.DEFAULT_MODEL,
        #         messages=[{"role": "user", "content": "Hi"}],
        #         max_tokens=5
        #     )
        #     print("✅ API连通性测试通过")
        # except Exception as e:
        #     print(f"⚠️  API密钥有效但连通性有问题: {e}")
        #
        # print("✅ 配置验证通过")

    @classmethod
    def get_review_prompt(cls, mode="basic"):
        prompts = {
            "basic": """你是一个资深Python代码审查专家。请对以下代码进行详细审查：

要求：
1. 代码质量分析（可读性、规范性）
2. 潜在问题识别（bug、逻辑错误）
3. 改进建议（代码优化、最佳实践）
4. 按严重程度分类：严重、警告、建议

请用中文回复，结构清晰。""",
            "advanced": """你是一个高级Python架构师。请进行深度代码审查：

审查维度：
1. 架构设计合理性
2. 算法效率分析
3. 代码可维护性
4. 扩展性评估
5. 详细的重构方案

请提供具体的优化代码示例。""",
            "security": """你是安全代码审查专家。专注于安全漏洞检测：

安全检查项：
1. 注入漏洞（SQL、命令注入）
2. 敏感信息泄露
3. 输入验证缺失
4. 权限控制问题
5. 常见Web安全漏洞

标记风险等级：高危、中危、低危。""",
            "performance": """你是性能优化专家。分析代码性能问题：

性能审查：
1. 时间复杂度分析
2. 内存使用优化
3. I/O操作优化
4. 并发性能问题
5. 缓存策略评估

提供具体的性能优化建议。"""
        }
        return prompts.get(mode, prompts["basic"])