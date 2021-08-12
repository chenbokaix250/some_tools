cmake_minimum_required(VERSION 2.8)
project( upd_send )
find_package( OpenCV REQUIRED )

add_executable( server_msg message/Server_msg.cpp lib/PracticalSocket.cpp )
target_link_libraries( server_msg ${OpenCV_LIBS} )
add_executable( client_msg message/Client_msg.cpp lib/PracticalSocket.cpp )
target_link_libraries( client_msg ${OpenCV_LIBS} )

