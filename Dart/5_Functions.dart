void main() {
  findRectanglePerimeter(5, 10);
  print("The area is ${findRectangleArea(2, 3)}");

  printCities("New York", "Sydney", "Cartagena");
  printCountries("USA");
  
  findVolume(50, breadth: 20, height: 4);
  findVolume(50, height: 4, breadth: 20);

  findVolume2(3, breadth: 10);
}

// SHORT HAND SYNTAX : =>
findRectanglePerimeter (int length, int breadth) => print("The perimeter is: ${2 * (length + breadth)}");

findRectangleArea (int length, int breadth) => length * breadth;

// REQUIRED PARAMETERS

printCities(String name1, String name2, String name3) {
  print("Name 1 is: $name1");
  print("Name 2 is: $name2");
  print("Name 3 is: $name3");
}

// OPTIONAL POSITIONAL PARAMETERS

printCountries(String name1, [String name2, String name3]) {
  print("Name 1 is: $name1");
  print("Name 2 is: $name2");
  print("Name 3 is: $name3");
}

// OPTIONAL NAMED PARAMETERS

findVolume(int length, {int breadth, int height}) {
  print("Length is: $length");
  print("Breadth is: $breadth");
  print("Height is: $height");

  print("The volume is: ${length * breadth * height}");
}

// OPTIONAL DEFAULT PARAMETERS

findVolume2(int length, {int breadth = 5, int height = 10}) {
  print("Length is: $length");
  print("Breadth is: $breadth");
  print("Height is: $height");

  print("The volume is: ${length * breadth * height}");
}