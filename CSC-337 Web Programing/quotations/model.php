<?php
//Derek Tominaga
class DatabaseAdapter {
    private $DB;
    public function __construct() {
        $dataBase ='mysql:dbname=quotes;charset=utf8;host=127.0.0.1';
        
        $user ='root';
        $password ='';
        
        try {
            $this->DB = new PDO ( $dataBase, $user, $password );
            $this->DB->setAttribute ( PDO::ATTR_ERRMODE,
                
                PDO::ERRMODE_EXCEPTION );
            
        } catch ( PDOException $e ) {
            echo ('Error establishing Connection');
            exit ();
        }      
    }//End of constructor
    
    public function getAllQuotations(){
        $stmt = $this->DB->prepare('SELECT * FROM quotations ORDER BY rating DESC');
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }//End of getAllQuotations
    
    public function getAllUsers(){
        $stmt = $this->DB->prepare('SELECT * FROM users');
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }//End of getAllUsers
    
    public function verifyCredentials($account, $psw){
        $stmt = $this->DB->prepare('SELECT * FROM users WHERE username = "'.$account.'"');
        $stmt->execute();
        $array = $stmt->fetchAll(PDO::FETCH_ASSOC);
        if ($array[0]['password'] === $psw){
            return True;
        }else{
            return False;
        }
    }//End of verifyCredentials
    
    public function addQuote($quote, $author){
//         $stmt = $this->DB->prepare('insert into quotations(quote,added,author,rating,flagged) 
//             values("'.$quote.'",NOW(),"'.$author.'",0,0)');
        $stmt = $this->DB->prepare('insert into quotations(quote,added,author,rating,flagged)
            values(:bind_quote,NOW(),:bind_author,0,0)');
        $stmt->bindParam (':bind_quote', $quote);
        $stmt->bindParam (':bind_author', $author);
        $stmt->execute();
    }//end of addQuote
    
    public function addUser($accountName, $psw){
        $stmt = $this->DB->prepare('insert into users(username,password) 
            values("'.$accountName.'","'.$psw.'")');
        $stmt->execute();
    }//End of addUsers
    
    public function ratingUp($id){
        $stmt = $this->DB->prepare('UPDATE quotations SET rating = rating + 1 WHERE id ='.$id);
        $stmt->execute();
    }//end of ratingUp
    
    public function ratingDown($id){
        $stmt = $this->DB->prepare('UPDATE quotations SET rating = rating - 1 WHERE id ='.$id);
        $stmt->execute(); 
    }//end of ratingDown
    
    public function deleteEntry($id){
        $stmt = $this->DB->prepare('DELETE FROM quotations WHERE id ='.$id);
        $stmt->execute();
    }//end of deleteEntry
    
} // End class DatabaseAdapter


//Start of Testing 
//$theDBA = new DatabaseAdapter ();
//$theDBA->ratingUp(61);

// if($theDBA->verifyCredentials('Kevin','1234')){
//     echo 'works'.PHP_EOL;
// }else{
//     echo 'broken'.PHP_EOL;
// }
// if(!$theDBA->verifyCredentials('Kevin','1256')){
//     echo 'works'.PHP_EOL;
// }else{
//     echo 'broken'.PHP_EOL;
// }
// if(!$theDBA->verifyCredentials('Random','random')){
//     echo 'works'.PHP_EOL;
// }else{
//     echo 'broken'.PHP_EOL;
// }
// $theDBA->addUser('Ryan', 'abcd');
// $theDBA->addQuote('It Is Ok World', 'Ryan');
// $arr = $theDBA->getAllQuotations();
// print_r($arr);
// $arr = $theDBA->getAllUsers();
// print_r($arr);

?>