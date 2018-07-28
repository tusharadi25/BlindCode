<?php
include 'connect.php';
mysqli_select_db($conn,'id4238412_blindcode');
$name = $_POST['name'];
$college = $_POST['college'];
$contact = $_POST['contact'];
$time=$_POST['timecomplited'];
$error=$_POST['error'];


$sql="Insert into Intra (name, college,contact,Timecomplited,error) values ('$name','$college','$contact','$time','$error')";
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
}
echo (' '.$name);
?>