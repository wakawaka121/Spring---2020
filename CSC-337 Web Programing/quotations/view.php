<!DOCTYPE html>
<!-- Derek Tominaga -->
<html>
<head>
<link rel="stylesheet" type="text/css" href="styles.css" />
<meta charset="UTF-8">
<title>view.php</title>
</head>
<body onload = 'displayAll()'>
<h1>Quotation Service</h1>
<button onclick = 'location.href = "addQuote.php"'>Add Quote</button>
<div id = "quoteDiv"></div>
<script>
function displayAll(){
	var quoteDiv = document.getElementById('quoteDiv');
	var ajax = new XMLHttpRequest();
	var testStr = '';
	ajax.open("GET", "controller.php?status=display");
	ajax.send();
	ajax.onreadystatechange = function(){
			console.log("State: " + ajax.readyState);
			if(ajax.readyState == 4 && ajax.status == 200){
				var quoteString = ajax.responseText;
				quoteDiv.innerHTML = quoteString;
			}
		};	
}
</script>
</body>
</html>
