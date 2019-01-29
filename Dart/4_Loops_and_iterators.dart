void main () {

  // For LOOP

  for (int x = 0; x < 5; x++)
    print("FOR - Hello $x");

    // FOR..in LOOP
  List planetList = ["Mercury", "Venus", "Earth", "Mars"];
  for (String planet in planetList)
    print(planet);

  // WHILE LOOP

  int y = 0;
  while (y < 5) {
    print("WHILE - Hello $y");
    y++;
  }

  // DO WHILE LOOP

  int z = 0;
  do {
    print("DO WHILE - Hello $z");
    z++;
  } while(z < 5);

  // BREAK KEYWORD
  // Using Labels
  myOuterLoop: for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++) {
      print("$i $j");
      if (i == 2 && j == 2)
        break myOuterLoop;
    }

  // CONTINUE KEYWORD
  // Using Labels
print("Continue\n\n");
  myLoop : for (int i = 0; i < 3; i++)
      for (int j = 0; j < 3; j++){
        if (i == j)
          continue myLoop;
        print("$i $j");
      }
}