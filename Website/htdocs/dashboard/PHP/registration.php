<?php
include 'database_handler.php';
$email = $_POST['email'];
$password = $_POST['password'];

$check="SELECT * FROM users WHERE UserName = '$email'";
$rs = mysqli_query($conn,$check);
if($data = mysqli_fetch_array($rs, MYSQLI_NUM)) 
{
    header('Location: /dashboard/HTML/registerAlreadyExists.html');
}
else
{
    $sql = "INSERT INTO users (UserName,UserPass) VALUES ('$email','$password')";
    if (mysqli_query($conn,$sql))
    {
        header('Location: /dashboard/HTML/userRegistered.html');
    }
    else
    {
        header('Location: /dashboard/HTML/registerError.html');
    }
}
?>