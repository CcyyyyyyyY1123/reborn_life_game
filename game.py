import tkinter as tk
from tkinter import messagebox
import random
class Character:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.age = 0  # Initialize age for tracking
        self.talents = {'体魄': 0, '快乐': 0, '美貌': 0, '经验': 0, '金钱': 0}
        self.events_history = []  # History of events that occur
        self.age_limit = random.randint(60, 99)
    def generate_talents(self):
        """随机生成天赋值"""
        for talent in self.talents:
            self.talents[talent] = random.randint(1, 100)

    def update_age(self, increment=1):
        """Update the character's age and check for age limit."""
        self.age += increment
        if self.age >= self.age_limit:
            return True

    def check_talent_events(self):
        """Check for any special events triggered by reaching certain talent thresholds."""
        events_triggered = []
        if self.talents['体魄'] >= 80:
            events_triggered.append("体力非常好，参加马拉松，增加快乐和正气")
            self.talents['快乐'] += 5
            self.talents['经验'] += 5
        if self.talents['快乐'] >= 90:
            events_triggered.append("保持良好心态，吸引了更多朋友，增加社交圈影响力和金钱")
            self.talents['金钱'] += 100
        if self.talents['经验'] >= 75:
            events_triggered.append("正直行为在社区中获得尊重，增加工作机会")
            self.talents['金钱'] += 50
        if self.talents['金钱'] >= 1000:
            events_triggered.append("金钱充裕，选择进行投资，影响未来的金钱增长速度")
        self.events_history.extend(events_triggered)
        return events_triggered

class EventManager:
    def __init__(self):
        self.events = {
            'childhood': ["在幼儿园表现出色，增加快乐和正气", "生病住院，减少体魄和金钱"],
            'teenage': ["参加学校体育活动，提高体魄", "参与学术竞赛，获得奖学金，增加金钱和经验"],
            'young_adult': ["通过打工获得宝贵经验，提高正气和体魄", "经历一次失败的恋爱，减少快乐但增加经验"]
        }

    def trigger_event(self, age_category):
        """Randomly triggers an event based on the age category."""
        possible_events = self.events.get(age_category, [])
        if possible_events:
            return random.choice(possible_events)
        return ""

class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("重生模拟器")
        self.character = None
        self.event_manager = EventManager()


        tk.Label(self, text="角色的名字：").grid(row=0, column=0)
        self.name_var = tk.Entry(self)
        self.name_var.grid(row=0, column=1)


        tk.Label(self, text="角色的性别：").grid(row=1, column=0)
        self.gender_var = tk.StringVar(self)
        self.gender_var.set("男")  # default value
        genders = ["男", "女"]
        self.gender_menu = tk.OptionMenu(self, self.gender_var, *genders)
        self.gender_menu.grid(row=1, column=1)

        # Talent display
        self.talents_labels = {}
        row = 2
        for talent in ["体魄", "快乐", "美貌", "经验", "金钱"]:
            tk.Label(self, text=f"{talent}：").grid(row=row, column=0)
            label = tk.Label(self, text="0")
            label.grid(row=row, column=1)
            self.talents_labels[talent] = label
            row += 1

        # Buttons
        tk.Button(self, text="生成天赋", command=self.generate_talents).grid(row=row, column=0, columnspan=2)
        tk.Button(self, text="开始游戏", command=self.start_game).grid(row=row + 1, column=0, columnspan=2)

        self.pack()

    def generate_talents(self):

        if not self.name_var.get():
            messagebox.showinfo("提示", "请先输入角色名字")
            return

        name = self.name_var.get()
        gender = self.gender_var.get()
        self.character = Character(name, gender)
        self.character.generate_talents()

        # Update UI display
        for talent, label in self.talents_labels.items():
            label.config(text=str(self.character.talents[talent]))

    def start_game(self):
        """ Starts the game """
        if not hasattr(self, 'character') or not all(value > 0 for value in self.character.talents.values()):
            messagebox.showinfo("提示", "请先生成天赋")
            return
        self.master.switch_frame(GamePage, self.character)

class GamePage(tk.Frame):
    def __init__(self, master, character, event_manager):
        super().__init__(master)
        self.character = character
        self.event_manager = event_manager
        self.master.title(f"游戏进行中 - {self.character.name}")
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        tk.Label(self, text=f"角色名: {self.character.name}").pack()
        tk.Label(self, text=f"性别: {self.character.gender}").pack()
        self.age_label = tk.Label(self, text=f"年龄: {self.character.age}")
        self.age_label.pack()
        self.talent_labels = {}
        for talent, value in self.character.talents.items():
            label = tk.Label(self, text=f"{talent}: {value}")
            label.pack()
            self.talent_labels[talent] = label

        self.event_label = tk.Label(self, text="当前事件: 等待发生")
        self.event_label.pack()
        self.history_listbox = tk.Listbox(self, height=10, width=50)
        self.history_listbox.pack()
        tk.Button(self, text="下一步", command=self.next_step).pack()

    def next_step(self):
        # Increase age by one year

        self.age_label.config(text=f"年龄: {self.character.age}")
        if self.character.age == 8:  # 检查是否角色已经8岁
            self.special_choice_event()

        age_over = self.character.update_age()
        self.age_label.config(text=f"年龄: {self.character.age}")


        if age_over:
            messagebox.showinfo("游戏结束", f"{self.character.name}已达到{self.character.age_limit}岁, 游戏结束。")
            self.master.destroy()  # 关闭窗口
            return



        events = self.character.check_talent_events()
        if events:
            event_text = "\n".join(events)
            self.event_label.config(text=f"当前事件: {event_text}")
            for event in events:
                self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event}")  # 添加到事件历史
        else:
            # Trigger a random event based on the age category
            age_category = self.determine_age_category()
            event_text = self.event_manager.trigger_event(age_category)
            self.event_label.config(text=f"当前事件: {event_text}")
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_text}")  # 添加到事件历史

        # Update talent displays
        for talent, label in self.talent_labels.items():
            label.config(text=f"{talent}: {self.character.talents[talent]}")

    def special_choice_event(self):
        """触发8岁时的特殊事件对话框"""
        events = ['事件A', '事件B', '事件C', '事件D']
        selected_event = random.choice(events)
        response = messagebox.askyesno("特殊事件", f"你遇到了一个特殊事件：{selected_event}\n你想要接受这个事件吗？")
        if response:
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: 接受了{selected_event}")
        else:
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: 拒绝了{selected_event}")



    def determine_age_category(self):

        if self.character.age < 13:
            return 'childhood'
        elif self.character.age < 20:
            return 'teenage'
        else:
            return 'young_adult'

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.event_manager = EventManager()
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class, *args):

        if frame_class == GamePage:
            new_frame = frame_class(self, *args, self.event_manager)
        else:
            new_frame = frame_class(self, *args)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()