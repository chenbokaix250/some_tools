#include "../lib/PracticalSocket.h" // For UDPSocket and SocketException
#include <iostream>          // For cout and cerr
#include <cstdlib>           // For atoi()
#include <fstream>
#define BUF_LEN 65540 // Larger than maximum UDP packet size

#include "opencv2/opencv.hpp"
using namespace cv;
#include "../config.h"
#include <typeinfo>

struct Data
{
    uint32_t a;
    uint16_t b;
    uint16_t c;
    uint32_t d;
};
int main(int argc, char * argv[]) {

    if (argc != 2) { // Test for correct number of parameters
        cerr << "Usage: " << argv[0] << " <Server Port>" << endl;
        exit(1);
    }

    unsigned short servPort = atoi(argv[1]); // First arg:  local port

    Data * data;
    int needRecv = sizeof(Data);
    UDPSocket sock(servPort);

    char buffer[BUF_LEN]; // Buffer for echo string
    int recvMsgSize; // Size of received message
    string sourceAddress; // Address of datagram source
    unsigned short sourcePort; // Port of datagram source



    while (1) {
        // Block until receive message from a client
        recvMsgSize = sock.recvFrom(buffer, BUF_LEN, sourceAddress, sourcePort);
        
        cout << "Received packet from " << sourceAddress << ":" << sourcePort << endl;
        cout<<"buffer:"<<buffer<<endl;
        
        cout<<"buffer type:"<<typeid(buffer).name()<<endl;

        cout<<sizeof(buffer)<<endl;

        memcpy(data,buffer,needRecv);

        cout<<data->a<<endl;
        cout<<data->b<<endl;
        cout<<data->c<<endl;
        cout<<data->d<<endl;

    }



   

    return 0;
}
