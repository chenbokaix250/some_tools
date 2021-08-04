#!/bin/bash

cd ../build

echo "发送message1"

./client_msg 127.0.0.1 3000 1 150 250 300 450 35.58 45.77 1 

echo "发送message2"

./client_msg 127.0.0.1 3030 1 150 250 300 450 35.58 45.77 1 


echo "发送image1"

./client_img 127.0.0.1 4000 ../image/a1.jpg 

echo "发送image2"

./client_img 127.0.0.1 4040 ../image/tst.jpg

echo  "完成发送"