import json
import os
import httpx
from config import Config


class ChatAssistant:
    """
    智能命令行助手主类 - DeepSeek API版本
    """

    def __init__(self):
        # 初始化配置
        self.config = Config()

        # 初始化对话历史
        self.conversation_history = []
        self._load_history()

        # 系统提示词
        self.system_prompt = "你是一个智能命令行助手，回答要简洁专业，适合在命令行中显示。"

    def _load_history(self):
        """从文件加载对话历史"""
        try:
            if os.path.exists(self.config.history_file):
                with open(self.config.history_file, 'r', encoding='utf-8') as f:
                    self.conversation_history = json.load(f)
                print(f"✅ 已加载 {len(self.conversation_history)} 条历史记录")
            else:
                print("ℹ️  无历史记录，开始新对话")
        except Exception as e:
            print(f"❌ 加载历史记录失败: {e}")
            self.conversation_history = []

    def _save_history(self):
        """保存对话历史到文件"""
        try:
            with open(self.config.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"❌ 保存历史记录失败: {e}")

    def _get_ai_response(self, user_input):
        """使用DeepSeek API获取AI回复"""
        try:
            # 构建消息列表
            messages = [{"role": "system", "content": self.system_prompt}]

            # 添加历史对话（最近5轮）
            for history in self.conversation_history[-5:]:
                messages.extend([
                    {"role": "user", "content": history["question"]},
                    {"role": "assistant", "content": history["answer"]}
                ])

            # 添加当前问题
            messages.append({"role": "user", "content": user_input})

            # 调用DeepSeek API
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config.api_key}"
            }

            data = {
                "model": self.config.model,
                "messages": messages,
                "max_tokens": 1000,
                "temperature": 0.7,
                "stream": False
            }

            # 使用httpx调用DeepSeek API
            with httpx.Client() as client:
                response = client.post(
                    f"{self.config.api_base}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=30.0
                )

                if response.status_code == 200:
                    result = response.json()
                    return result["choices"][0]["message"]["content"]
                else:
                    error_msg = f"❌ API请求失败: {response.status_code}"
                    if response.status_code == 402:
                        error_msg += " - 账户余额不足，请充值"
                    elif response.status_code == 401:
                        error_msg += " - API密钥无效"
                    elif response.status_code == 429:
                        error_msg += " - 请求频率超限"
                    return error_msg

        except httpx.TimeoutException:
            return "❌ 请求超时，请检查网络连接"
        except Exception as e:
            return f"❌ 获取AI回复时出错: {str(e)}"

    def _show_help(self):
        """显示帮助信息"""
        help_text = """
🤖 智能命令行助手 - DeepSeek版本

基础命令:
  help     - 显示此帮助信息
  history  - 显示对话历史
  clear    - 清空对话历史
  quit     - 退出程序

对话功能:
  直接输入任何问题，助手会智能回复
  对话历史会自动保存到文件
  使用DeepSeek AI引擎，支持上下文记忆

示例:
  您: 你好
  您: Python是什么？
  您: 帮我写一个排序算法
  您: history
  您: clear
  您: quit
        """
        print(help_text)

    def _show_history(self):
        """显示对话历史"""
        if not self.conversation_history:
            print("📝 暂无对话历史")
            return

        print(f"\n📝 对话历史 (共{len(self.conversation_history)}条):")
        print("=" * 60)
        for i, conversation in enumerate(self.conversation_history, 1):
            print(f"{i}. 您: {conversation['question']}")
            print(f"   AI: {conversation['answer']}")
            print("-" * 60)

    def _clear_history(self):
        """清空对话历史"""
        self.conversation_history = []
        self._save_history()
        print("✅ 对话历史已清空")

    def run(self):
        """运行主程序"""
        print("🚀 智能命令行助手已启动！(DeepSeek版本)")
        print("💡 输入 'help' 查看帮助，输入 'quit' 退出程序")

        while True:
            try:
                # 获取用户输入
                user_input = input("\n您: ").strip()

                # 处理空输入
                if not user_input:
                    continue

                # 处理命令
                if user_input.lower() == 'quit':
                    print("👋 再见！")
                    break
                elif user_input.lower() == 'help':
                    self._show_help()
                    continue
                elif user_input.lower() == 'history':
                    self._show_history()
                    continue
                elif user_input.lower() == 'clear':
                    self._clear_history()
                    continue

                # 处理普通对话
                print("AI: 思考中...", end='\r')

                # 获取AI回复
                ai_response = self._get_ai_response(user_input)

                # 显示回复
                print(f"AI: {ai_response}")

                # 保存到历史
                self.conversation_history.append({
                    "question": user_input,
                    "answer": ai_response
                })
                self._save_history()

            except KeyboardInterrupt:
                print("\n\n👋 程序被用户中断，再见！")
                break
            except Exception as e:
                print(f"\n❌ 发生错误: {e}")


def main():
    """程序入口点"""
    try:
        assistant = ChatAssistant()
        assistant.run()
    except ValueError as e:
        print(f"❌ 配置错误: {e}")
        print("💡 请检查.env文件中的DEEPSEEK_API_KEY配置")
    except Exception as e:
        print(f"❌ 程序启动失败: {e}")


if __name__ == "__main__":
    main()