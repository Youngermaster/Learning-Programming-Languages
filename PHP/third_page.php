<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css">
    <script src="main.js"></script>
</head>
<body>
    <?php
          function FunctionName()
          {
              echo "This is the message inside the function block <br>";
          }  
    ?>
    <?php
        
        include ("function.php"); // Execute even if it fails.
        //require ("function.php"); Execute until here if it fails.
        echo "<h2>Execution flow</h2><br>";
        echo "This is the first message <br>";
        FunctionName();
        echo "This is the second message <br>";
        NewFunctionName();
    ?>
    <?php
        echo "<hr><h2>Example of ambits variables</h2><br>";
        $name = "Juan";
        function giveName()
        {
            global $name;
            $name = "Mi name is: $name";
        }

        giveName();
        echo $name;

    ?>
</body>
</html>