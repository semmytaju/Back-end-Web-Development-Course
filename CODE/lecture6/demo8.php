<?php
	// Create namespace
	namespace MyNamespace;
	
	// Create class
	class MyClass
	{
		// Ceate a function
		public function getNamespace(){
			return __NAMESPACE__;
		}
	}
	
	// Create object and call function
	$obj = new MyClass();
	echo $obj->getNamespace();
?>