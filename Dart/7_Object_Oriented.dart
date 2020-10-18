void main() {
  /**
   *  DEFAULT CONSTRUCTOR.
  var student = Student(); // The keyword NEW in Dart is optional.
  student.id = 23;
  student.name = "Juan";
   */
  var student = Student(123, "Juan");
  print("${student.id} and ${student.name}");

  var student1 = Student.myCustomConstructor(23);
  print("${student1.age}");
}

class Student {
  int id;
  int age;
  String name;

  /**
   * DEFAULT CONSTRUCTOR
  Student() {

  }
  */

  /**
   * PARAMETERIZED CONSTRUCTOR
   */
  Student(this.id, this.name);

  /**
   * NAMED CONSTRUCTOR OR CUSTOM CONSTRUCTOR
   */

  Student.myCustomConstructor(this.age);

  study() => print("$name is now studying");

  sleep() => print("$name is now sleeping");
}
