#include "Temperature.h"
#include <iostream>
#include <windows.h>
using namespace std;

Temperature::Temperature() //default constructor
{
	tempDegree = 0;
	timer = 0;
	state = 0;
	EnergyRate = 0;
	Energy_Consumed_In_A_Month_From_Temp[DAYS_IN_A_MONTH - 1] = { 0 };
	Energy_Consumed_In_A_Week_From_Temp[DAYS_IN_A_WEEK - 1] = { 0 };
	Energy_Consumed_In_A_Year_From_Temp[MONTHS_IN_A_YEAR - 1] = { 0 };
}

void Temperature::setTempDegree(int celsiusDegree)
{
	tempDegree = celsiusDegree;
}

int Temperature::getTempDegree()
{
	return this->tempDegree;
}

int Temperature::setPeriodicTimerInSeconds(int timedIntervals)
{
	if (timedIntervals <= 60)
	{
		this->timer = (timedIntervals * 1000); //converts timedIntervals in seconds to milliseconds using 1000
	}
	else
		cout << "Time should be less than or equals to 60 seconds" << endl;

	while (this->state == true)
	{
		Sleep(this->timer);
		this->state = false;
		cout << "I am working" << endl; //gui prompt
	}

	return this->timer;
}

int Temperature::setPeriodicTimerInMinutes(int timedIntervals)
{
	this->timer = (timedIntervals * 60000); //converts timedIntervals in minutes to milliseconds using 1000

	while (this->state == true)
	{
		Sleep(this->timer);
		cout << "I am working" << endl; //gui prompt
		this->state = false;
	}

	return this->timer;
}

void Temperature::setState(bool status)
{
	this->state = status;
}

bool Temperature::getState()
{
	return(this->state);
}