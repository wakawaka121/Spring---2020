<?php
//Derek Tominaga
include 'model.php';
$theDBA = new DatabaseAdapter();
if (isset($_POST['entrySubmit'])){
    $quote = htmlspecialchars($_POST['newQuote']);
    //$quote = addslashes($quote);
    $author = htmlspecialchars($_POST['author']);
    quoteEntry($theDBA,$quote,$author);
}
if (isset($_POST['plus'])){
    $id = $_POST['id'];
    $theDBA->ratingUp($id);
    header("Location:view.php");
}
if (isset($_POST['minus'])){
    $id = $_POST['id'];
    $theDBA->ratingDown($id);
    header("Location:view.php");
}
if (isset($_POST['delete'])){
    $id = $_POST['id'];
    $theDBA->deleteEntry($id);
    header("Location:view.php");
}
if (isset($_GET['status'])){
    quoteString($theDBA);
}

function quoteString($theDBA){
    $quoteArray = $theDBA->getAllQuotations();
    $quoteString = "";
    if (count($quoteArray) === 0){
        echo "<br>No quotes found";
    }else{
    for ($i = 0; $i < count($quoteArray); $i++){
        $quoteString .= '<form method="post" class = "quotes" action = "controller.php">"'.$quoteArray[$i]['quote'].'"<br><br>';
        $quoteString .= '--'.$quoteArray[$i]['author'].'<br><br>';
        $quoteString .= '<input type = "submit" name = "plus" value = "+">';
        $quoteString .= '<input type = "hidden" name = "id" value = "'.$quoteArray[$i]['id'].'">';
        $quoteString .= '<label id = "rating"> '.$quoteArray[$i]['rating'].' </label>';
        $quoteString .= '<input type = "submit" name = "minus" value = "-">';
        $quoteString .= '<input type = "submit" name = "delete" value = "Delete">';
        $quoteString .= '</form>';
    }
    echo $quoteString;
    }
}

function quoteEntry($theDBA,$quote, $author){
        $theDBA->addQuote($quote,$author);
        header("Location:view.php");
}
?>