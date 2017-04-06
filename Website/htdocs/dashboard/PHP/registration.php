<?php
include 'database_handler.php';
$email = $_POST['email'];
$password = $_POST['password'];

$sql = "INSERT INTO users (UserName,UserPass) VALUES ('$email','$password')";
$result = mysqli_query($conn,$sql);

header("Location: /dashboard/index.html");
?>