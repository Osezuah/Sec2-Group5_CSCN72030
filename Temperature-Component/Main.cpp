//Ehi's Temperature Component.
#include "Temperature.h"
#include <iostream>
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

}