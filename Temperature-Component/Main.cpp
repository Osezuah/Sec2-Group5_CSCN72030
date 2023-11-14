//Ehi's Temperature Component.
#include "Temperature.h"
#include "DateAndTime.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(void)
{
	Temperature t1;
	t1.setTempDegree(75);
	cout << "current temp: " << t1.getTempDegree() << endl;
	cout << "Increased temp: " << t1.increaseTemp() << endl;
	cout << "\n\n";
	Temperature t2;
	t2.setTempDegree(22);
	cout << "current temp: " << t2.getTempDegree() << endl;
	cout << "Decreased temp: " << t2.decreaseTemp() << endl;

	//new tests
	DateAndTime(); //has a file
	Files f1; //reads data from that file
	ifstream inputFile = f1.ReadingAFile("test.txt");

	if (inputFile.is_open()) {
		// Read data from the file, for example
		string line;
		while (getline(inputFile, line)) {
			cout << "Read from file: " << line << endl;
		}

		// Close the file (this will happen automatically when the function returns)
		// inputFile.close();
	}

	Scheduling s1;
	s1.setTimerInSeconds(30);
	s1.setTimerInMinutes(15);
	s1.setTimerInHours(1);
}