<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP Get Class Method Name</title>
</head>
<body>

<?php
	class Sample
	{
		public function myMethod(){
			echo __METHOD__;
		}
	}
	// Create object and call function
	$obj = new Sample();
	$obj->myMethod();
?>

</body>
</html>