<?php
	class Phone_Number {
	  // declare property
	   var $no_hp;
	   var $email;
	}
	  
	// buat objek dari class Phone_Number (instansiasi)
	$andi = new Phone_Number();
	$rudi = new Phone_Number();

	// set property untuk objek andi
	$andi->no_hp="0812345";
	$andi->email="andi@unklab.com";

	// set property untuk objek rudi
	$rudi->no_hp="0854321";
	$rudi->email="rudi@unklab.com";
	  
	// print property untuk objek andi
	echo "Andi Phone Number  & email:"."<br>";
	echo $andi->no_hp; 
	echo "<br />";
	echo $andi->email; 
	echo "<br />";

	// print property untuk objek rudi
	echo "<br><br>"."Rudi Phone Number & email:"."<br>";
	echo $rudi->no_hp; 
	echo "<br />";
	echo $rudi->email; 
	echo "<br />";
?>