<?php
$user_id = $_POST['user_id'];
$genre_wt = $_POST['genre_wt'];
$author_wt = $_POST['author_wt'];
$ratings_wt = $_POST['ratings_wt'];

// $user_id = 1;
// $genre_wt = 2000;
// $author_wt = 30000;
// $ratings_wt = 4000;

$command = '/Users/aditya16.narula/anaconda/bin/python hybrid.py '.$user_id.' '.$genre_wt.' '.$author_wt.' '.$ratings_wt.' 2>&1';
//$command = '/Users/aditya16.narula/anaconda/bin/python authorbasedrecommendation.py '.$user_id.' 2>&1';
//echo $command;

$output = shell_exec($command);
echo json_encode($output);
?>
