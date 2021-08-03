# 项目中UDP沟通对接

## 项目背景

需要利用UDP发送检测信息，包括：检测框信息、目标位置信息、目标图像、目标属性。

测试时需要显示目标视频信息，方便双方联调。


## Demo

### Require

`CMake and OpenCV`

### install 

```
git clone https://github.com/chenbokai/udp_transmission.git

cd udp_transmission/

mkdir build 

cd  build 
cmake ..&&make
```

### message

message command include two parts: client & server

client_msg parameters include(total10) : 

| List0  |List1 |List2 |List3 |List4 |List 5|List6 |List7 |List8 |List9 |
|----|----|----|----|----|----|----|----|----|----|
|State|server|Port|Xmin|Xmax|Ymin|Ymax|Xpos|Ypos|Flag|

State 0,1,2:
* 0 --- init
* 1 --- working
* 2 --- over

Flag 0, 1,2:
* 0 --- no detect
* 1 --- Lable1
* 2 --- Label 2

server_msg only has 1  parameters:
* Port

#### how to run
```
cd  build
./server_msg 2000
./client_msg 127.0.0.1 2000 150 350 200 400 35.85 46.73 2
```
>推荐端口大于1024，0-1024端口被系统占用。

### image

image command include two parts:client& server

client_img has three parameters:
* Server
* Port 
* image Address

server_msg only has 1 parameters:
* Port

#### how to run

```
cd  build
./server_img 2000
./client_img 127.0.0.1 2000 ../image/tst.jpg
```
>接收的图片会以taker_over+端口号的命名 保存在image文件夹中

### video
 
 video command imclude tow parts:client& server

 client_video has three parameters:
 * Server 
 * Port

 server_msg only has 1 parameters:
 * Port

 #### how to run

 ```
 ./server_video 2000
 ./client_video 127.0.0.1 2000 
 ```

### command

image command include two parts:client& server

client_img has three parameters:
* Server
* Port 
* command

server_msg only has 1 parameters:
* Port

Command:
* start
* end

other command will cause error.

 #### how to run

 ```
 ./server_cmd 2000
 ./client_cmd 127.0.0.1 2000  start/end
 ```
## Todo

后期完成脚本编写


