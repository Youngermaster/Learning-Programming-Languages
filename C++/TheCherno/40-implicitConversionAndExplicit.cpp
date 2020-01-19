#include <iostream>
#include <string>

class Entity
{
private:
    std::string m_Name;
    int m_age;

public:
    explicit Entity(const std::string &name)
        : m_Name(name), m_age(-1) {}

    Entity(int age)
        : m_age(age), m_Name("Unknown") {}
};

void printFunction(const Entity &entity)
{
    // Stuff
}

int main(int argc, char const *argv[])
{
    Entity e1 = 22;
    Entity e2("Juan");
    printFunction(44);
    printFunction(Entity("Dímelo pai'"));
    return 0;
}
