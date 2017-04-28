<?php 
	include 'database_handler.php';

	$name = "";
	$author = "";
	$stage = "";
  $votes = 0;
  $rating = 0;
  $downloads = 0;
  $time = "";
  $character = "Mario";
  $description = "";

  $count = $_REQUEST["count"];
  $id = (int)$count;

  // Get id info used in the rest of the script
  // SavesChar
  $savesCharIdQuery = mysqli_query($conn,"SELECT Fk_SavesCharId FROM saves WHERE SaveId = '$id'");
  $savesCharId = mysqli_fetch_assoc($savesCharIdQuery)['Fk_SavesCharId'];
  // Stage
  $stageIdQuery = mysqli_query($conn,"SELECT Fk_StageId FROM saves WHERE SaveId = '$id'");
  $stageId = mysqli_fetch_assoc($stageIdQuery)['Fk_StageId'];
  // Character
  $characterIdQuery = mysqli_query($conn,"SELECT Fk_CharacterId FROM saveschar WHERE SavesCharId = '$savesCharId'");
  $characterId = mysqli_fetch_assoc($characterIdQuery)['Fk_CharacterId'];

  // get bot name, downloads, and time created given id of save
  $nameQuery = mysqli_query($conn,"SELECT SaveName FROM saves WHERE SaveId = '$id'");
  $name = mysqli_fetch_assoc($nameQuery)['SaveName'];
  $downloadsQuery = mysqli_query($conn, "SELECT downloads FROM saves WHERE SaveId = '$id'");
  $downloads = mysqli_fetch_assoc($downloadsQuery)['downloads'];
  $timeQuery = mysqli_query($conn, "SELECT TimeCreated FROM saves WHERE SaveId = '$id'");
  $time = mysqli_fetch_assoc($timeQuery)['TimeCreated'];
  $descriptionIdQuery = mysqli_query($conn,"SELECT Description FROM saves WHERE SaveId = '$id'");
  $description = mysqli_fetch_assoc($descriptionIdQuery)['Description'];

	// get Author of given save's user foreign key id
  $authorQuery = mysqli_query($conn,"SELECT UserName FROM users WHERE UserId = '$id'");
  $author = mysqli_fetch_assoc($authorQuery)['UserName'];

	// Get stage bot was trained on given save's stage foreign key id
	$stageQuery = mysqli_query($conn,"SELECT StageName FROM savesstage WHERE StageId = '$stageId'");
  $stage = mysqli_fetch_assoc($stageQuery)['StageName'];

	// Get rating for bot given savid, uses all votes linked to its id
	$ratingQuery = mysqli_query($conn,"SELECT Rating FROM ratings WHERE Fk_SaveId = '$id'");
	$voteArray = array();
	while($row = mysqli_fetch_array($ratingQuery))
	{
    $voteArray[] = $row['Rating'];
	}
  $votes = count($voteArray);
  $total = 0;
  foreach($voteArray as &$value)
  {
  	$total = $total + $value;
  }
  $rating = 0;
  if($votes>=1)
  {
  	$rating = ($total/$votes);
  }

	// Get the character given save id
	$characterQuery = mysqli_query($conn,"SELECT CharacterName FROM characters WHERE CharacterId = '$characterId'");
  $character = mysqli_fetch_assoc($characterQuery)['CharacterName'];

  echo ($name.','.$author.','.$stage.','.$rating.','.$votes.','.$downloads.','.$time.','.$character.','.$description);
?>