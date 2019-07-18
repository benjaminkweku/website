<?php
if(isset($_POST['submit'])){
$name=$_POST['name'];
$email=$_POST['email'];
$msg=$_POST['msg'];

$to='qwekubenjamin17@gmail.com';
$subject='form submission';
$message="Name: ".$name. "\n". "wrote the following:". "\n \n".$msg;
$header="From: ".$email;

if(mail($to,$subject,$message,$header)){
    echo "Sent Successfully! Thanks you. We will contact you shortly!";

}
else{
    echo "Something went wrong!";
}
}
?>