<?php
$user_id = $_POST['user_id'];
$command = '/usr/bin/python initial.py '.$user_id;
$output = shell_exec($command);
#$data = array();
#$data['sucess'] = true;
#$data['output'] = $output;
echo json_encode($output);
?>
