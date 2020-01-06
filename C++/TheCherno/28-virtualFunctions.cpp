#include <iostream>
#include <string>
#define LOG(x) std::cout << x << std::endl

class Entity {
public:
    // ! We add virtual because if we
    // ! want to override this function.
    virtual std::string GetName() { return "Entity"; }
};


class Player : public Entity {
private:
    std::string m_name;
public:
    Player(const std::string &name)
     : m_name(name) {}

    std::string GetName() override { return m_name; }
};


void PrintName(Entity* entity) {
    LOG(entity->GetName());
}

int main() {
    Entity* e = new Entity();
    PrintName(e);
    Player* p = new Player("Juan Manuel");
    PrintName(p);
    return 0;
}
