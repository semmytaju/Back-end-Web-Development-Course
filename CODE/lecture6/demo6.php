<?php
	// membuat namespace
	namespace Enemy;

	// membuat trait
	trait Makhluk {
		function printTrait() {
			echo "Nama Trait adalah: ".__TRAIT__;
		}
	}

	class ManusiaSerigala {

		use Makhluk;

	}

	// membuat objek
	$objTest = new ManusiaSerigala();
	$objTest->printTrait();
?>