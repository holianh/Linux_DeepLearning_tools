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

# html to excel:
```html
    <table id="simpleTable1">
        <thead><tr><th>A</th><th>B</th><th>C</th></tr></thead>
        <tbody>
              <tr><td>1</td><td>2</td><td>3</td></tr>
              <tr><td>1</td><td>2</td><td>3</td></tr>
              <tr><td>1</td><td>2</td><td>3</td></tr>             
        </tbody>
    </table>
    <script src="https://cdn.jsdelivr.net/gh/linways/table-to-excel@v1.0.4/dist/tableToExcel.js"></script>
    <button id="button-excel">Create Excel</button>
    <script type="text/javascript">
        let button = document.querySelector("#button-excel");
        button.addEventListener("click", e => {
          let table = document.querySelector("#simpleTable1");
          TableToExcel.convert(table);
      });
    </script>
```


# html pre, p, div max height:

```html
<style>
    pre {
      max-height: 400px;
      overflow: auto;
    }
    </style>
```

Nếu muốn riêng 1 class nào đó:

```html
<!DOCTYPE html>
<html>
<head>
<style>
p.ex1 {
  max-height: 50px;
  overflow: auto;
}
</style>
</head>
<body>
<h1>The max-height Property</h1>

<h2>max-height: none (default):</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam semper diam at erat pulvinar, at pulvinar felis blandit. Vestibulum volutpat tellus diam, consequat gravida libero rhoncus ut. Maecenas imperdiet felis nisi, fringilla luctus felis hendrerit sit amet. Pellentesque interdum, nisl nec interdum maximus, augue diam porttitor lorem, et sollicitudin felis neque sit amet erat.</p>

<h2>max-height: 50px:</h2>
<p class="ex1">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam semper diam at erat pulvinar, at pulvinar felis blandit. Vestibulum volutpat tellus diam, consequat gravida libero rhoncus ut. Maecenas imperdiet felis nisi, fringilla luctus felis hendrerit sit amet. Pellentesque interdum, nisl nec interdum maximus, augue diam porttitor lorem, et sollicitudin felis neque sit amet erat.</p>

</body>
</html>
```

