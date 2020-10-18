void main() {
  // Default getter and setter.
  var student = Student();
  student.name = "Juan"; // Calling Default setter
  print(student.name); // Calling Default getter

  // Custom setter and getter
  student.percentage = 438.0; // Calling custom setter
  print(student.percentage); // Calling custom getter
}

class Student {
  String name; // Instance variable
  double _percent; // Private Instance variable

  set percentage(double markSecure) =>
      _percent = (markSecure / 5); // Instance variable with custom setter

  // Instance variable with custom getter
  get percentage => _percent;
}
