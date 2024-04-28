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
    tk.Label(dialog, text="B. 将他赶走（江湖经验+5，快乐-10）").pack(pady=5)

    def handle_choice(choice):
        if choice == 'A':
            self.character.talents['经验'] += 10
            self.character.talents['快乐'] += 5
            event_description = "买一包给他吃，正气增加10点，快乐增加5点"
        else:
            self.character.talents['江湖经验'] += 5
            self.character.talents['正气'] -= 10
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
    tk.Label(dialog, text="B. 大逆不道，拳击警告（正气+10，体魄+2）").pack(pady=5)

    def handle_choice(choice):
        if choice == 'A':
            self.character.talents['江湖经验'] += 3
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
    tk.Label(dialog, text="B. 少掺和为妙（江湖经验+15，快乐-10）").pack(pady=5)

    def handle_choice(choice):
        if choice == 'A':
            self.character.talents['经验'] += 25
            self.character.talents['金钱'] -= 800000
            event_description = "劝阻掌柜，正气增加25点，金钱减少800000"
        else:
            self.character.talents['江湖经验'] += 15
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
    tk.Label(dialog, text="A. 草里蹲他一波（体魄-2，江湖经验+6）").pack(pady=5)
    tk.Label(dialog, text="B. 换个地方多贴几张（江湖经验+10，金钱+15%）").pack(pady=5)

    def handle_choice(choice):
        if choice == 'A':
            self.character.talents['体魄'] -= 2
            self.character.talents['江湖经验'] += 6
            event_description = "草里蹲他一波，体魄减少2，江湖经验增加6"
        else:
            self.character.talents['江湖经验'] += 10
            self.character.talents['金钱'] += int(self.character.talents['金钱'] * 0.15)
            event_description = "换个地方多贴几张，江湖经验增加10，金钱增加15%"
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
    tk.Label(dialog, text="B. 少管闲事（江湖经验+4）").pack(pady=5)

    def handle_choice(choice):
        if choice == 'A':
            self.character.talents['经验'] += 10
            self.character.talents['快乐'] += 10
            event_description = "赶紧拉一把，正气增加10，快乐增加10"
        else:
            self.character.talents['江湖经验'] += 4
            event_description = "少管闲事，江湖经验增加4"
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
            self.character.talents['江湖经验'] += 10
            event_description = "匿名写信下单，金钱增加11%，江湖经验增加10"
        else:
            self.character.talents['金钱'] *= 0.89  # Decrease money by 11%
            self.character.talents['江湖经验'] += 3
            event_description = "蒙面约见，金钱减少11%，江湖经验增加3"
        self.history_listbox.insert(tk.END, f"{self.character.age}岁: {event_description}")
        self.update_talent_display()
        dialog.destroy()

    tk.Button(dialog, text="A", command=lambda: handle_choice('A')).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(dialog, text="B", command=lambda: handle_choice('B')).pack(side=tk.RIGHT, padx=10, pady=10)

    dialog.transient(self.master)
    dialog.grab_set()
    self.master.wait_window(dialog)