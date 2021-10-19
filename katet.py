#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
	katet
    программа реалезует:
	Извлечение квадратного корня, взведение в стеаень, расчет гипотенузы.
    операции вынесены в классы
'''
import os
class Calc_func:
	def calculate_katet(self):
		print ("Расчет гипотенузы.")
		katet1 = int(input("Катет один: "))
		katet2 = int(input("Катет два : "))
		gipotenuza = katet1**2 + katet2**2
		print ("Гипотенуза равна: ", gipotenuza)
		#print("---=====================---")
		return
	def calculate_koren_kvadrat(self):
		inkoren = float(input("Число для извлечения квадратного корня: "))
		koren = inkoren**0.5
		print ("Корень квадратный: ", koren)
		#print("---=====================---")
		return

	def calculate_stepen(self):
		num_for_stepen = int(input("Число, возводимое в степень: "))
		stepen = int(input("Степень числа: "))
		print ("Результат возведения в степень: ", num_for_stepen**stepen)
        #print("---=====================---")
		return

class Display_msg:
	def display_menu_main(self):
		print("---=====================---")
		print("Меню:")
		print("[1] Расчет гипотенузы")
		print("[2] Квадратный корень")
		print("[3] Возведение числа в степень")
		print("---------------------------")
		print("[0] Завершить программу")
		print("---=====================---")

	def display_out_error(self):
		print ("+---====================---+")
		print ("| Внимание! Неверное меню. |")
		print ("+---====================---+")

	def display_trasparant_exit(self):
		print ("+--------------------+")
		print ("|Программа завершена.|")
		print ("+--------------------+")

	def display_trasparant_Error(self):
		print ("Внимание! Неверное меню.")

	def check_enter_char(self, case_switch):
	#функция проверят ввод пользователя
		if case_switch == '0':
			a = "Программа завершена"
			b = '0'
			return a, b
		elif case_switch == '1':
			#перед отображением нового окна, очистить окно
			os.system('cls')
			cl.calculate_katet()
			a = "Расчет гипотенузы"
			b = '1'
			return a, b
		elif case_switch == '2':
			#перед отображением нового окна, очистить окно
			os.system('cls')
			cl.calculate_koren_kvadrat()
			a = "Квадратный корень"
			b = '2'
			return a, b
		elif case_switch == '3':
			#перед отображением нового окна, очистить окно
			os.system('cls')
			cl.calculate_stepen()
			a = "Возведение числа в степень"
			b = '3'
			return a, b
		else:
			dspl_msg.display_trasparant_Error()
			a = "Неверный ввод"
			b = ''
			return a, b


if __name__ == '__main__':
	cl = Calc_func()
	dspl_msg = Display_msg()
	while True:
		#отобразить меню пользователя
		dspl_msg.display_menu_main()
		#проверка еорректного ввода
		main_mnu_press = input("==>")
		if main_mnu_press == '0':
			dspl_msg.display_trasparant_exit()
			break
		dspl_msg.check_enter_char(main_mnu_press)
