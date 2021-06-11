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
        cout << *myInt << endl; // * I should get a 10
	// ! The pointer value should be deleted after this scope
    }
    // ! I won't get a 10, I'll get a default value (0), due to the deletion of the pointer
    cout << *p << endl; 
    return 0;
}
