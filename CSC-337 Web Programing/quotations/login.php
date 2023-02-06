<!DOCTYPE html>
<!-- Derek Tominaga -->
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="styles.css" />
<title>login.php</title>
</head>
<body>
<h3>Login</h3>
<div id = "loginDiv">
<form method = "post" autocomplete = "off">
<input type = "text" placeholder = "Username" name = "accName" required>
<br>
<input type = "text" placeholder = "Password" name = "accPass" required>
<br><br>
<input type = "submit" formaction = "controller.php" name= "login" value = "Login" required>
</form>
</div>
</body>
</html>
