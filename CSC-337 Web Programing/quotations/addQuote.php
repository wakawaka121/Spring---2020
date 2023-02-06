<!DOCTYPE html>
<!-- Derek Tominaga -->
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" type="text/css" href="styles.css" />
<title>addQuote.php</title>
</head>
<body>
<h3>Add a Quote</h3>
<div id = "addQuoteDiv">
<form method = "post" autocomplete = "off" action = "controller.php">
<textarea name = "newQuote" placeholder = "Enter new quote" rows = "6" cols = "72" required></textarea>
<br>
<input type = "text" name = "author" placeholder = "Author" required>
<br><br>
<input type = "submit" name="entrySubmit" value = "Add Quote" required>
</form>
</div>
</body>
</html>
