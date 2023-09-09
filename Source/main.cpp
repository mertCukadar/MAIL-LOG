#include <iostream>
#include <winsock2.h>

//#pragma comment(lib, "ws2_32.lib")

using namespace std;
bool wsInit() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        cerr << "WSAStartup failed.\n";
        return false;
    }
    return true;
}

int main() {
        if (system("python -m venv env") == 0) {
        const char* activate_command = 
            #ifdef _WIN32
                "env\\Scripts\\activate";
            #else
                "source env/bin/activate";
            #endif

        if (system(activate_command) == 0) {
            if (system("pip install -r ../requirements.txt") == 0) {
                if (system("python main.py") == 0) {
                    std::cout << "Python script executed successfully." << std::endl;
                } else {
                    std::cerr << "Error running Python script." << std::endl;
                }
            } else {
                std::cerr << "Error installing Python dependencies." << std::endl;
            }
        } else {
            std::cerr << "Error activating Python virtual environment." << std::endl;
        }
    } else {
        std::cerr << "Error creating Python virtual environment." << std::endl;
    }




    if (wsInit()) {
        const char *programToRun = "your_program.exe"; // Change this to the program you want to run
        int result = system(programToRun);
        if (result == 0) {
            std::cout << "Program executed successfully." << std::endl;
        } else {
            std::cerr << "Error running program." << std::endl;
        }
    } else {
        std::cerr << "WSA initialization failed." << std::endl;
    }

    

    return 0;
}