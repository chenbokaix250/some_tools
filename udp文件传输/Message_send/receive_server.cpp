#include <sys/socket.h>
#include <netinet/in.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <unistd.h>
std::vector<char> receiveBinaryData(int listeningPort,std::size_t dataSize){
    int socketFD = socket(AF_INET, SOCK_DGRAM, 0);
    if (socketFD == -1) {
        std::cerr << "Failed to create socket" << std::endl;
        return {};
    }

    // 绑定本地地址和端口
    sockaddr_in localAddr{};
    localAddr.sin_family = AF_INET;
    localAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    localAddr.sin_port = htons(listeningPort);
    if (bind(socketFD, (sockaddr*)&localAddr, sizeof(localAddr)) == -1) {
        std::cerr << "Failed to bind socket" << std::endl;
        close(socketFD);
        return {};
    }

    std::vector<char> receivedData(dataSize);

    std::size_t totalReceived = 0;
    std::size_t packetSize = 8;
    std::vector<char> packet(packetSize);

    while(totalReceived<dataSize){
        std::size_t remaining = dataSize - totalReceived;
        std::size_t currentPacketSize = (remaining < packetSize) ? remaining : packetSize;

        ssize_t received = recv(socketFD, packet.data(), currentPacketSize, 0);
        if (received == -1) {
            std::cerr << "Failed to receive data" << std::endl;
            break;
        }

        std::copy(packet.begin(), packet.begin() + received, receivedData.begin() + totalReceived);

        totalReceived += received;
    }

    close(socketFD);
    return receivedData;
}
void saveToFile(const std::vector<char>& data) {
    std::ofstream file("file.txt", std::ios::binary);
    if (!file) {
        std::cerr << "Failed to create file" << std::endl;
        return;
    }

    file.write(data.data(), data.size());
    file.close();

    std::cout << "File saved successfully." << std::endl;
}

int main(){

    int listeningPort = 12345;
    std::size_t dataSize = 946;  // 假设知道要接收的数据大小

    std::vector<char> receivedData = receiveBinaryData(listeningPort, dataSize);

    std::cout << "Received data size: " << receivedData.size() << std::endl;

    saveToFile(receivedData);

    return 0;
}