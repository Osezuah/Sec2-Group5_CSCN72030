#pragma once
#define DAYS_IN_A_MONTH 31
#define DAYS_IN_A_WEEK 7
#define MONTHS_IN_A_YEAR 12
class Temperature
{
	int tempDegree;
	bool state;
	int timer;
	float Energy_Consumed_In_A_Week_From_Temp[DAYS_IN_A_WEEK];
	float Energy_Consumed_In_A_Month_From_Temp[DAYS_IN_A_MONTH];
	float Energy_Consumed_In_A_Year_From_Temp[MONTHS_IN_A_YEAR];
	float EnergyRate;
	//my other perspective is adding weather API
	//utilizing decision making algorothm that makes suggestion on the setting the
	//heaters and coolers should be 
	//remember you have a file from the sensor class 
public:
	Temperature();
	void setTempDegree(int celsiusDegree);
	int getTempDegree();
	int setPeriodicTimerInSeconds(int);
	int setPeriodicTimerInMinutes(int);
	void setState(bool);
	bool getState();
};

