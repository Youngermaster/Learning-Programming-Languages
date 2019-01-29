void main(){

  // Numbers: Int
  int score = 10;
  var age = 17;   // It is inferred as integer automatically by compiler.
  int hexValue = 0xEADEF;

  // Numbers: Double
  double percentage = 55.4;
  var percent = 99.9;   // It is inferred as double automatically by compiler.
  double exponents = 1.5e5;

  // String
  String name = "Juan";
  var company = "YECO"; // It is inferred as string automatically by compiler.

  // Boolean
  bool isAlive = true;
  var isDead = false; // It is inferred as boolean automatically by compiler.

  print(hexValue);
  print(exponents);

  // Literals
  true;
  int x = 2;
  "John";
  5;

  // Various ways to define String literals in Dart.
  String s1 = 'Single';
  String s2 = "Double";
  String s3 = 'It\'s easy';
  String s4 = "It's easy";

  String s5 = "This going to be a very long String."
      " This is just a sample String demo in Dart programming language";

  // String interpolation : Use ["My name is $name"] instead of ["My name is " + name]

  String name2 = "Juan";

  print("My name is $name");
  print("The number of the characters in my name is ${name.length}");

  int l = 10;
  int h = 20;

  print("The sum of $l + $h is: ${l + h}");

  // Final
  final cityName = "Medellín";
  final String countryName = "Colombia";  // It is not necessary write the data type

  // Constants
  const PI = 3.14;
  const double gravity = 9.8; // It is not necessary write the data type

}

class Circle {
  final color = "Red";
  static const PI = 3.14; // Only static fields can be declared as constant in a class.
}