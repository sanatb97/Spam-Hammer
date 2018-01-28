<?php
	 if($_SERVER["REQUEST_METHOD"] == "POST") {
	 	if($_POST["data"] == "ham") {
			echo file_get_contents("C:\\Users\\sanat\\Documents\\I_Hack 2018\\results\\hamMails.txt");
		} else if($_POST["data"] == "spam"){
			echo file_get_contents("C:\\Users\\sanat\\Documents\\I_Hack 2018\\results\\spamMails.txt");
			
		}

	 	}
?>