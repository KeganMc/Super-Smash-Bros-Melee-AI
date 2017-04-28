<?php 
	include 'database_handler.php';

  $name = $_REQUEST["botName"];
  
  $conn->query("UPDATE saves SET downloads = downloads + 1 WHERE SaveName = '$name'");
?>