#include <iostream>
#include <string>
#define LOG(x) std::cout << x << std::endl

class Printable {
public:
    virtual std::string GetClassName() = 0;
};

class Entity : public Printable {
public:
    virtual std::string GetName() { return "Entity"; }
    std::string GetClassName() override { return "Entity"; }
};


class Player : public Entity {
private:
    std::string m_name;
public:
    Player(const std::string &name)
     : m_name(name) {}

    std::string GetName() override { return m_name; }
    std::string GetClassName() override { return "Player"; }
};

class A : public Printable {
public:
    std::string GetClassName() override { return "A"; }
};

void PrintName(Entity* entity) {
    LOG(entity->GetName());
}

void Print(Printable* obj) {
    LOG(obj->GetClassName());
}

int main() {
    Entity* e = new Entity();
    Player* p = new Player("Juan Manuel");
    Print(e);
    Print(p);
    Print(new A());
    return 0;
}
