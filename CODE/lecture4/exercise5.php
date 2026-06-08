<?php
	class Fruit {
		// declare property
		public $name;
		public $color;

		// constructor
		public function __construct($name, $color) {
		$this->name = $name;
		$this->color = $color;
		}
		// method
		public function intro() {
		echo "The fruit is {$this->name} and the color is {$this->color}.";
		}
	}

	// Strawberry is inherited from Fruit
	class Strawberry extends Fruit {
	  public function message() {
		echo "Do you like fruit? ";
	  }
	}
	
	$strawberry = new Strawberry("Strawberry", "red");
	$strawberry->message();
	echo "<br/>";
	$strawberry->intro();
?>