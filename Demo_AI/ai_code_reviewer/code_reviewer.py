#!/usr/bin/env python3
"""
项目二：智能代码审查工具
功能：自动分析Python代码质量，生成详细审查报告
"""

import os
import sys
import json
from datetime import datetime

from pathlib import Path
from openai import OpenAI
from config import Config


class CodeReviewer:
    """智能代码审查器核心类"""

    def __init__(self):
        """初始化审查器"""
        try:
            # 验证配置
            Config.validate_config()

            # 初始化DeepSeek客户端
            self.client = OpenAI(
                api_key=Config.API_KEY,
                base_url=Config.API_BASE
            )

            # 初始化属性
            self.review_history = []
            self.current_mode = "basic"

            print("🤖 智能代码审查器初始化完成！")

        except Exception as e:
            print(f"❌ 初始化失败: {e}")
            sys.exit(1)

    def read_code_file(self, file_path):
        """读取代码文件"""
        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"文件不存在: {file_path}")

            if path.suffix != '.py':
                print("⚠️  注意：这不是Python文件，但会继续分析")

            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f"📖 已读取文件: {file_path} ({len(content)} 字符)")
            return content

        except Exception as e:
            raise Exception(f"读取文件失败: {e}")

    def analyze_code_complexity(self, code):
        """简单代码复杂度分析"""
        lines = code.split('\n')
        stats = {
            'total_lines': len(lines),
            'code_lines': len([l for l in lines if l.strip() and not l.strip().startswith('#')]),
            'comment_lines': len([l for l in lines if l.strip().startswith('#')]),
            'function_count': code.count('def '),
            'class_count': code.count('class '),
            'import_count': code.count('import ') + code.count('from ')
        }
        return stats

    def review_code(self, code, mode="basic"):
        """核心代码审查方法"""
        try:
            # 分析代码基础信息
            stats = self.analyze_code_complexity(code)
            print(f"🔍 代码分析: {stats['code_lines']}行代码, {stats['function_count']}个函数")

            # 构建审查提示词
            system_prompt = Config.get_review_prompt(mode)

            user_prompt = f"""
请审查以下Python代码：
文件信息：
- 总行数: {stats['total_lines']}
- 代码行: {stats['code_lines']} 
- 函数数: {stats['function_count']}
- 类数量: {stats['class_count']}
代码内容：
{code}
请进行{Config.REVIEW_MODES[mode]}审查：
"""
            print("🔄 AI分析中...", end="", flush=True)

            # 调用DeepSeek API
            response = self.client.chat.completions.create(
                model=Config.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,
                max_tokens=Config.MAX_TOKENS
            )

            # 处理响应
            review_result = response.choices[0].message.content
            print("\r✅ 代码审查完成！" + " " * 20)

            # 更新历史记录
            self.review_history.append({
                "timestamp": datetime.now().isoformat(),
                "mode": mode,
                "stats": stats,
                "file_size": len(code),
                "result": review_result
            })

            return review_result

        except Exception as e:
            error_msg = f"❌ 代码审查出错: {str(e)}"
            print(f"\r{error_msg}" + " " * 20)
            return error_msg

    def generate_report(self, code, review_result, original_file_path):
        """生成审查报告"""
        try:
            # 创建报告文件名
            original_name = Path(original_file_path).stem
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_file = f"{Config.REPORT_OUTPUT_DIR}/review_{original_name}_{timestamp}.md"

            # 重新分析代码获取统计信息
            stats = self.analyze_code_complexity(code)

            # 构建报告内容
            report_content = f"""# 代码审查报告
            
## 文件信息
- 审查文件: {original_file_path}
- 审查时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- 审查模式: {Config.REVIEW_MODES[self.current_mode]}
- 代码统计: {stats['code_lines']}行代码, {stats['function_count']}个函数

## 代码概览
{code}

## 审查结果
{review_result}

## 统计信息
- 总行数: {stats['total_lines']}
- 代码行: {stats['code_lines']}
- 注释行: {stats['comment_lines']}
- 函数数量: {stats['function_count']}
- 类数量: {stats['class_count']}
- 导入数量: {stats['import_count']}

---
*生成工具: 智能代码审查器 v1.0*
            """
            # 保存报告
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report_content)

            print(f"📊 审查报告已生成: {report_file}")
            return report_file

        except Exception as e:
            print(f"❌ 生成报告失败: {e}")
            return None

    def change_mode(self, new_mode):
        """切换审查模式"""
        if new_mode in Config.REVIEW_MODES:
            self.current_mode = new_mode
            print(f"🔄 已切换到 {new_mode} 模式: {Config.REVIEW_MODES[new_mode]}")
        else:
            print(f"❌ 无效模式，可选: {', '.join(Config.REVIEW_MODES.keys())}")

    def show_modes(self):
        """显示所有审查模式"""
        print("\n📋 可用审查模式:")
        for mode, description in Config.REVIEW_MODES.items():
            print(f"  {mode}: {description}")

    def show_history(self):
        """显示审查历史"""
        if not self.review_history:
            print("📝 暂无审查历史")
            return

        print(f"\n📝 最近 {len(self.review_history)} 次审查:")
        for i, review in enumerate(self.review_history[-5:], 1):
            time_str = review['timestamp'][11:19]
            print(f"{i}. 模式: {review['mode']}, 时间: {time_str}")
            print(f"   统计: {review['stats']['code_lines']}行代码")

    def show_help(self):
        """显示帮助信息"""
        help_text = f"""
📖 代码审查工具使用指南：

【基础命令】
review [文件路径] → 审查指定代码文件
mode [模式] → 切换审查模式
modes → 显示所有审查模式
history → 显示审查历史
help → 显示此帮助信息
quit → 退出程序

【当前状态】
模式: {self.current_mode} ({Config.REVIEW_MODES[self.current_mode]})
历史: {len(self.review_history)} 次审查
        """
        print(help_text)

    def run(self):
        """主运行循环"""
        print("=" * 50)
        print("🤖 智能代码审查工具 v1.0")
        print("=" * 50)
        self.show_help()

        while True:
            try:
                user_input = input("\n🔧 命令：").strip()

                if user_input.lower() == 'quit':
                    print("👋 再见！")
                    break
                elif user_input.lower() == 'help':
                    self.show_help()
                elif user_input.lower() == 'modes':
                    self.show_modes()
                elif user_input.lower() == 'history':
                    self.show_history()
                elif user_input.lower().startswith('mode '):
                    new_mode = user_input[5:].strip()
                    self.change_mode(new_mode)
                elif user_input.lower().startswith('review '):
                    file_path = user_input[7:].strip()
                    self._handle_review_command(file_path)
                else:
                    print("⚠️ 未知命令，输入 'help' 查看帮助")

            except KeyboardInterrupt:
                print("\n\n⚠️ 程序被中断")
                break
            except Exception as e:
                print(f"❌ 发生错误: {e}")

    def _handle_review_command(self, file_path):
        """处理审查命令"""
        try:
            # 读取代码文件
            code_content = self.read_code_file(file_path)

            if not code_content.strip():
                print("⚠️ 文件内容为空")
                return

            # 进行代码审查
            review_result = self.review_code(code_content, self.current_mode)

            # 显示审查结果
            print("\n" + "=" * 50)
            print("📋 代码审查结果")
            print("=" * 50)
            print(review_result)

            # 生成报告
            report_file = self.generate_report(code_content, review_result, file_path)
            if report_file:
                print(f"💾 详细报告已保存至: {report_file}")

        except Exception as e:
            print(f"❌ 审查失败: {e}")

def main():
    try:
        reviewer = CodeReviewer()
        reviewer.run()
    except Exception as e:
        print(f"❌ 程序启动失败: {e}")
        print("💡 请检查：")
        print(" 1. DeepSeek API密钥是否正确配置")
        print(" 2. 网络连接是否正常")

if __name__ == "__main__":
    main()