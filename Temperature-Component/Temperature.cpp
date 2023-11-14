#include "Temperature.h"
#include <iostream>
#include <fstream>
#include <windows.h>
using namespace std;

Temperature::Temperature() //default constructor
{
	tempDegree = 0;
}

void Temperature::setTempDegree(int celsiusDegree)
{
	this->tempDegree = celsiusDegree;
}

int Temperature::getTempDegree()
{
	return this->tempDegree;
}

int Temperature::increaseTemp() //GUI
{
	//this needs GUI
	int* pTemp = &(this->tempDegree);
	(*pTemp)++;
	if (*pTemp <= 100)
	{
		true;
	}
	else
	{
		cout << "It should not go above 100C" << endl;
		exit(1);
	}
	
	return this->tempDegree;
}

int Temperature::decreaseTemp() //GUI
{
	//this needs GUI
	int* pTemp = &(this->tempDegree);
	(*pTemp)--;
	if (*pTemp > 20)
	{
		true;
	}
	else
	{
		cout << "It should not go below 20C" << endl;
		exit(1);
	}

	return this->tempDegree;
}

int Scheduling::setTimerInSeconds(int timedIntervals)
{
	if (timedIntervals <= 60)
	{
		this->secondsTimer = (timedIntervals * 1000); //converts timedIntervals in seconds to milliseconds using 1000
		cout << timedIntervals << "sec set successfully" << endl;
	}
	else
		cout << "Time should be less than or equals to 60 seconds" << endl;

	return this->secondsTimer;
}

int Scheduling::setTimerInMinutes(int timedIntervals)
{
	this->minutesTimer = (timedIntervals * 60000); //converts timedIntervals in minutes to milliseconds using 1000
	cout << timedIntervals << "min set successfully" << endl;
	return this->minutesTimer;
}

int Scheduling::setTimerInHours(int timedIntervals)
{
	this->hoursTimer = (timedIntervals * 3600000); //converts timedIntervals in minutes to milliseconds using 1000
	cout << timedIntervals << "hr set successfully" << endl;
	return this->hoursTimer;
}

void Scheduling::setTimerInHours(int a, int b) //for EnergyConsumption Class
{
	this->hoursTimer = (a * b);
}

void Scheduling::setTimerInSeconds(int a, int b) //for EnergyConsumption Class
{
	this->secondsTimer = (a * b);
}

void Scheduling::setTimerInMinutes(int a, int b) //for EnergyConsumption Class
{
	this->minutesTimer = (a * b);
}

void Scheduling::setTimeFrame(int Time1, int Time2) //for energy consumption class
{
	this->timeFrame = (Time1 * Time2);
}

int Scheduling::setTimeFrameInSeconds(int timeframe)
{
	Scheduling timing;
	this->timeFrame = timing.setTimerInSeconds(timeframe);

	return this->timeFrame;
}

int Scheduling::setTimeFrameInMinutes(int timeframe)
{
	Scheduling timing;
	this->timeFrame = timing.setTimerInMinutes(timeframe);

	return this->timeFrame;
}

int Scheduling::setTimeFrameInHours(int timeframe)
{
	Scheduling timing;
	this->timeFrame = timing.setTimerInHours(timeframe);

	return this->timeFrame;
}

void Heating_Cooling_Unit::setState(bool status)
{
	this->state = status;
}

bool Heating_Cooling_Unit::getState()
{
	return(this->state);
}

float EnergyConsumption::calculateAverageTimeSpent()
{
	return 0;
}

float EnergyConsumption::calculateAverageTempDegree()
{
	return 0;
}

float* EnergyConsumption::displayMonthlyConsumption()
{
	return 0;
}

float* EnergyConsumption::displayWeeklyConsumption()
{
	return 0;
}

float* EnergyConsumption::displayYearlyConsumption()
{
	return 0;
}

ofstream Files::AppendingToFile(const string& filename)
{
	ofstream outputFile(filename, ios::app);
	if (!outputFile.is_open()) {
		cout << "Error opening file for writing: " << filename << endl;
		exit(1);
	}
	return outputFile;
}

ifstream Files::ReadingAFile(const string& filename)
{
	ifstream inputFile(filename);
	if (!inputFile.is_open()) {
		cout << "Error opening file for reading: " << filename << endl;
		exit(1);
	}
	return inputFile;
}