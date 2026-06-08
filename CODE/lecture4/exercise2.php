<?php
	//create class manusia
	class manusia{
		// declare property
		public $name = "My name is Juan Tan.";
		public $hair = "My hair color is black.";
		
		//method manusia
		function tampilkan_nama(){
			return $this->name." <br/>";
		}
		
		function warna_rambut(){
			return "$this->hair <br/>";
		}
		
	}
	// instansiasi class
	$manusia = new manusia();
	 
	// call and print method "tampilkan_nama"
	echo $manusia->tampilkan_nama();
	 
	// call and print method "warna_rambut"
	echo $manusia->warna_rambut();
?>