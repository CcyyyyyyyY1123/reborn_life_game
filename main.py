import tkinter as tk
from tkinter import messagebox
import random
class Character:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.age = 0  # Initialize age for tracking
        self.talents = {'体魄': 0, '快乐': 0, '美貌': 0, '经验': 0, '金钱': 0,'人脉':0,'正气':0}
        self.events_history = []  # History of events that occur
        self.age_limit = random.randint(60, 99)
        self.background = random.choice(['武术世家', '书香世家'])  # Randomly assign a family background
        self.events_history.append(f"出生在{self.background}")
        self.generate_initial_talents()
    def generate_initial_talents(self):
        """Initialize talents based on family background."""
        base_talent = 10  # Base talent value for all attributes
        for talent in self.talents:
            self.talents[talent] = random.randint(1, 100) + base_talent

        # Adjust specific talents based on family background
        if self.background == '武术世家':
            self.talents['体魄'] += 20  # Boost physical talent for martial arts family
        elif self.background == '书香世家':
            self.talents['经验'] += 20  # Boost experience for scholarly family

    def generate_talents(self):
        """随机生成天赋值"""
        for talent in self.talents:
            self.talents[talent] = random.randint(1, 100)

    def update_age(self, increment=1):
        """Update the character's age and check for age limit."""
        self.age += increment
        if self.age >= self.age_limit:
            return True  # 返回一个标志表示达到年龄上限
        return False

class EventManager:
    def __init__(self):
        self.events = {
            'childhood': ["你出现在一个书香世家""你出生在一个武术世家"],

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

        tk.Label(self, text="角色的名字：").grid(row=0, column=0, sticky="w")
        self.name_var = tk.Entry(self)
        self.name_var.grid(row=0, column=1, sticky="ew")  # Expand entry horizontally

        tk.Label(self, text="角色的性别：").grid(row=1, column=0, sticky="w")
        self.gender_var = tk.StringVar(self)
        self.gender_var.set("男")
        genders = ["男", "女"]
        self.gender_menu = tk.OptionMenu(self, self.gender_var, *genders)
        self.gender_menu.grid(row=1, column=1, sticky="ew")

        self.grid_columnconfigure(1, weight=1)  # Make the second column expandable

        # Talent display setup with grid
        self.talents_labels = {}
        row = 2
        for talent in ["体魄", "快乐", "美貌", "经验", "金钱", '人脉', '正气']:
            tk.Label(self, text=f"{talent}：").grid(row=row, column=0, sticky="w")
            label = tk.Label(self, text="0")
            label.grid(row=row, column=1, sticky="ew")
            self.talents_labels[talent] = label
            row += 1

        # Buttons
        tk.Button(self, text="生成天赋", command=self.generate_talents).grid(row=row, column=0, columnspan=2, sticky="ew")
        tk.Button(self, text="开始游戏", command=self.start_game).grid(row=row + 1, column=0, columnspan=2, sticky="ew")

        self.pack(fill="both", expand=True)  # Make the frame expand with the window


    def generate_talents(self):
        """ Generate and update talent values display """
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
        self.eighteen_event_triggered = False
        self.create_widgets()
        self.pack(fill="both", expand=True)

    def create_widgets(self):
        tk.Label(self, text=f"角色名: {self.character.name}").pack(fill="x")
        tk.Label(self, text=f"性别: {self.character.gender}").pack(fill="x")
        self.age_label = tk.Label(self, text=f"年龄: {self.character.age}")
        self.age_label.pack(fill="x")
        self.talent_labels = {}
        for talent, value in self.character.talents.items():
            label = tk.Label(self, text=f"{talent}: {value}")
            label.pack(fill="x")
            self.talent_labels[talent] = label
        self.event_label = tk.Label(self, text="当前事件: 等待发生")
        self.event_label.pack(fill="x")
        self.history_listbox = tk.Listbox(self, height=10, width=50)
        self.history_listbox.pack(fill="both", expand=True)
        tk.Button(self, text="下一步", command=self.next_step).pack(fill="x")

    def next_step(self):
        # Check special events before age update
        event_triggered = False
        age_increment = 1  # Default age increment

        if self.character.age == 0:
            self.special_choice_event()
            age_increment = 3  # Jump from 0 to 3 years
            event_triggered = True
        elif self.character.age == 3:
            self.three_year_old_event()
            age_increment = 3  # Jump from 3 to 6 years
            event_triggered = True
        elif self.character.age == 6:
            self.six_year_old_event()
            age_increment = 6  # Jump from 6 to 12 years
            event_triggered = True
        elif self.character.age == 12:
            self.twelve_year_old_event()
            age_increment = 6  # Jump from 12 to 18 years
            event_triggered = True
        elif self.character.age >= 18:
            self.eighteen_year_old_event()
            age_increment = 1  # From 18 onward, age normally
            event_triggered = True

            # Trigger a random event if the character is 18 or older
            self.trigger_random_event()

        # Update age by the determined increment
        for _ in range(age_increment):
            age_over = self.character.update_age()
            if age_over:
                messagebox.showinfo("游戏结束", f"{self.character.name}已达到{self.character.age_limit}岁, 游戏结束。")
                self.master.destroy()  # Close the window
                return

        # Update the age display
        self.age_label.config(text=f"年龄: {self.character.age}")

        # Check and trigger any talent based events if no special age event was triggered
        if not event_triggered:
            events = self.character.check_talent_events()
            if events:
                event_text = "\n".join(events)
                self.event_label.config(text=f"当前事件: {event_text}")
                for event in events:
                    self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event}")

    def trigger_random_event(self):
        """Triggers a random event from the available events."""
        random_event = random.randint(1, 10)
        if random_event == 1:
            self.random_event_1()
        elif random_event == 2:
            self.random_event_2()
        elif random_event == 3:
            self.random_event_3()
        elif random_event == 4:
            self.random_event_4()
        elif random_event == 5:
            self.random_event_5()
        elif random_event == 6:
            self.random_event_6()
        elif random_event == 7:
            self.random_event_7()
        elif random_event == 8:
            self.random_event_8()
        elif random_event == 9:
            self.random_event_9()
        elif random_event == 10:
            self.random_event_10()

    def determine_age_category(self):
        # Determine the age category based on the character's age
        if self.character.age < 13:
            return 'childhood'
        elif self.character.age < 20:
            return 'teenage'
        else:
            return 'young_adult'

    def special_choice_event(self):
        """触发0岁时的特殊事件对话框，自定义按钮文本，显示家庭背景"""
        dialog = tk.Toplevel(self)
        dialog.title("出生与抓周礼")

        # 显示家庭背景信息
        family_background_text = f"你出生在一个{'武术' if self.character.background == '武术世家' else '书香'}世家。"
        tk.Label(dialog, text=family_background_text).pack(pady=10)
        tk.Label(dialog, text="爹娘给你办了抓周礼，你把手伸向：").pack(pady=10)
        tk.Label(dialog, text="A. 小木剑").pack(pady=5)
        tk.Label(dialog, text="B. 小裙子").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['经验'] += 10
                event_description = "选择了小木剑，经验增加10点"
            else:
                self.character.talents['美貌'] += 10
                event_description = "选择了小裙子，美貌增加10点"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)  # 设置为临时窗口，当主窗口关闭时一起关闭
        dialog.grab_set()  # 模态窗口，阻塞其它窗口操作
        self.master.wait_window(dialog)  # 等待对话框关闭

    def three_year_old_event(self):
        """触发3岁时的特殊事件对话框"""
        dialog = tk.Toplevel(self)
        dialog.title("下雪天的选择")
        tk.Label(dialog, text="下雪天，小伙伴和你说门口的铁狮子是甜的，他们都去舔了，你决定：").pack(pady=10)
        tk.Label(dialog, text="A. 舔").pack(pady=5)
        tk.Label(dialog, text="B. 不舔").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['快乐'] += 10
                self.history_listbox.insert(tk.END, f"{self.character.age}岁: 选择了舔铁狮子，快乐增加10点")
            else:
                self.character.talents['经验'] += 10
                self.history_listbox.insert(tk.END, f"{self.character.age}岁: 选择了不舔铁狮子，经验增加10点")
            dialog.destroy()
            self.update_talent_display()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)  # 设置为临时窗口，当主窗口关闭时一起关闭
        dialog.grab_set()  # 模态窗口，阻塞其它窗口操作
        self.master.wait_window(dialog)  # 等待对话框关闭

    def six_year_old_event(self):
        """触发6岁时的特殊事件对话框"""
        dialog = tk.Toplevel(self)
        dialog.title("门牙事件")
        tk.Label(dialog, text="你的两颗门牙掉了，小伙伴们笑你许久，但没过多久他们也纷纷掉了门牙。").pack(pady=10)
        tk.Label(dialog, text="这让你感到不那么尴尬，并鼓励了你。（体魄+2）").pack(pady=10)

        tk.Button(dialog, text="好的", command=lambda: handle_accept(dialog)).pack(pady=20)

        def handle_accept(dialog):
            self.character.talents['体魄'] += 2
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: 门牙掉落，体魄增加2点")
            dialog.destroy()
            self.update_talent_display()

        dialog.transient(self.master)  # 设置为临时窗口，当主窗口关闭时一起关闭
        dialog.grab_set()  # 模态窗口，阻塞其它窗口操作
        self.master.wait_window(dialog)  # 等待对话框关闭

    def twelve_year_old_event(self):
        """触发12岁时的特殊事件对话框"""
        dialog = tk.Toplevel(self)
        dialog.title("古玩店的选择")
        tk.Label(dialog, text="你在古玩店看见一件很喜欢的物件，你决定：").pack(pady=10)
        tk.Label(dialog, text="A. 买").pack(pady=5)
        tk.Label(dialog, text="B. 不买").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['金钱'] -= 1000
                self.history_listbox.insert(tk.END, f"{self.character.age}岁: 购买了赝品，金钱减少1000")
            else:
                self.character.talents['经验'] += 10
                self.history_listbox.insert(tk.END, f"{self.character.age}岁: 拒绝购买，经验增加10")
            dialog.destroy()
            self.update_talent_display()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)  # 设置为临时窗口，当主窗口关闭时一起关闭
        dialog.grab_set()  # 模态窗口，阻塞其它窗口操作
        self.master.wait_window(dialog)  # 等待对话框关闭

    def eighteen_year_old_event(self):
        """触发18岁时的特殊事件对话框，确保只触发一次"""
        if not self.eighteen_event_triggered:  # 检查事件是否已经被触发过
            dialog = tk.Toplevel(self)
            dialog.title("生命的抉择")
            tk.Label(dialog, text="你突然觉得不能碌碌终生，决定卷死所有人，你决定：").pack(pady=10)
            tk.Label(dialog, text="A. 锻炼").pack(pady=5)
            tk.Label(dialog, text="B. 打扮").pack(pady=5)

            def handle_choice(choice):
                if choice == 'A':
                    self.character.talents['体魄'] += 6
                    self.history_listbox.insert(tk.END, f"{self.character.age}岁: 选择锻炼，体魄增加6点")
                else:
                    self.character.talents['美貌'] += 10
                    self.history_listbox.insert(tk.END, f"{self.character.age}岁: 选择打扮，美貌增加10点")
                dialog.destroy()
                self.update_talent_display()

            tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
            tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

            dialog.transient(self.master)  # 设置为临时窗口，当主窗口关闭时一起关闭
            dialog.grab_set()  # 模态窗口，阻塞其它窗口操作
            self.master.wait_window(dialog)  # 等待对话框关闭

            self.eighteen_event_triggered = True  # 触发后将标志位设为真

    def random_event_1(self):
        """Random event 1"""
        dialog = tk.Toplevel(self)
        dialog.title("你正要出门上工，撞到邻居家的妹妹。")
        tk.Label(dialog, text="她苦着脸，问你能不能帮忙修一下她家坏掉的门，你打算？").pack(pady=10)
        tk.Label(dialog, text="A. 帮帮她吧（经验+8，快乐+2）").pack(pady=5)
        tk.Label(dialog, text="B. 不去（金钱+10%，正气-2）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['经验'] += 8
                self.character.talents['快乐'] += 2
                event_description = "帮帮她吧，正气增加8点，快乐增加2点"
            else:
                self.character.talents['金钱'] *= 1.1  # Increase money by 10%
                self.character.talents['正气'] -= 2
                event_description = "不去帮忙，金钱增加10%，正气减少2点"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_event_2(self):
        """Random event 2"""
        dialog = tk.Toplevel(self)
        dialog.title("一个脏兮兮的乞丐来到你身边。")
        tk.Label(dialog, text="水汪汪的大眼睛直勾勾地盯着你的蒸饺，你决定？").pack(pady=10)
        tk.Label(dialog, text="A. 买一包给他吃（经验+10，快乐+5）").pack(pady=5)
        tk.Label(dialog, text="B. 将他赶走（经验+5，快乐-10）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['经验'] += 10
                self.character.talents['快乐'] += 5
                event_description = "买一包给他吃，正气增加10点，快乐增加5点"
            else:
                self.character.talents['经验'] += 5
                self.character.talents['快乐'] -= 10
                event_description = "将他赶走，江湖经验增加5点，正气减少10点"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_event_3(self):
        """Random event 3"""
        dialog = tk.Toplevel(self)
        dialog.title("你在酒楼喝酒，见一青年才俊不满朝中行为，在墙壁上题诗讽刺。")
        tk.Label(dialog, text="你决定？").pack(pady=10)
        tk.Label(dialog, text="A. 老子也能写！加入他（江湖经验+3，快乐-2）").pack(pady=5)
        tk.Label(dialog, text="B. 大逆不道，拳击警告（经验+10，体魄+2）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['经验'] += 3
                self.character.talents['快乐'] -= 2
                event_description = "加入他，江湖经验增加3点，快乐减少2点"
            else:
                self.character.talents['经验'] += 10
                self.character.talents['体魄'] += 2
                event_description = "拳击警告，正气增加10点，体魄增加2点"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_event_4(self):
        """Random event 4"""
        dialog = tk.Toplevel(self)
        dialog.title("武馆掌柜正大声呵斥一名弱女子。")
        tk.Label(dialog, text="你打算？").pack(pady=10)
        tk.Label(dialog, text="A. 劝阻掌柜，有话好说（经验+25，金钱-800000）").pack(pady=5)
        tk.Label(dialog, text="B. 少掺和为妙（经验+15，快乐-10）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['经验'] += 25
                self.character.talents['金钱'] -= 800000
                event_description = "劝阻掌柜，正气增加25点，金钱减少800000"
            else:
                self.character.talents['经验'] += 15
                self.character.talents['快乐'] -= 10
                event_description = "少掺和为妙，江湖经验增加15点，快乐减少10点"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_event_5(self):
        """Random event 5"""
        dialog = tk.Toplevel(self)
        dialog.title("为扩大宣传饮品，你打算请一位代言人。")
        tk.Label(dialog, text="你选择：").pack(pady=10)
        tk.Label(dialog, text="A. 仙风道骨李大白（金钱+888888）").pack(pady=5)
        tk.Label(dialog, text="B. 悲天悯人杜子帅（金钱+999999）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['金钱'] += 888888
                event_description = "选择了仙风道骨李大白，金钱增加888888"
            else:
                self.character.talents['金钱'] += 999999
                event_description = "选择了悲天悯人杜子帅，金钱增加999999"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_event_6(self):
        """Random event 6"""
        dialog = tk.Toplevel(self)
        dialog.title("你的共享轿子生意越做越大，影响到了对家生意，他们派人与你谈判。")
        tk.Label(dialog, text="你决定：").pack(pady=10)
        tk.Label(dialog, text="A. 与对家达成合作协议（人脉+25，金钱-10%）").pack(pady=5)
        tk.Label(dialog, text="B. 没得商量（金钱+71000，快乐+5）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['人脉'] += 25
                self.character.talents['金钱'] -= int(self.character.talents['金钱'] * 0.1)
                event_description = "与对家达成合作协议，人脉增加25，金钱减少10%"
            else:
                self.character.talents['金钱'] += 71000
                self.character.talents['快乐'] += 5
                event_description = "没得商量，金钱增加71000，快乐增加5"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_event_7(self):
        """Random event 7"""
        dialog = tk.Toplevel(self)
        dialog.title("你的生意宣传收效甚好，有人问你是不是上面有人，你怎么回答？")
        tk.Label(dialog, text="你选择：").pack(pady=10)
        tk.Label(dialog, text="A. 没人，全靠一身正气！（经验+25，金钱+25%）").pack(pady=5)
        tk.Label(dialog, text="B. 撒谎说上面有人（金钱-28%，正气-5）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['经验'] += 25
                self.character.talents['金钱'] += int(self.character.talents['金钱'] * 0.25)
                event_description = "没人，全靠一身正气！正气增加25，金钱增加25%"
            else:
                self.character.talents['金钱'] -= int(self.character.talents['金钱'] * 0.28)
                self.character.talents['正气'] -= 5
                event_description = "撒谎说上面有人，金钱减少28%，经验减少5"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_event_8(self):
        """Random event 8"""
        dialog = tk.Toplevel(self)
        dialog.title("你的大力宣传标语经常被人破坏，你打算：")
        tk.Label(dialog, text="你选择：").pack(pady=10)
        tk.Label(dialog, text="A. 草里蹲他一波（体魄-2，经验+6）").pack(pady=5)
        tk.Label(dialog, text="B. 换个地方多贴几张（经验+10，金钱+15%）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['体魄'] -= 2
                self.character.talents['经验'] += 6
                event_description = "草里蹲他一波，体魄减少2，江湖经验增加6"
            else:
                self.character.talents['经验'] += 10
                self.character.talents['金钱'] += int(self.character.talents['金钱'] * 0.15)
                event_description = "换个地方多贴几张，经验增加10，金钱增加15%"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_event_9(self):
        """Random event 9"""
        dialog = tk.Toplevel(self)
        dialog.title("西湖边有一位姑娘意欲轻生，你是否一把拉住她？")
        tk.Label(dialog, text="你选择：").pack(pady=10)
        tk.Label(dialog, text="A. 赶紧拉一把（经验+10，快乐+10）").pack(pady=5)
        tk.Label(dialog, text="B. 少管闲事（经验+4）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['经验'] += 10
                self.character.talents['快乐'] += 10
                event_description = "赶紧拉一把，正气增加10，快乐增加10"
            else:
                self.character.talents['经验'] += 4
                event_description = "少管闲事，经验增加4"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def random_event_10(self):
        """Random event 10"""
        dialog = tk.Toplevel(self)
        dialog.title("匿名服务的实施")
        tk.Label(dialog, text="你认为可以如何实施？").pack(pady=10)
        tk.Label(dialog, text="A. 匿名写信下单（金钱+11%，江湖经验+10）").pack(pady=5)
        tk.Label(dialog, text="B. 蒙面约见（金钱-11%，江湖经验+3）").pack(pady=5)

        def handle_choice(choice):
            if choice == 'A':
                self.character.talents['金钱'] *= 1.11  # Increase money by 11%
                self.character.talents['经验'] += 10
                event_description = "匿名写信下单，金钱增加11%，江湖经验增加10"
            else:
                self.character.talents['金钱'] *= 0.89  # Decrease money by 11%
                self.character.talents['经验'] += 3
                event_description = "蒙面约见，金钱减少11%，江湖经验增加3"
            self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
            self.update_talent_display()
            dialog.destroy()

        tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def update_talent_display(self):
        """更新天赋标签显示"""
        for talent, label in self.talent_labels.items():
            label.config(text=f"{talent}: {self.character.talents[talent]}")
    def determine_age_category(self):
        # Determine the age category based on the character's age
        if self.character.age < 13:
            return 'childhood'


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.event_manager = EventManager()  # Instantiate the EventManager once for the app
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class, *args):
        """Destroys current frame and replaces it with a new one."""
        if frame_class == GamePage:
            new_frame = frame_class(self, *args, self.event_manager)  # Only pass the event manager to GamePage
        else:
            new_frame = frame_class(self, *args)  # Do not pass the event manager to other frames
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()