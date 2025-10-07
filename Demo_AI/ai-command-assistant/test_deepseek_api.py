# test_deepseek_api.py - DeepSeek API连通性测试
import os
import httpx
from dotenv import load_dotenv


def test_deepseek_api():
    """测试DeepSeek API是否正常工作"""

    # 加载环境变量
    load_dotenv()

    # 获取API密钥
    api_key = os.getenv('DEEPSEEK_API_KEY')

    if not api_key:
        print("❌ 错误：未找到DEEPSEEK_API_KEY，请检查.env文件")
        return False

    print("🔍 检测到DeepSeek API密钥，开始测试连接...")

    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": "请回复'DeepSeek API测试成功'"}],
            "max_tokens": 20,
            "temperature": 0.7
        }

        # 调用DeepSeek API
        with httpx.Client() as client:
            response = client.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30.0
            )

            if response.status_code == 200:
                result = response.json()
                ai_response = result["choices"][0]["message"]["content"]
                print(f"✅ DeepSeek API测试成功！AI回复: {ai_response}")
                return True
            else:
                print(f"❌ DeepSeek API测试失败: {response.status_code} - {response.text}")
                return False

    except Exception as e:
        print(f"❌ DeepSeek API测试失败: {e}")
        return False


if __name__ == "__main__":
    test_deepseek_api()