<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP Get Current Function Name</title>
</head>
<body>

<?php
	function myFunction(){
		echo  "The function name is - " . __FUNCTION__;
	}
	
	// Call a function
	myFunction();
?>

</body>
</html>