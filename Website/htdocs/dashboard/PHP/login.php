<?php
include 'database_handler.php';
$email = $_POST['email'];
$password = $_POST['password'];

$check="SELECT * FROM users WHERE UserName = '$email'";
$pass="SELECT * FROM users WHERE UserPass = '$password'";
$rs = mysqli_query($conn,$check);
$rs2 = mysqli_query($conn,$pass);
if($data = mysqli_fetch_array($rs, MYSQLI_NUM) && $data = mysqli_fetch_array($rs2, MYSQLI_NUM)) 
{
    header('Location: /dashboard/loginHome.html');
}
else
{
	header('Location: /dashboard/loginError.html');
}
?>