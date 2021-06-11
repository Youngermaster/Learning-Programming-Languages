#include <iostream>

using namespace std;

class MyInt {
   private:
    int *data;

   public:
    MyInt(int *p = nullptr) { data = p; };

    ~MyInt() { delete data; };
    int &operator*() { return *data; };
};

int main(int argc, char const *argv[]) {
    int *p = new int(10);
	{
    MyInt myInt = MyInt(p);
    cout << *myInt << endl;
	}
	cout << *p << endl;
    return 0;
}
