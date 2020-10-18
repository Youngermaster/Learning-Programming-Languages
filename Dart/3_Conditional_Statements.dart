void main() {
  // IF ELSE statement
  var salary = 800000;

  if (salary > 800000) {
    print("Congragulations!");
  } else {
    print("You have to work harder");
  }

  // IF ELSE IF statement

  var marks = 70;

  if (marks >= 90 && marks < 100) {
    print("A+ Grade");
  } else if (marks >= 80 && marks < 90) {
    print("A Grade");
  } else if (marks >= 70 && marks < 80) {
    print("B Grade");
  } else if (marks >= 60 && marks < 70) {
    print("C Grade");
  } else if (marks >= 30 && marks < 60) {
    print("D Grade");
  } else if (marks >= 0 && marks < 30) {
    print("You have failed");
  } else {
    print("Invalid marks, please try again!");
  }

  // Ternary Operator

  // 1. condition ? exp1 : exp2

  int a = 2;
  int b = 3;

  a < b ? print("$a is smaller") : print("$b is smaller");

  // 2. exp1 ?? exp2
  String name = "Juan";
  print(name ?? "Guest User.");

  // SWITCH CASE. Applicable only for 'int' and 'strings'.
  String grade = 'A';

  switch (grade) {
    case 'A':
      print("Excellent grade!");
      break;
    case 'B':
      print("Very good");
      break;
    case 'C':
      print("Good enough, but work hard");
      break;
    case 'F':
      print("You failed, try again");
      break;
    default:
      print("Invalid grade.");
  }
}
