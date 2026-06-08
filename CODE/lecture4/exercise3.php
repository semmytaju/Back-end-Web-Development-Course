<html>
	<body>
		<?php
			class Fruit {
				// Properties
				public $name;
				public $color;

				// Method set
				function set_name($name) {
					$this->name = $name;
				}
				
				// Method get
				function get_name() {
					return $this->name;
				}
			}
			
			// instansiasi class
			$apple = new Fruit();
			$banana = new Fruit();
			
			// set value
			$apple->set_name('Apple');
			$banana->set_name('Banana');
			
			// get value
			echo "Fruit #1 Name: ".$apple->get_name();
			echo "<br>";
			echo "Fruit #2 Name: ".$banana->get_name();
		?>
	</body>
</html>