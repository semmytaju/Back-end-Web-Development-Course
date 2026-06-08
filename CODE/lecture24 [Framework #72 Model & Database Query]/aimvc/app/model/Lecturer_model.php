<?php  

class Lecturer_model{
	private $db;

	public function __construct(){
		// create object from database class
		$this->db = new Database;

		// check status
		if($this->db == false){
			echo "<script>console.log('Connection failed.' );</script>";
		}else{
			echo "<script>console.log('Connected successfully.' );</script>";
		}
		
	}

	public function getAllDataLecturer(){
		$arr_data = $this->db->query("select * from tbl_lecturer;");
		$this->db->db_close(); // Close database connection
		return $arr_data;
	}
}
?>