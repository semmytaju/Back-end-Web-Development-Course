<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP Get Current Class Name</title>
</head>
<body>

<?php
	class MyClass{
		public function getClassName(){
			return __CLASS__;
		}
	}
	// Create object and call function
	$obj = new MyClass();
	echo $obj->getClassName();
?>

</body>
</html>