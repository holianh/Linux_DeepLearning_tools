# Đọc file CSV=> array:
```php
$myFile='short_url.csv';
$csv  = array();
$file = fopen($myFile, 'r');
while (($result = fgetcsv($file)) !== false){
    $csv[] = $result;
}
fclose($file);
```
Định dạng file đầu vào:
```
thanh-hai,https://aisolutions.vn
the-diep,https://aisolutions.vn/pro
huy-du,https://aisolutions.vn/pro/index
```

Kết quả:
```
Array (
    [0] => Array (
            [0] => thanh-hai
            [1] => https://aisolutions.vn        )
    [1] => Array (
            [0] => the-diep
            [1] => https://aisolutions.vn/pro      )
    [2] => Array (
            [0] => huy-du
            [1] => https://aisolutions.vn/pro/index )
)
```

# js post thông tin (jquery) yêu cầu xoá thông tin trên server:
yêu cầu có dùng cái này trong header hoặc footer:
```html
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
...
<input type="button" class="btn" id="xoa" value="Xoá" onclick="fnXoa()">
```
## Code JS yêu cầu xoá:
```html
<script type="text/javascript">
    function fnXoa() {
        var short_name=$('#short_name').val();
        var data   = {	short_name: short_name,
                        type:       'del',
                        pass: 		$('#long_name').val()
                     };
        console.log('Nếu là Admin: Xoá đối tượng:'+short_name);			 	
        console.log('Nếu là Admin, va:'+data);			 	
        // perform an ajax call
        $.ajax({
            url: 'index.php', // this is the target
            method: 'post', // method
            data: data, // pass the input value to server
            success: function(r) { // if the http response code is 200
                $('#input-validate').css('color', 'green').html(r);		                
            },
            error: function(r) { // if the http response code is other than 200
                console.log(r.responseText);
                $('#input-validate').css('color', 'red').html(r.responseText);
            }
        });
    };
</script>
```
## Code PHP đầu file, thực  hiện xoá:
```php
if(isset($_POST['type'])) {
	if ($_POST['type']=='del') {
		if ($_POST['pass']=='123') {
			// Xoá: $_POST['short_name']
			echo "Bắt đầu xoá....";
			$short_name = $_POST['short_name'];
			// $myFile='short_url.csv';
			$csv1  = array();
			$file = fopen($myFile, 'r');
			while (($result = fgetcsv($file)) !== false){
				if ($short_name!= $result[0]){
			    	$csv1[] = $result;
			    }
			}			
			fclose($file);			// print_r($csv1);
			function FnWrite_csv( $strMyFile, $data) {
			    $file = fopen($strMyFile, 'w');				
				foreach ($data as $value) {
					fwrite($file,$value[0].','.$value[1]."\r\n");
				}
				fclose($file);
			}
			FnWrite_csv($myFile, $csv1) ;
			die();
		}
	}
}
```

# 