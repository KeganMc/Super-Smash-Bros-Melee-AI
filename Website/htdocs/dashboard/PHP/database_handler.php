<?php
$servername = "localhost";
$username = "root";
$password = "";
$databasename = "smashdatabase";

// Create connection
$conn = new mysqli($servername, $username, $password, $databasename);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
//echo "Connected successfully"."<br>";
?>