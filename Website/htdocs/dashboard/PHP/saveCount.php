<?php 
  include 'database_handler.php';
  // Create table name variables for easy access
  $save = "saves";

  $savesArray = array();

  //--------------------------------------------------------------------------
  //  Query database for data
  //--------------------------------------------------------------------------

  $saves = mysqli_query($conn,"SELECT SaveId FROM $save");

  while($row = mysqli_fetch_array($saves))
	{
    $savesArray[] = $row['SaveId'];
	}

	//$stringy = implode("|",$savesArray);

  echo count($savesArray);
?>