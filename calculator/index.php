<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Calculator</title>
    <link rel="styleshet" href="calculator/css/main.css">
</head>
<body>
<!-- get method shows data in url, unlike post method-->
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
    <input type="number" name="num1" placeholder="number 1"> 
        <select name="operator">
            <option value="add">+</option>
            <option value="substract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>

        </select>
        <input type="number" name="num2" placeholder="number 2">
        <button>Calculate</button>
    </form>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Data grabbing
        $num01 = filter_input(INPUT_POST,"num1", FILTER_SANITIZE_NUMBER_FLOAT);
        $num02 = filter_input(INPUT_POST, "num2", FILTER_SANITIZE_NUMBER_FLOAT);
        $operator = htmlspecialchars($_POST["operator"]);

        // Error Handling
        $errors = false;
        if (empty($num01) || empty($num02) || empty($operator)) {
            echo "<p class='clac-error'> Fill in all fields please.</p>";
            $errors = true;
    }
    if (!is_numeric($num01) || !is_numeric($num02)) {
        echo "<p class='clac-error'> Only use numbers please.</p>";
    }
    // Calculate the number is no errors

    if (!$errors) {
        $value = 0;
        switch ($operator) {
            case "add" :
                $value = $num01 + $num02;
                break;
            case "substract" :
                $value = $num01 - $num02;
                break;
            case "multiply" :
                $value = $num01 * $num02;
                break;
            case "divide" :
                $value = $num01 / $num02;
                break;
            default :
                echo "<p class='calc-error'>Something went HORRIBLY WRONG!! </p>";
            }
            echo "<p class='calc-result'>Result = " . $value . "</p>" ;
        }
    }
    ?>
</body>
</html>