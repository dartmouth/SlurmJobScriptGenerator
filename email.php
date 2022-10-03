<!-- https://www.geeksforgeeks.org/how-to-fill-all-input-fields-automatically-from-database-by-entering-input-in-one-textbox-using-php/ -->
<?php
// Get the user id 
$user_id = $_REQUEST['user_id'];
  
// Database connection
$con = mysqli_connect("localhost", "root", "", "gfg");
  
if ($user_id !== "") {
      
    // Get corresponding first name and 
    // last name for that user id    
    $query = mysqli_query($con, "SELECT email_address FROM userdata WHERE user_id='$user_id'");
  
    $row = mysqli_fetch_array($query);
  
    // Get the user id
    $email_address = $row["email_address"];
}
// Store it in a array
$result = array("$user_id");
  
// Send in JSON encoded form
$myJSON = json_encode($result);
echo $myJSON;
?>