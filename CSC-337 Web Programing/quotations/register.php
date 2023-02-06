<!DOCTYPE html>
<!-- Derek Tominaga -->
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="styles.css" />
<title>register.php</title>
</head>
<body>
<h3>Register</h3>
<div id = "registerDiv">
<form method = "post" autocomplete = "off">
<input type = "text" placeholder = "Username" name = "regName" required>
<br>
<input type = "text" placeholder = "Password" name = "regPass" required>
<br><br>
<input type = "submit" formaction = "controller.php" name = "reg" value = "Register" required>
</form>
</div>
</body>
</html>
