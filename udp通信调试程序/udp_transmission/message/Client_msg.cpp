
#include "../lib/PracticalSocket.h"      // For UDPSocket and SocketException
#include <iostream>               // For cout and cerr
#include <cstdlib>                // For atoi()
using namespace std;

#include "opencv2/opencv.hpp"
using namespace cv;
#include "../config.h"


int main(int argc, char * argv[]) {
    if ((argc < 10) || (argc > 10)) { // Test for correct number of arguments
        cerr << "Usage: " << argv[0] << " <Server> <Server Port> <Xmin> <Xmax> <Ymin> <Ymax><xpos><ypox><flag>\n";
        exit(1);
    }

    string servAddress = argv[1]; // First arg: server address
    unsigned short servPort = Socket::resolveService(argv[2], "udp");

    string xmin = argv[3];
    string xmax = argv[4];
    string ymin = argv[5];
    string  ymax = argv[6];
    string  xpos = argv[7];
    string  ypos = argv[8];
    string  flag = argv[9];
    string  spacing = " ";

    string  result = xmin + spacing +  xmax  + spacing + ymin  + spacing +  ymax  + spacing +  xpos  + spacing +  ypos  + spacing + flag;
    
    char sendbytes [150];
    strcpy(sendbytes,result.c_str());
    printf("client send: %s\n", result.c_str());  

    UDPSocket sock;
    

    sock.sendTo(sendbytes, sizeof(sendbytes), servAddress, servPort);




    return 0;
}
