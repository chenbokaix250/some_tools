#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk
import tkinter.messagebox

import platform


if (platform.system() == "Darwin"):
	print("system is Mac")
	
window = tk.Tk() # 生成一个窗口对象
window.title('多包发送生成工具') # 设置窗口标题
window.geometry("640x280")

#声明故障灯变量
l_red = tk.IntVar()
l_yellow = tk.IntVar()
l_green = tk.IntVar()

#创建变量的CheckBox 并利用grid布局

tk.Label(text="故障等级").grid(row=1,column=0)
tk.Checkbutton(text = "RED", variable = l_red).grid(row=1,column=1)
tk.Checkbutton(text = "YELLOW", variable = l_yellow).grid(row=1,column=2)
tk.Checkbutton(text = "GREEN", variable = l_green).grid(row=1,column=3)


# Entry
tk.Label(text="发送节点").grid(row=2,column=0)
node = tk.Entry()
node.grid(row=2,column=1)

# 第一组故障

tk.Label( text = '第一组').grid(row=3,column=0)
tk.Label( text="SPN1:").grid(row=3,column=1)
spn1 = tk.Entry()
spn1.grid(row=3,column=2)
tk.Label( text="FMI1:").grid(row=3,column=3)
fmi1 = tk.Entry()
fmi1.grid(row=3,column=4)

# 第二组故障

tk.Label( text = '第二组').grid(row=4,column=0)
tk.Label( text="SPN2:").grid(row=4,column=1)
spn2 = tk.Entry()
spn2.grid(row=4,column=2)
tk.Label( text="FMI2:").grid(row=4,column=3)
fmi2 = tk.Entry()
fmi2.grid(row=4,column=4)

# 第三组故障

tk.Label( text = '第三组').grid(row=5,column=0)
tk.Label( text="SPN3:").grid(row=5,column=1)
spn3 = tk.Entry()
spn3.grid(row=5,column=2)
tk.Label( text="FMI3:").grid(row=5,column=3)
fmi3 = tk.Entry()
fmi3.grid(row=5,column=4)

# 第四组故障

tk.Label( text = '第四组').grid(row=6,column=0)
tk.Label( text="SPN4:").grid(row=6,column=1)
spn4 = tk.Entry()
spn4.grid(row=6,column=2)
tk.Label( text="FMI4:").grid(row=6,column=3)
fmi4 = tk.Entry()
fmi4.grid(row=6,column=4)

# 第五组故障

tk.Label( text = '第五组').grid(row=7,column=0)
tk.Label( text="SPN5:").grid(row=7,column=1)
spn5 = tk.Entry()
spn5.grid(row=7,column=2)
tk.Label( text="FMI5:").grid(row=7,column=3)
fmi5 = tk.Entry()
fmi5.grid(row=7,column=4)


var = tk.StringVar()

msg = tk.StringVar()

# 解析id和故障等级
def light_id_anly(method):
	l_red_send = l_red.get()
	l_yellow_send = l_yellow.get()
	l_green_send = l_green.get()

	node_send = node.get()
	if node_send == "":
		node_send = '0x00'
	strID = str(node_send)
	list_id = list(strID)
	strID1 = str(list_id[2] + list_id[3])
	if method == 0:
		id_s = '0x18FECA' + strID1
	elif method == 1:
		id_s = '0x18ECFF' + strID1
	elif method == 2:
		id_s = '0x18FBFF' + strID1

	error_num = 0
	if l_red_send == 1:
		error_num = error_num + 16
	if l_yellow_send == 1:
		error_num = error_num + 4
	if l_green_send == 1:
		error_num = error_num + 1

	return id_s,error_num
#解析spn和fmi
def spn_fmi_aly(spnn,fmin):

	list_spn = list(spnn)
	list_spn = list_spn[2:]
	if len(list_spn) %2 == 1:
		list_spn.insert(0,0)
	#print(list_spn[-2],list_spn[-1])
	if len(list_spn) < 3:
		spn_l = '0x' + str(list_spn[-2]) + str(list_spn[-1])
		spn_m = '0x00'
		spn_h = 0
	elif len(list_spn) < 5:
		spn_l = '0x' + str(list_spn[-2]) + str(list_spn[-1])
		spn_m = '0x' + str(list_spn[-4]) + str(list_spn[-3])
		spn_h = 0
	elif len(list_spn) < 7:
		spn_l = '0x' + str(list_spn[-2]) + str(list_spn[-1])
		spn_m = '0x' + str(list_spn[-4]) + str(list_spn[-3])
		spn_h =str(list_spn[-6]) + str(list_spn[-5])

    #将spn高3位和fmi合并输出
	byte4 = int(fmin)+ int(spn_h)*32
	byte4 = hex(byte4)
	byte_node=['0xff',spn_l,spn_m,byte4,'0x7f','0xff','0xff']
	return spn_l,spn_m,byte4
#单包发送
def single_send():
    
	global Entry
	id_s,error_num = light_id_anly(0)
	spnn = hex(int(spn1.get()))
	fmin = fmi1.get()
	spn_l,spn_m,spn_h = spn_fmi_aly(spnn,fmin)
	single=['0xff',spn_l,spn_m,spn_h,'0x7f','0xff','0xff']
	single.insert(0,str(hex(error_num)))
	#print(id_s)
	#print(single)
	return single,id_s

#多包发送
def multi_send(package_num):
    global Entry
    id_s ,error_num = light_id_anly(1)
    id_m ,_ = light_id_anly(2)
	
    spnn1 = hex(int(spn1.get()))
    fmin1 = fmi1.get()
    spn1_l,spn1_m,spn1_h = spn_fmi_aly(spnn1,fmin1)
    spnn2 = hex(int(spn2.get()))
    fmin2 = fmi2.get()
    spn2_l,spn2_m,spn2_h = spn_fmi_aly(spnn2,fmin2)

    if package_num > 2:
        spnn3 = hex(int(spn3.get()))
        fmin3 = fmi3.get()
        spn3_l,spn3_m,spn3_h = spn_fmi_aly(spnn3,fmin3)

    if package_num > 3:
        spnn4 = hex(int(spn4.get()))
        fmin4 = fmi4.get()
        spn4_l,spn4_m,spn4_h = spn_fmi_aly(spnn4,fmin4)
    if package_num > 4:
        spnn5 = hex(int(spn5.get()))
        fmin5 = fmi5.get()
        spn5_l,spn5_m,spn5_h = spn_fmi_aly(spnn5,fmin5)

    if package_num == 2:

        mul2_1 = ['0x20',hex(package_num*2),'0x00',hex(package_num),'0xff','0xCA','0xFE','0x00']
        mul2_2 = ['0x01',hex(error_num),'0xff',spn1_l,spn1_m,spn1_h,'0x7f',spn2_l]
        mul2_3 = ['0x02',spn2_m,spn2_h,'0x7f','0xff','0xff','0xff','0xff']
        return mul2_1,mul2_2,mul2_3,id_s,id_m
    if package_num == 3:

        mul3_1 = ['0x20',hex(package_num*2),'0x00',hex(package_num),'0xff','0xCA','0xFE','0x00']
        mul3_2 = ['0x01',hex(error_num),'0xff',spn1_l,spn1_m,spn1_h,'0x7f',spn2_l]
        mul3_3 = ['0x02',spn2_m,spn2_h,'0x7f',spn3_l,spn3_m,spn3_h,'0x7f']
        return mul3_1,mul3_2,mul3_3,id_s,id_m
    if package_num == 4:

        mul4_1 = ['0x20',hex(package_num*2),'0x00',hex(package_num),'0xff','0xCA','0xFE','0x00']
        mul4_2 = ['0x01',hex(error_num),'0xff',spn1_l,spn1_m,spn1_h,'0x7f',spn2_l]
        mul4_3 = ['0x02',spn2_m,spn2_h,'0x7f',spn3_l,spn3_m,spn3_h,'0x7f']
        mul4_4 = ['0x03',spn4_l,spn4_m,spn4_h,'0x7f','0xff','0xff','0xff']
        return mul4_1,mul4_2,mul4_3,id_s,id_m
    if package_num == 5:

        mul5_1 = ['0x20',hex(package_num*2),'0x00',hex(package_num),'0xff','0xCA','0xFE','0x00']
        mul5_2 = ['0x01',hex(error_num),'0xff',spn1_l,spn1_m,spn1_h,'0x7f',spn2_l]
        mul5_3 = ['0x02',spn2_m,spn2_h,'0x7f',spn3_l,spn3_m,spn3_h,'0x7f']
        mul5_4 = ['0x03',spn4_l,spn4_m,spn4_h,'0x7f',spn5_l,spn5_m,spn5_h]
        mul5_5 = ['0x04','0x7f','0xff','0xff','0xff','0xff','0xff','0xff']
        return mul5_1,mul5_2,mul5_3,mul5_4,mul5_5,id_s,id_m


def hit():

	
	if spn2.get() == "" and spn3.get() == "" and spn4.get() == "" and spn5.get() == "" :
		package_num = 1
	elif spn3.get() == "" and spn4.get() == "" and spn5.get() == "" :
		package_num = 2
	elif spn4.get() == "" and spn5.get() == "" :
		package_num = 3
	elif spn5.get() == "" :
		package_num = 4
	else:
		package_num = 5
	if package_num < 2:
		print("单包发送")
		single,id_s = single_send()
		print("MSG_ID:",id_s,'Data:',single)
	else:
		print("多包发送")
		if(package_num == 2):

			mul2_1,mul2_2,mul2_3,id_s,id_m = multi_send(package_num)
			print("MSG_ID:",id_s,'Data1:',mul2_1)
			print("MSG_ID:",id_m,'Data2:',mul2_2)
			print("MSG_ID:",id_m,'Data3:',mul2_3)

		if(package_num == 3):

			mul3_1,mul3_2,mul3_3,id_s,id_m = multi_send(package_num)
			print("MSG_ID:",id_s,'Data1:',mul3_1)
			print("MSG_ID:",id_m,'Data2:',mul3_2)
			print("MSG_ID:",id_m,'Data3:',mul3_3)

		if(package_num == 4):

			mul4_1,mul4_2,mul4_3,id_s,id_m = multi_send(package_num)
			print("MSG_ID:",id_s,'Data1:',mul4_1)
			print("MSG_ID:",id_m,'Data2:',mul4_2)
			print("MSG_ID:",id_m,'Data3:',mul4_3)

		if(package_num == 5):

			mul5_1,mul5_2,mul5_3,mul5_4,mul5_5,id_s,id_m = multi_send(package_num)
			print("MSG_ID:",id_s,'Data1:',mul5_1)
			print("MSG_ID:",id_m,'Data2:',mul5_2)
			print("MSG_ID:",id_m,'Data3:',mul5_3)
			print("MSG_ID:",id_m,'Data3:',mul5_4)
			print("MSG_ID:",id_m,'Data3:',mul5_5)
			
			
#解析按钮

b = tk.Button(window, text = '解析',  command=hit)
b.grid(row=11,column=4)

window.mainloop() # 创建事件循环（不必理解，照抄即可）

#todo 有空改成在界面显示数据
