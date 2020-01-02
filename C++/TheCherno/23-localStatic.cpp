#include <iostream>

#define LOG(x) std::cout << x << std::endl

void function() {
    int iterator = 0;
    iterator++;
    LOG(iterator);
}

void s_function() {
    static int iterator = 0;
    iterator++;
    LOG(iterator);
}

class Singleton
{
private:
    /* data */
public:
  static Singleton& Get() {
      static Singleton instance;
      return instance;
  }

  void Hello() {LOG(&Get());}
};


int main(int argc, char const *argv[])
{
    function();
    function();
    function();
    function();
    function();
    LOG("=========================");
    s_function();
    s_function();
    s_function();
    s_function();
    s_function();
    LOG("=========================");
    Singleton::Get().Hello();
    Singleton::Get().Hello();
    Singleton::Get().Hello();
    return 0;
}
