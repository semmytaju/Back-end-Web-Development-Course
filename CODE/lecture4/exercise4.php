<html>
<body>
	<?php
		class Fruit {
		  // properties
		  var $name;
		  var $color;

		  // methods [PHP OOP - Constructor]
		  function __construct($name, $color) {
			$this->name = $name;
			$this->color = $color; 
		  }
		  
		  // methods [PHP OOP - Destructor]
		  function __destruct() {
			echo "The fruit is {$this->name} and the color is {$this->color}."; 
		  }
		}
		
		// instansiasi class
		$apple = new Fruit("Apple", "red");
	?>
</body>
</html>