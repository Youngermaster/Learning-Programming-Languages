<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Static Variables</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css">
    <script src="main.js"></script>
</head>
<body>
    <?php
        function incrementVariable() {
            static $contador = 0;
            $contador++;
            echo($contador);
        }

        incrementVariable();
        incrementVariable();
        incrementVariable();
    ?>
</body>
</html>