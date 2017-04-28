<?php 
	include 'database_handler.php';

	$name = $_REQUEST["name"];
	$author = "default@default.com";
  $votes = 0;
  $rating = 1;
  $downloads = 0;
  $character = $_REQUEST["character"];
  $stage = $_REQUEST["stage"];
  $description = $_REQUEST["description"];

  $charIdQuery = mysqli_query($conn,"SELECT CharacterId FROM characters WHERE CharacterName = '$character'");
  $charId = mysqli_fetch_assoc($charIdQuery)['CharacterId'];

  $stageIdQuery = mysqli_query($conn,"SELECT StageId FROM savesstage WHERE StageName = '$stage'");
  $stageId = mysqli_fetch_assoc($stageIdQuery)['StageId'];

  $char = "INSERT INTO saveschar (Fk_CharacterId, Fk_RelationId, Port)
  VALUES ('$charId', '2', '2')";
  if ($conn->query($char) === TRUE) {
    echo "New record created successfully";
    $last_id = $conn->insert_id;
  } else {
    echo "Error: " . $char . "<br>" . $conn->error;
  }

  $save = "INSERT INTO saves (SaveName, downloads, Description, Fk_UserId, Fk_StageId, Fk_SavesCharId)
  VALUES ('$name', '0', '$description', '9', '$stageId', '$last_id')";
  if ($conn->query($save) === TRUE) {
    echo "New record created successfully";
  } else {
    echo "Error: " . $save . "<br>" . $conn->error;
  }

  header('Location: /dashboard/index.html');
?>