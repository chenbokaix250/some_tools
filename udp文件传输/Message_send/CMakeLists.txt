cmake_minimum_required(VERSION 3.19)
project(Message_send)

set(CMAKE_CXX_STANDARD 17)

add_executable(Message_send send_client.cpp)
add_executable(Message_recv receive_server.cpp)