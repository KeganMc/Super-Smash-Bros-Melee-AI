<?php 
	include 'database_handler.php';

	$name = $_REQUEST["name"];
  $rating = $_REQUEST["rating"];

  $saveIdQuery = mysqli_query($conn,"SELECT SaveId FROM saves WHERE SaveName = '$name'");
  $saveId = mysqli_fetch_assoc($saveIdQuery)['SaveId'];

  $rate = "INSERT INTO ratings (Rating, Fk_SaveId, Fk_UserId)
  VALUES ('$rating', '$saveId', '5')";

  if ($conn->query($rate) === TRUE) {
    echo "New record created successfully";
    $last_id = $conn->insert_id;
  } else {
    echo "Error: " . $rate . "<br>" . $conn->error;
  }
?>