#include "file_utils.h"

/**
 * @brief returns content of text file as vector of strings
 * 
 * @param fileName 
 * @return std::vector<std::string> 
 */
std::vector<std::string> FileReader::readFile(const std::string& fileName) {
    std::vector<std::string> contents;
    std::ifstream file(fileName);

    if (!file.is_open()) {
        std::cerr << "Unable to open File" << std::endl;
        std::exit(EXIT_FAILURE);
    }

    std::string line;

    while (std::getline(file, line)) {
        contents.push_back(line);
    }

    file.close();

    return contents;
}