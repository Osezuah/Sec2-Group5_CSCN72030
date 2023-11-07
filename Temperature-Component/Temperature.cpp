#include "Temperature.h"
#include <iostream>
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
	}
	else
		cout << "Time should be less than or equals to 60 seconds" << endl;

	return secondsTimer;
}

int Scheduling::setTimerInMinutes(int timedIntervals)
{
	this->minutesTimer = (timedIntervals * 60000); //converts timedIntervals in minutes to milliseconds using 1000

	return minutesTimer;
}

void Heating_Cooling_Unit::setState(bool status)
{
	this->state = status;
}

bool Heating_Cooling_Unit::getState()
{
	return(this->state);
}