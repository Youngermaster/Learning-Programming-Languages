/*�Hay un n�mero entero que tiene un residuo de 2 cuando se
divide entre 5 y un residuo de 3 cuando se divide entre 6? */

#include <iostream>
using namespace std;

int main()
{
	for (int y = 0; y < 1000; y++)
	{
		if ((y % 5 == 2) && (y % 6 == 3))
		{
			cout << "El numero es : " << y << endl;
		}
	}

	return 0;
}
