import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("猜数字游戏")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')
        self.root.resizable(False, False)
        
        # 游戏变量
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 7
        self.game_over = False
        
        self.setup_ui()
        self.start_new_game()
        
    def setup_ui(self):
        """设置用户界面"""
        # 标题
        title_label = tk.Label(
            self.root, 
            text="🎯 猜数字游戏", 
            font=("微软雅黑", 20, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=20)
        
        # 游戏说明
        info_text = "我想了一个1-100之间的数字\n你有7次机会猜中它！"
        info_label = tk.Label(
            self.root,
            text=info_text,
            font=("微软雅黑", 12),
            bg='#f0f0f0',
            fg='#34495e'
        )
        info_label.pack(pady=10)
        
        # 剩余次数显示
        self.attempts_label = tk.Label(
            self.root,
            text="",
            font=("微软雅黑", 14, "bold"),
            bg='#f0f0f0',
            fg='#e74c3c'
        )
        self.attempts_label.pack(pady=5)
        
        # 提示信息
        self.hint_label = tk.Label(
            self.root,
            text="请输入你的猜测：",
            font=("微软雅黑", 12),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        self.hint_label.pack(pady=10)
        
        # 输入框
        self.entry = tk.Entry(
            self.root,
            font=("微软雅黑", 14),
            width=15,
            justify='center'
        )
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda e: self.make_guess())
        
        # 猜测按钮
        self.guess_button = tk.Button(
            self.root,
            text="猜测",
            font=("微软雅黑", 12, "bold"),
            bg='#3498db',
            fg='white',
            width=15,
            height=2,
            command=self.make_guess,
            cursor='hand2'
        )
        self.guess_button.pack(pady=10)
        
        # 结果显示区域
        self.result_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.result_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # 结果文本
        self.result_text = tk.Text(
            self.result_frame,
            height=8,
            width=35,
            font=("微软雅黑", 10),
            bg='#ffffff',
            fg='#2c3e50',
            wrap='word',
            state='disabled'
        )
        self.result_text.pack(fill='both', expand=True)
        
        # 按钮框架
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        # 新游戏按钮
        self.new_game_button = tk.Button(
            button_frame,
            text="新游戏",
            font=("微软雅黑", 11),
            bg='#27ae60',
            fg='white',
            width=12,
            command=self.start_new_game,
            cursor='hand2'
        )
        self.new_game_button.pack(side='left', padx=5)
        
        # 退出按钮
        self.quit_button = tk.Button(
            button_frame,
            text="退出",
            font=("微软雅黑", 11),
            bg='#e74c3c',
            fg='white',
            width=12,
            command=self.root.quit,
            cursor='hand2'
        )
        self.quit_button.pack(side='left', padx=5)
        
    def start_new_game(self):
        """开始新游戏"""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.game_over = False
        
        # 更新界面
        self.attempts_label.config(text=f"剩余次数: {self.max_attempts}")
        self.hint_label.config(text="请输入你的猜测：", fg='#2c3e50')
        self.entry.config(state='normal')
        self.guess_button.config(state='normal')
        
        # 清空结果显示
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "🎮 游戏开始！请输入一个1-100之间的数字\n\n")
        self.result_text.config(state='disabled')
        
        # 聚焦到输入框
        self.entry.focus()
        
    def make_guess(self):
        """处理用户猜测"""
        if self.game_over:
            return
            
        try:
            guess = int(self.entry.get())
            self.entry.delete(0, tk.END)
            
            if guess < 1 or guess > 100:
                self.show_result("❌ 请输入1-100之间的数字！\n", 'error')
                return
                
            self.attempts += 1
            remaining = self.max_attempts - self.attempts
            self.attempts_label.config(text=f"剩余次数: {remaining}")
            
            if guess == self.secret_number:
                self.game_won()
            elif guess < self.secret_number:
                self.show_result(f"📈 太小了！你猜的是 {guess}\n", 'hint')
            else:
                self.show_result(f"📉 太大了！你猜的是 {guess}\n", 'hint')
                
            if self.attempts >= self.max_attempts and not self.game_over:
                self.game_over = True
                self.show_result(f"😢 游戏结束！正确答案是 {self.secret_number}\n", 'error')
                self.end_game()
                
        except ValueError:
            self.show_result("❌ 请输入有效的数字！\n", 'error')
            
    def game_won(self):
        """游戏胜利"""
        self.game_over = True
        emoji = "🎉" if self.attempts <= 3 else "🎊" if self.attempts <= 5 else "😊"
        self.show_result(f"{emoji} 恭喜你！猜对了！数字是 {self.secret_number}\n你用了 {self.attempts} 次机会！\n", 'success')
        self.end_game()
        
    def show_result(self, message, msg_type):
        """显示结果消息"""
        self.result_text.config(state='normal')
        
        # 根据消息类型设置颜色
        if msg_type == 'success':
            color = '#27ae60'  # 绿色
        elif msg_type == 'error':
            color = '#e74c3c'  # 红色
        elif msg_type == 'hint':
            color = '#3498db'  # 蓝色
        else:
            color = '#2c3e50'  # 默认颜色
            
        self.result_text.config(fg=color)
        self.result_text.insert(tk.END, message)
        self.result_text.see(tk.END)
        self.result_text.config(state='disabled')
        
    def end_game(self):
        """结束游戏"""
        self.entry.config(state='disabled')
        self.guess_button.config(state='disabled')
        
    def run(self):
        """运行游戏"""
        self.root.mainloop()

if __name__ == "__main__":
    game = GuessNumberGame()
    game.run()
