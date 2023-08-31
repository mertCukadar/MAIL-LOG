cmake_minimum_required(VERSION 3.25)
set(CMAKE_CXX_STANDARD_REQUIRED 17)

project(MailLog VERSION 0.1.0 LANGUAGES C CXX)

#include_directories(include)

file(GLOB SOURCES "Source/*.cpp")

add_executable(MailLog ${SOURCES})

if(WIN32)
    #find_package(WindowsSDK REQUIRED) -- i dont have windowsSDK lib. if you have installed pls delete this comment
    target_link_libraries(MailLog PRIVATE ws2_32.lib)
endif ()

#to take build with cmake you should do these steps to terminal
#1. mkdir build
#2. cd build
#3. cmake ..
#4. cmake --build .
#5. go to debug file run the .exe file
