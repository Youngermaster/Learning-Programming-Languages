#include <iostream>
#include <string>

struct Vector2
{
    float x, y;
    int test;

    Vector2(float x, float y)
        : x(x), y(y), test(-1) {}

    Vector2(int test)
        : test(test), x(-1), y(-1) {}

    Vector2 Add(const Vector2 &other) const
    {
        return Vector2(x + other.x, y + other.y);
    }

    Vector2 Multiply(const Vector2 &other) const
    {
        return Vector2(x * other.x, y * other.y);
    }

    Vector2 operator+(const Vector2 &other) const
    {
        return Add(other);
    }

    Vector2 operator*(const Vector2 &other) const
    {
        return Multiply(other);
    }

    Vector2 operator^(const Vector2 &other) const
    {
        return Vector2(21);
    }
};

std::ostream &operator<<(std::ostream &stream, const Vector2 &vector)
{
    stream << vector.x << ", " << vector.y << " -> " << vector.test;
    return stream;
}

int main(int argc, char const *argv[])
{
    Vector2 position(4.0f, 4.0f);
    Vector2 speed(0.5f, 1.5f);
    Vector2 force(1.1f, 1.1f);

    Vector2 result1 = position.Add(speed.Multiply(force));
    Vector2 result2 = position + speed * force;

    std::cout << result2 << std::endl;
    Vector2 f = result2 ^ 21;
    std::cout << f << std::endl;

    return 0;
}
