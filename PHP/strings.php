<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Strings</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css">
    <script src="main.js"></script>
    <style>
        .resaltar {
            color: #F00;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <?php
      echo "<p class='resaltar'>This is a example</p>";
      $variable1 = "House";
      $variable2 = "house";
      
      if (strcmp($variable1, $variable2)) {
          echo "The word is equal";
      } if (strcasecmp($variable1, $variable2)) {
          echo "All their characters are equals";
      } else {
          echo "The words are innequal";
      }

    ?>
</body>
</html>