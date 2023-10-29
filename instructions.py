import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

txt_instruction = '''
Ця програма дозволить вам за допомогою тесту Руф'є провести первинну діагностику вашого здоров'я.\n
Проба Руф'є являє собою навантажувальний комплекс, призначений для оцінки працездатності серця при фізичному навантаженні.
У випробуваного визначають частоту пульсу за 15 секунд.
Потім протягом 45 секунд випробуваний виконує 30 присідань.\n
Після закінчення навантаження пульс підраховується знову: число пульсацій за перші 15 секунд, 30 секунд відпочинку, число пульсацій за останні 15 секунд.\n '''


txt_test1 = ''' Заміряйте пульс за 15 секунд.\n
Результат запишіть у відповідне поле. '''


txt_test2 = ''' Виконайте 30 присідань за 45 секунд.\n
Натисніть кнопку "Почати", щоб запустити лічильник присідань.\n
Робіть присідання зі швидкістю лічильника. '''


txt_test3 = ''' Протягом хвилини заміряйте пульс двічі:\n
за перші 15 секунд хвилини, потім за останні 15 секунд.\n
Результати запишіть у відповідні поля. '''


txt_sits = 'Виконайте 30 присідань за 45 секунд.'


txt_index = "Ваш індекс Руф’є:"
txt_workheart = "Працездатність серця:"
txt_nodata = ''' Немає даних для такого віку '''
txt_res = []
txt_res.append(''' Низька. Терміново зверніться до лікаря! ''')
txt_res.append(''' Задовільна. Зверніться до лікаря! ''')
txt_res.append(''' Середня. Можливо, варто додатково обстежитись у лікаря. ''')
txt_res.append(''' Вище середнього ''')
txt_res.append(''' Висока ''')


def ruffier_index(P1, P2, P3):
   return (4 * (P1+P2+P3) - 200) / 10


def neud_level(age):
   norm_age = (min(age, 15) - 7) // 2
   result = 21 - norm_age * 1.5
   return result

def ruffier_result(r_index, level):
   if r_index >= level:
       return 0
   level = level - 4
   if r_index >= level:
       return 1
   level = level - 5
   if r_index >= level:
       return 2
   level = level - 5.5
   if r_index >= level:
       return 3
   return 4 #


def test(p1, p2, p3, age):
   if age < 7:
       return (txt_index + "0", txt_nodata)
   else:
       ruff_index = ruffier_index(p1, p2, p3)
       result = txt_res[ruffier_result(ruff_index, neud_level(age))]
       res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
       return res
