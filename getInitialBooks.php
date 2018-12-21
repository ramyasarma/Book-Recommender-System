<?php
$user_id = $_POST['user_id'];
$command = '/Users/aditya16.narula/anaconda/bin/python initial.py '.$user_id.' 2>&1';
$output = shell_exec($command);
echo json_encode($output);
?>
