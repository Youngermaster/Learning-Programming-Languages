void main() {
  var dog = Dog();
  dog.color = "Black";
  dog.breed = "Labrador";
  dog.bark();
  dog.eat();

  var cat = Cat();
  cat.color = "White";
  cat.age = 2;
  cat.meow();
  cat.eat();

  var animal = Animal();
  animal.color = "Brown";
  animal.eat();
}

// Inheritance
class Animal {
  String color;

  void eat() {
    print("Animal is eating eat");
  }
}

class Dog extends Animal {
  String breed;

  void bark() {
    print("Bark!");
  }

  // Dart method Overriding - Polymorphism
  void eat() {
    print("Dog is eating");
  }
}

class Cat extends Animal {
  int age;

  void meow() {
    print("Meow");
  }
}

// Dart constructor
