#include "nlohmann/json.hpp"
#include <fstream>
#include <sstream>
#include <iostream>

int main(){
    std::ifstream inputFile("config.json");
    std::stringstream buffer;
    buffer<<inputFile.rdbuf();
    std::string jsonString = buffer.str();
    nlohmann::json config = nlohmann::json::parse(jsonString);

    std::string name = config["name"];
    std::string url = config["url"];
    int page = config["page"];
    bool isNonProfit = config["isNonProfit"];

    std::cout << "Name: " << name << std::endl;
    std::cout << "URL: " << url << std::endl;
    std::cout << "Page: " << page << std::endl;
    std::cout << "Is Non-Profit: " << std::boolalpha << isNonProfit << std::endl;

    std::string street = config["address"]["street"];
    std::string city = config["address"]["city"];
    std::string country = config["address"]["country"];

    std::cout << "Address: " << street << ", " << city << ", " << country << std::endl;

    for (const auto& link : config["links"]) {
        std::string linkName = link["name"];
        std::string linkUrl = link["url"];
        std::cout << "Link: " << linkName << " - " << linkUrl << std::endl;
    }

    return 0;

}