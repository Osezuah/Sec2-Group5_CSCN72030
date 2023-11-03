//Ehi's Temperature Component.
#include "Temperature.h"
#include <iostream>
using namespace std;

int main(void)
{
	Temperature Device1;
	//core functionality
	Device1.setState(true);
	Device1.setTempDegree(50);
	cout << "Device1 has been set a temp of " << Device1.getTempDegree() << "C" << endl; //gui prompt
	
	//#1 perspective
	cout << "Enter the time in seconds for device1 to run continuously" << endl; //gui prompt
	int timeInSeconds;
	cin >> timeInSeconds;
	Device1.setPeriodicTimerInSeconds(timeInSeconds);//make the gui loop this continuously until the device is forced shutdown
}