<?php
	// Create a class
	class App{
		// PHP Constructor
		public function __construct(){

			// display structured information (type and value)
			$url = $this -> parseURL();
			var_dump($url);

		}

		public function parseURL(){
			if(isset($_GET['url'])){
				// Remove end slash
				$url = rtrim($_GET['url'], '/');

				// Remove/filter special character
				$url = filter_var($url, FILTER_SANITIZE_URL);

				// Convert to array
				$url = explode('/',  $url);

				return $url;
			}
		}
	}
?>
