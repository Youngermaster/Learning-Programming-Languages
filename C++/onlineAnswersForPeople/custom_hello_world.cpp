#include <iostream>
using namespace std;

int main() {
	const char ARR_SIZE{8};
	char hello[ARR_SIZE] = "Hello, ";
	char world[ARR_SIZE] = "World!";
	cout << hello << world << endl;
}
