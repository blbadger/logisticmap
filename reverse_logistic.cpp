#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

vector<double> reverse_logistic(vector<double> values, double r, int steps){
	if (steps == 0){
		return values;
	}
	vector<double> new_values {};
	for (int i=0; i < values.size(); i++){
		double current_value = values[i];
		
		if ((r*r-4*r*current_value) >= 0){
			double numerator = r + sqrt(r*r - 4*r*current_value);
			double next_value = numerator / (2*r);
			if(0 < next_value and 1 > next_value){
				new_values.push_back(next_value);
				}
			
			numerator = r - sqrt(r*r - 4*r*current_value);
			next_value = numerator / (2*r);
			if(0 < next_value and 1 > next_value){
				new_values.push_back(next_value);
				}
			}
			
		}
	return reverse_logistic(new_values, r, steps-1);
}


int main() {
	vector<double> values {0.5};
	double r = 3.9;
	int steps = 3;
	vector<double> val = reverse_logistic(values, r, steps);
	cout << val.size() << endl;
	for (int i = 0; i < val.size(); i++){
		cout << std::setprecision (17) << val[i] << ',' << ' ';
	}
	return 0;
}



