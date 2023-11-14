#pragma once
#define DAYS_IN_A_MONTH 31
#define DAYS_IN_A_WEEK 7
#define MONTHS_IN_A_YEAR 12
#define ENERGY_RATE 2.8
#include <fstream>
using namespace std;

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

class Scheduling: public Temperature
{
private:
	int secondsTimer;
	int minutesTimer;
	int hoursTimer;
	int timeFrame;
public:
	Scheduling() :Temperature()
	{
		secondsTimer = 0;
		minutesTimer = 0;
		hoursTimer = 0;
		timeFrame = 0;
		Temperature t1;
		t1.setTempDegree(0);
	};

	int setTimerInSeconds(int);
	int setTimerInMinutes(int);
	int setTimerInHours(int);
	void setTimerInHours(int, int); //for energy consumption
	void setTimerInSeconds(int, int);//for energy consumption
	void setTimerInMinutes(int, int); //for energy consumption
	void setTimeFrame(int, int); //for energy consumption
	int setTimeFrameInSeconds(int);
	int setTimeFrameInMinutes(int);
	int setTimeFrameInHours(int);

};

class EnergyConsumption: public Scheduling
{
private:
	float Energy_Consumed_In_A_Week_From_Temp[DAYS_IN_A_WEEK];
	float Energy_Consumed_In_A_Month_From_Temp[DAYS_IN_A_MONTH];
	float Energy_Consumed_In_A_Year_From_Temp[MONTHS_IN_A_YEAR];
public:
	EnergyConsumption() : Scheduling()
	{
		Energy_Consumed_In_A_Week_From_Temp[DAYS_IN_A_WEEK - 1] = { 0 };
		Energy_Consumed_In_A_Month_From_Temp[DAYS_IN_A_MONTH - 1] = { 0 };
		Energy_Consumed_In_A_Year_From_Temp[MONTHS_IN_A_YEAR - 1] = { 0 };
		Scheduling s1;
		s1.setTimerInMinutes(0, 0);
		s1.setTimerInSeconds(0, 0);
		s1.setTimerInHours(0, 0);
		s1.setTimeFrame(0, 0);
	};
	float calculateAverageTimeSpent();
	float calculateAverageTempDegree();
	float* displayWeeklyConsumption();
	float* displayMonthlyConsumption();
	float* displayYearlyConsumption();
};

class Files
{
public:
	ofstream AppendingToFile(const string&);
	ifstream ReadingAFile(const string&);
};
