void main() {

  onClause();
  catchClause();
  catchAndStackTraceClause();
  finallyClause();

  // There are to ways with custom exceptions.
  // First way.
  try {
    depositMoney(-220);
  } on DepositException {
    print(new DepositException().errorMessage());
  }

  // Second way
  try {
    depositMoney(-220);
  } catch(e) {
    print(e.errorMessage());
  }
}

/**
 * Perform exception handling
 */

// ON CLAUSE
// Case 1: When you know the exception to be thrown, use ON Clause.

onClause() {
  try {
    int result = 12 ~/ 0;
    print("The result is $result");
  } on IntegerDivisionByZeroException {
    print("Cannot divide by zero");
  }
}

// CATCH CLAUSE
// Case 2: When you do not know the exception, use Catch Clause.

catchClause() {
  try {
    int result = 12 ~/ 0;
    print("The result is $result");
  } catch (e) {
    print("The exception thrown is: $e");
  }
}

// CATCH CLAUSE
// Case 3: Using STACK TRACE to know the events occurred before exception was thrown.

catchAndStackTraceClause() {
  try {
    int result = 12 ~/ 0;
    print("The result is $result");
  } catch (e, s) {
    print("The exception thrown is: $e");
    print("STACK TRACE\n $s");
  }
}

// FINALLY CLAUSE
// Case 4: Whether there is an Exception or not, Finally clause is always executed.

finallyClause() {
  try {
    int result = 12 ~/ 0;
    print("The result is $result");
  } catch (e) {
    print("The exception thrown is: $e");
  } finally {
    print("This is a Finally Clause and is always executed.");
  }
}

/**
 * Custom exception handling
 */

// CASE 5: Custom Exception.
class DepositException implements Exception {
  String errorMessage() {
    return "You cannot enter amount less than zero";
  }
}

void depositMoney(int amount) {
  if (amount < 0) {
    throw new DepositException();
  }
}