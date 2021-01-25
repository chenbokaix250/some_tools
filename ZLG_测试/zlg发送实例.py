
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2021/1/23 4:34 下午
@Author  : chenbokai
@File    : test.py
'''

'''
操作CAN发送报文的步骤
1.打开设备          ZCAN_OpenDevice
2.设置杨勇波特率     GetIProperty()->SetValue
3.初始化通道        ZCAN_InitCAN
4.启动通道          ZCAN_StartCAN
5.发送CAN报文       ZCAN_Transmit
'''

'''
ZLG中python项目的构架方式

1.安装驱动
2.kernels文件夹及相关文件放入python3安装目录
3.zlgcan.py放入目录
4.引用后,执行流程
'''





from zlgcan import *


zcanlib = ZCAN() #实例化对象
handle = zcanlib.OpenDevice(ZCAN_USBCANFD_MINI,0,0)#打开设备
if handle == INVALID_DEVICE_HANDLE:
    print("Open Device failed!")
    exit(0)
print("device handle:%d." %(handle))

info = zcanlib.GetDeviceInf(handle)#获取设备信息
print("Device Information:\n%s" %(info))

#利用SetValue设置属性

def start_can(zcanlib,device_handle,chn):
	ip = zcanlib.GetIProperty(device_handle) #GetIProperty返回设备句柄
	ret = zcanlib.SetValue(ip,str(chn) + "/clock","60000000")#时钟
	if ret != ZCAN_STATUS_OK:
		print("Set CH%d CANFD clock failed!" %(chn))
	ret = zcanlib.SetValue(ip, str(chn) + "/canfd_standard", "0")#通道选择
	if ret != ZCAN_STATUS_OK:
		print("Set CH%d CANFD standard failed!" %(chn))
	ret = zcanlib.SetValue(ip, str(chn) + "/canfd_abit_baud_rate", "250000")#仲裁域波特率
	if ret != ZCAN_STATUS_OK:
		print("Set CH%d CANFD standard failed!" %(chn))
	ret = zcanlib.SetValue(ip, str(chn) + "/canfd_dbit_baud_rate", "250000")##数据域波特率
	if ret != ZCAN_STATUS_OK:
		print("Set CH%d CANFD standard failed!" %(chn))
	ret = zcanlib.SetValue(ip, str(chn) + "/initenal_resistance", "1")#终端电阻 0(禁止) 1(使能)
	if ret != ZCAN_STATUS_OK:
		print("Open CH%d resistance failed!" %(chn))
	zcanlib.ReleaseIProperty(ip)

	#print(ip)
	chn_init_cfg = ZCAN_CHANNEL_INIT_CONFIG()#实例化结构体
	chn_init_cfg.can_type = ZCAN_TYPE_CANFD  #设置CAN类型(此处ZLG应该是CAN和CAHFD搞反了)
	chn_init_cfg.config.can.abit_timing = 250000 #1Mbps #仲裁域波特率
	chn_init_cfg.config.can.dbit_timing = 250000 #1Mbps #数据域波特率
	chn_init_cfg.config.can.mode = 0	#模式

	chn_handle = zcanlib.InitCAN(device_handle, chn, chn_init_cfg)
	#返回值INVALID_CHANNEL_HANDLE时表示操作失败
	#操作成功时,返回通道句柄值,保存句柄,用于操作
	if chn_handle is None:
		return None
	zcanlib.StartCAN(chn_handle) #返回STATUS_OK表示操作成功,STATUS_ERR表示操作失败
	return chn_handle

chn_handle = start_can(zcanlib, handle, 0)	#发送前准备函数
print("channel handle:%d." %(chn_handle))
#Send CAN Messages
transmit_num = 100
msgs = (ZCAN_Transmit_Data * transmit_num)() #msg 发送占位
print(type(msgs))
for i in range(transmit_num):
    msgs[i].transmit_type = 0 #Send Self 0-正常发送 1-自发自收 3-单次自发自收
    msgs[i].frame.eff     = 1 #extern frame  0-标准帧 1-扩展帧
    msgs[i].frame.rtr     = 0 #remote frame  0-数据帧 2-远程帧
    msgs[i].frame.can_id  = 0x18ff1242 + i  #ID
    msgs[i].frame.can_dlc = 8 #数据长度8
    for j in range(msgs[i].frame.can_dlc):
        msgs[i].frame.data[j] = j
ret = zcanlib.Transmit(chn_handle, msgs, transmit_num) #利用Transmit函数完成发送
print("Tranmit Num: %d." % ret)

print("========")
print('ok')