#pragma once
#define DAYS_IN_A_MONTH 31
#define DAYS_IN_A_WEEK 7
#define MONTHS_IN_A_YEAR 12
#define ENERGY_RATE 22
#include <fstream>
class Temperature
{
	int tempDegree;
public:
	Temperature();
	void setTempDegree(int celsiusDegree);
	int getTempDegree();
	int increaseTemp();
	int decreaseTemp();
};

class Heating_Cooling_Unit:public Temperature
{
private:
	bool state;
public:
	Heating_Cooling_Unit() :Temperature() 
	{
		state = 0;
		Temperature t1;
		t1.setTempDegree(0);
	};
	void setState(bool);
	bool getState();
};

class Scheduling
{
private:
	int secondsTimer;
	int minutesTimer;
	int timeFrame;
public:
	int setTimerInSeconds(int);
	int setTimerInMinutes(int);
	void setTimeFrame(int);
	int getTimeFrame();
   //ofstream savesTimesToFile();
};

class EnergyConsumption
{
private:
	float Energy_Consumed_In_A_Week_From_Temp[DAYS_IN_A_WEEK];
	float Energy_Consumed_In_A_Month_From_Temp[DAYS_IN_A_MONTH];
	float Energy_Consumed_In_A_Year_From_Temp[MONTHS_IN_A_YEAR];
public:
	float calculateAverageTimeSpent();
	float calculateAverageTempDegree();
	float AverageRate();
	float* displayWeeklyConsumption();
	float* displayMonthlyConsumption();
	float* displayYearlyConsumption();
};


