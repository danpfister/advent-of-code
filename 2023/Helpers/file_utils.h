#ifndef FILE_UTILS_H
#define FILE_UTILS_H

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

class FileReader {
    public:
        static std::vector<std::string> readFile(const std::string& fileName);
};

#endif /* FILE_UTILS_H */