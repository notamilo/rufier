from instructions import *
from second import Seconds
from sits import Sits
from runner import Runner
from kivy.core.window import Window
purple = ((188 / 255, 143 / 255, 143 / 255, 1))
Window.clearcolor = purple

age = 7
result = 0
name = ""
p1, p2, p3 = 0, 0, 0


def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction, color=(75 / 255, 0 / 255 ,130 / 255))
        lbl1 = Label(text="Введіть ім'я:", halign="right", color=(75 / 255, 0 / 255 ,130 / 255))
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text="Введіть вік:", halign="right", color=(75 / 255, 0 / 255 ,130 / 255))
        self.in_age = TextInput(text="0", multiline=False)
        self.in_age.input_filter = "int"
        self.btn = Button(text="Почати", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn_color = (0.98, 0.31, 0.8, 1)
        self.btn.background_color = self.btn_color

        self.btn.bind(on_press=self.next)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line2.add_widget(lbl2)
        line1.add_widget(self.in_name)
        line2.add_widget(self.in_age)

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self, instance):
        global name, age, p1
        p1 = check_int(self.in_age.text)
        if p1 == False or p1 <= 0:
            p1 = 0
            self.in_age.text = str(p1)
        else:
            name = self.in_name.text
            age = int(self.in_age.text)
            self.manager.current = "first"


class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)

        tester = Label(text=txt_test1, color=(75 / 255, 0 / 255 ,130 / 255))
        label = Label(text="Введіть результат:", halign="right", color=(75 / 255, 0 / 255 ,130 / 255))
        self.in_result = TextInput(text="0", multiline=False)
        self.in_result.input_filter = "int"
        self.in_result.set_disabled(True)
        self.button = Button(text="Запустити таймер", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.button_color = (0.98, 0.31, 0.8, 1)
        self.button.background_color = self.button_color

        self.button.bind(on_press=self.next)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(label)
        line1.add_widget(self.in_result)

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(tester)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.button)

        self.add_widget(outer)

    def sec_finished(self, *args):
        self.in_result.set_disabled(False)
        self.button.set_disabled(False)
        self.button.text = "Продовжити"
        self.next_screen = True

    def next(self, instance):
        global result
        if not self.next_screen:
            self.button.set_disabled(True)
            self.button.text = "Заміряй пульс"
            self.lbl_sec.start()
        else:
            result = int(self.in_result.text)
            self.manager.current = 'second'


class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.lbl_sits = Sits(30)
        self.run = Runner(30, 1.5, size_hint=(0.4, 1))
        self.run.bind(finished=self.run_finished)

        instr = Label(text=txt_sits, size_hint=(0.5, 1), color=(75 / 255, 0 / 255 ,130 / 255))
        self.btn = Button(text='Продовжити', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn_color = (0.98, 0.31, 0.8, 1)
        self.btn.background_color = self.btn_color
        self.btn.on_press = self.next

        line = BoxLayout()
        vlay = BoxLayout(orientation="vertical", size_hint=(0.3, 1))
        vlay.add_widget(self.lbl_sits)
        line.add_widget(instr)
        line.add_widget(vlay)
        line.add_widget(self.run)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def run_finished(self, *args):
        self.btn.set_disabled(False)
        self.btn.text = "Продовжити"
        self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.lbl_sits.next)
        else:
            self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        self.next_screen = False

        self.stage = 0
        super().__init__(**kwargs)
        instr = Label(text=txt_test3, color=(75 / 255, 0 / 255 ,130 / 255))
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.lbl1 = Label(text='Рахуйте пульс', color=(75 / 255, 0 / 255 ,130 / 255))

        lbl_result1 = Label(text='Результат:', halign='right', color=(75 / 255, 0 / 255 ,130 / 255))
        self.in_result1 = TextInput(text='0', multiline=False)
        self.in_result1.input_filter = "int"
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result2 = Label(text='Результат після відпочинку:', halign='right', color=(75 / 255, 0 / 255 ,130 / 255))
        self.in_result2 = TextInput(text='0', multiline=False)
        self.in_result2.input_filter = "int"

        self.in_result1.set_disabled(True)
        self.in_result2.set_disabled(True)
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)
        self.btn = Button(text='Почати', size_hint=(0.3, 0.5), pos_hint={'center_x': 0.5})
        self.btn_color = (0.98, 0.31, 0.8, 1)
        self.btn.background_color = self.btn_color
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl1)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl1.text = 'Відпочинок'
                self.lbl_sec.restart(30)
                self.in_result1.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl1.text = 'Рахуйте пульс'
                self.lbl_sec.restart(15)
            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = 'Завершити'
                self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)
            if p2 == False:
                p2 = 0
                self.in_result1.text = str(p2)
            elif p3 == False:
                p3 = 0
                self.in_result2.text = str(p3)
            else:
                self.manager.current = 'result'


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = Label(text='', color=(75 / 255, 0 / 255 ,130 / 255))
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + '\n' + test(p1, p2, p3, age)


class HeartAttack(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="pulse"))
        sm.add_widget(PulseScr(name="first"))
        sm.add_widget(CheckSits(name="second"))
        sm.add_widget(PulseScr2(name="pulse2"))
        sm.add_widget(Result(name='result'))
        return sm


app = HeartAttack()
app.run()
