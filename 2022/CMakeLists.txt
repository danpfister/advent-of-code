cmake_minimum_required(VERSION 3.5)
project(advent-of-code-2022)

# Set the output directory for executables
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/bin)

# Include the Helpers directory for header files
include_directories(Helpers)

# Optionally set C++ standard (for example, C++17)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add a target for each day's solution
add_executable(day01 day01/day01.cpp Helpers/file_utils.cpp)
add_executable(day01_c day01/day01.c)
add_executable(day02 day02/day02.cpp Helpers/file_utils.cpp)
add_executable(day02_c day02/day02.c)
add_executable(day03 day03/day03.cpp Helpers/file_utils.cpp)
add_executable(day04 day04/day04.cpp Helpers/file_utils.cpp)
add_executable(day05 day05/day05.cpp Helpers/file_utils.cpp)
add_executable(day06 day06/day06.cpp Helpers/file_utils.cpp)
