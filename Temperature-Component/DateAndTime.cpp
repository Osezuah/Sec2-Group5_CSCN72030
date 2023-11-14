#define _CRT_SECURE_NO_WARNINGS
#include "DateAndTime.h"
#include <iostream>
#include <fstream>
#include <chrono>
#include <ctime>

using namespace std;

void DateAndTime()
{
    // Get the current system time
    auto currentTime = chrono::system_clock::now();

    // Convert the current time to a time_t object
    time_t currentTime_t = chrono::system_clock::to_time_t(currentTime);

    // Convert the time_t object to a tm structure for easier access to date and time components
    tm* localTime = localtime(&currentTime_t);

    // Array of day names for mapping tm_wday values
    const char* dayNames[] = { "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" };

    // Open a file for writing
    ofstream test("test.txt", ios::app);

    if (test.is_open())
    {
    // Display the current date, day of the week, and time
    test << "Current date and time: " << endl;
    test << (localTime->tm_year + 1900) << '-'
        << (localTime->tm_mon + 1) << '-'
        << localTime->tm_mday << ' '
        << dayNames[localTime->tm_wday] << ' '
        << localTime->tm_hour << ':'
        << localTime->tm_min << ':'
        << localTime->tm_sec << std::endl;
    }
    else {
        std::cerr << "Unable to open the file for writing." << std::endl;
        exit(1); // Return an error code
    }
    test.close();
    cout << "Output has been saved to 'test.txt'" << std::endl;
   
}
 
