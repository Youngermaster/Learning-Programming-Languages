#include <iostream>
#include <string>

#define LOG(x) std::cout << x << std::endl;

using String = std::string;

class Entity
{
private:
    String m_name;

public:
    Entity() : m_name("Unknown") {}
    Entity(const String &name) : m_name(name) {}
    const String &GetName() const { return m_name; }
};

int main(int argc, char const *argv[])
{
    Entity *e1;
    // * When this entity comes to the end of the scope
    // * it will die.
    {
        Entity stackEntity("Juan");
        e1 = &stackEntity;
        LOG(stackEntity.GetName());
    }
    LOG(e1->GetName());
    // ! If I try -> LOG(stackEntity.GetName());
    // ! it will fail.

    // * Using NEW keyword this memory gonna last
    // * until we delete it.
    Entity *e2;
    {
        Entity *heapEntity = new Entity("Manuel");
        e2 = heapEntity;
        LOG((*heapEntity).GetName());
    }
    LOG(e2->GetName());
    delete e2;

    return 0;
}
