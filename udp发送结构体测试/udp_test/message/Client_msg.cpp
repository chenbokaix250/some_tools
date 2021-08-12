
#include "../lib/PracticalSocket.h"      // For UDPSocket and SocketException
#include <iostream>               // For cout and cerr
#include <cstdlib>                // For atoi()
using namespace std;

#include "opencv2/opencv.hpp"
using namespace cv;
#include "../config.h"

typedef struct Info{
    uint32_t a;
    uint16_t b;
    uint16_t c;
    uint32_t d;
}info;
int main(int argc, char * argv[]) {
    if ((argc < 3) || (argc > 3)) { // Test for correct number of arguments
        cerr << "Usage: " << argv[0] << " <Server> <Server Port><state>\n";
        exit(1);
    }
    info udpPack;
    udpPack.a = 11223344;
    udpPack.b = 5566;
    udpPack.c = 7788;
    udpPack.d = 990000;

    string servAddress = argv[1]; // First arg: server address
    unsigned short servPort = Socket::resolveService(argv[2], "udp");

    cout<<"client send:"<<udpPack.a<<udpPack.b<<udpPack.c<<endl;
    char *pPack = (char *)&udpPack;



    UDPSocket sock;
    
    sock.sendTo(&udpPack, sizeof(info), servAddress, servPort);

    return 0;
}
