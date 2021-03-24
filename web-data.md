# Web Kết nối CSDL sqlite với PHP

```php
<?php
   class MyDB extends SQLite3
   {
      function __construct()
      {
         $this->open('data.db');
      }
   }
   $conn = new MyDB();
   if(!$conn){
      echo $conn->lastErrorMsg();
   } else {
      echo "Opened database successfully\n";
   }


   $sql="SELECT  * FROM `SellingKeys` WHERE `username` like 'Vui%'";;
   $rows = array();
   $k=0;
   $result = $conn->query($sql);
      while($row = $result->fetchArray(SQLITE3_ASSOC)) {
         foreach($row as $row1){
            $order   = array("\r\n", "\n", "\r");
            $replace = '<br />';
            $newstr = str_replace($order, $replace, $row1);
            echo $newstr.", ";
            $k+=1;
         }
         echo "<br/>"; 
      }

?>
```
