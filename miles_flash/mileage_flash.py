#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk() # 生成一个窗口对象
window.title('里程刷新工具') # 设置窗口标题
window.geometry("650x150")

# Entry
tk.Label(text="里程信息:").pack(padx=5, pady=10, side=tk.LEFT)
node = tk.Entry()
node.pack(padx=5, pady=20, side=tk.LEFT)


def analyze():
	
	t.delete('1.0','end')
	miles = node.get()
	if miles =="":
		print("请输入正确的里程信息")
		return 
#	print(type(miles))
	
	miles_info = str(hex(int(miles)*10))
	#print(miles_info)
	msg_list = list(miles_info)
	msg_list = msg_list[2:]
	if len(msg_list) % 2 == 1:
		msg_list.insert(0,0)

	msg0 = hex(2)

	if len(msg_list) < 4:
		msg1 = '0x' + str(msg_list[-2]) + str(msg_list[-1])
		msg2 = '0x00' 
		msg3 = '0x00' 
		msg4 = '0x00'
	elif len(msg_list) < 6:
		msg1 = '0x' + str(msg_list[-2]) + str(msg_list[-1])
		msg2 = '0x' + str(msg_list[-4]) + str(msg_list[-3])
		msg3 = '0x00' 
		msg4 = '0x00'
	elif len(msg_list) < 8:
		msg1 = '0x' + str(msg_list[-2]) + str(msg_list[-1])
		msg2 = '0x' + str(msg_list[-4]) + str(msg_list[-3])
		msg3 = '0x' + str(msg_list[-6]) + str(msg_list[-5])
		msg4 = '0x00' 
	else:
		msg1 = '0x' + str(msg_list[-2]) + str(msg_list[-1])
		msg2 = '0x' + str(msg_list[-4]) + str(msg_list[-3])
		msg3 = '0x' + str(msg_list[-6]) + str(msg_list[-5])
		msg4 = '0x' + str(msg_list[-8]) + str(msg_list[-7])
	
	var = "ID:0x0cef4217\n"
	var1 = "msg:"+ msg0 + " "+ msg1 + " "+ msg2 + " "+ msg3 + " "  + msg4 + " " + "0xff "*3
	t.insert('end',var)
	t.insert('end',var1)


b = tk.Button(window, text = '解析',  command=analyze)
b.pack(padx=5, pady=20, side=tk.LEFT)


t = tk.Text(window,width="50",height="10",)
t.pack(padx=5, pady=50)

fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")

t.configure(font=fontExample)



window.mainloop() 
