abstract class Animal {}

abstract class Bird extends Animal {}

abstract class Fish extends Animal {}

abstract class Mammal extends Animal {}

// Mixins
abstract class Flyer {
  void fly() => 'I can Fly';
}

abstract class Walker {
  void walk() => 'I can Walk';
}

abstract class Swimmer {
  void swim() => 'I can swim';
}

class Cat extends Mammal with Walker {}

class Dolphin extends Mammal with Swimmer {}

class Bat extends Mammal with Walker, Flyer {}

class Dove extends Bird with Flyer {}

class Duck extends Bird with Flyer, Walker, Swimmer {}

class Shark extends Fish with Swimmer {}

class FlyingFish extends Fish with Swimmer, Flyer {}

void main() {
  final duck = Duck();
  duck.walk();
  duck.swim();
  duck.fly();

  final flyingFish = FlyingFish();
  flyingFish.swim();
  flyingFish.fly();
}
