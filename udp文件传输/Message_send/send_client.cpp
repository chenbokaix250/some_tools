#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <unistd.h>

void sendBinaryData(const std::vector<char>& data,const std::string& destinationIP,int destinationPort){
    int socketFD= socket(AF_INET,SOCK_DGRAM,0);
    if(socketFD == -1){
        std::cerr<<"Failed to create socket"<<std::endl;
        return;
    }

    sockaddr_in destinationAddr{};
    destinationAddr.sin_family = AF_INET;
    destinationAddr.sin_port = htons(destinationPort);

    if (inet_pton(AF_INET, destinationIP.c_str(), &(destinationAddr.sin_addr)) <= 0) {
        std::cerr << "Invalid destination IP address" << std::endl;
        close(socketFD);
        return;
    }

    std::size_t dataSize = data.size();
    std::size_t totalSent = 0;
    std::size_t packageSize = 8;
    std::vector<char> packet(packageSize);

    while(totalSent < dataSize){
        std::size_t remaining = dataSize - totalSent;
        std::size_t currentPacketSize = (remaining<packageSize)?remaining:packageSize;
        std::copy(data.begin()+totalSent,data.begin()+totalSent+currentPacketSize,packet.begin());
        ssize_t sent = sendto(socketFD, packet.data(), currentPacketSize, 0, (sockaddr*)&destinationAddr, sizeof(destinationAddr));
        if (sent == -1) {
            std::cerr << "Failed to send data" << std::endl;
            break;
        }

        totalSent += currentPacketSize;
    }
    close(socketFD);
}

std::vector<char> readFile(const std::string& filename) {
    std::ifstream file(filename, std::ios::binary | std::ios::ate);
    if (!file) {
        std::cerr << "Failed to open file: " << filename << std::endl;
        return {};
    }

    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<char> data(size);
    if (!file.read(data.data(), size)) {
        std::cerr << "Failed to read data from file: " << filename << std::endl;
        return {};
    }

    file.close();

    return data;
}
int main(){
    std::string destinationIP = "127.0.0.1";
    int destinationPort = 12345;
    std::vector<char> fileData = readFile("source_file.txt");
    std::cout<<fileData.size()<<std::endl;
    sendBinaryData(fileData,destinationIP,destinationPort);

    return 0;
}