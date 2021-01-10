# Đọc file CSV=> array:
<details>
<summary>Full code:</summary>
	
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


</details>

# js post thông tin (jquery) yêu cầu xoá thông tin trên server:
yêu cầu có dùng cái này trong header hoặc footer:
```html
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
...
<input type="button" class="btn" id="xoa" value="Xoá" onclick="fnXoa()">
```
## Code JS yêu cầu xoá:

<details>
<summary>Full code:</summary>
	
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


</details>

## Code PHP đầu file, thực  hiện xoá:

<details>
<summary>Full code:</summary>
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


</details>

# html to excel:
<details>
<summary>Full code:</summary>
	
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


</details>

# html pre, p, div max height:

<details>
<summary>Full code:</summary>
	
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

</details>

# html js chart pan zoom:

<details>
<summary>Full code:</summary>
	
```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Chart Pan Zoom</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    
    <link rel="stylesheet" type="text/css" href="https://cdn3.devexpress.com/jslib/20.2.4/css/dx.common.css" />
    <link rel="stylesheet" type="text/css" href="https://cdn3.devexpress.com/jslib/20.2.4/css/dx.light.css" />
    <script src="https://cdn3.devexpress.com/jslib/20.2.4/js/dx.all.js"></script>
    
    <!-- <link rel="stylesheet" type="text/css" href="styles.css" /> -->
    <style type="text/css">
        #chart {
            height: 440px;
            width: 95%; 
            margin-left: auto;
            margin-right: auto;
        }
    </style>
</head>
<body class="dx-viewport">
    <div class="demo-container">
        <div id="chart"></div>
    </div>

    
    <!-- <script src="data.js"></script> -->
    <!-- <script src="index.js"></script> -->
    <script type="text/javascript">
        var zoomingData =  [ { arg: 10, y1: -12, y2: 10, y3: 32 },
            { arg: 20, y1: -32, y2: 30, y3: 12 },
            { arg: 40, y1: -20, y2: 20, y3: 30 },
            { arg: 50, y1: -39, y2: 50, y3: 19 },
            { arg: 60, y1: -10, y2: 10, y3: 15 },
            { arg: 75, y1: 10, y2: 10, y3: 15 },
            { arg: 80, y1: 30, y2: 50, y3: 13 },
            { arg: 90, y1: 40, y2: 50, y3: 14 },
            { arg: 100, y1: 50, y2: 90, y3: 90 },
            { arg: 105, y1: 40, y2: 175, y3: 120 },
            { arg: 110, y1: -12, y2: 10, y3: 32 },
            { arg: 120, y1: -32, y2: 30, y3: 12 },
            { arg: 130, y1: -20, y2: 20, y3: 30 },
            { arg: 140, y1: -12, y2: 10, y3: 32 },
            { arg: 150, y1: -32, y2: 30, y3: 12 },
            { arg: 160, y1: -20, y2: 20, y3: 30 },
            { arg: 170, y1: -39, y2: 50, y3: 19 },
            { arg: 180, y1: -10, y2: 10, y3: 15 },
            { arg: 185, y1: 10, y2: 10, y3: 15 },
            { arg: 190, y1: 30, y2: 100, y3: 13 },
            { arg: 200, y1: 40, y2: 110, y3: 14 },
            { arg: 210, y1: 50, y2: 90, y3: 90 },
            { arg: 220, y1: 40, y2: 95, y3: 120 },
            { arg: 230, y1: -12, y2: 10, y3: 32 },
            { arg: 240, y1: -32, y2: 30, y3: 12 },
            { arg: 255, y1: -20, y2: 20, y3: 30 },
            { arg: 270, y1: -12, y2: 10, y3: 32 },
            { arg: 280, y1: -32, y2: 30, y3: 12 },
            { arg: 290, y1: -20, y2: 20, y3: 30 },
            { arg: 295, y1: -39, y2: 50, y3: 19 },
            { arg: 300, y1: -10, y2: 10, y3: 15 },
            { arg: 310, y1: 10, y2: 10, y3: 15 },
            { arg: 320, y1: 30, y2: 100, y3: 13 },
            { arg: 330, y1: 40, y2: 110, y3: 14 },
            { arg: 340, y1: 50, y2: 90, y3: 90 },
            { arg: 350, y1: 40, y2: 95, y3: 120 },
            { arg: 360, y1: -12, y2: 10, y3: 32 },
            { arg: 367, y1: -32, y2: 30, y3: 12 },
            { arg: 370, y1: -20, y2: 20, y3: 30 },
            { arg: 380, y1: -12, y2: 10, y3: 32 },
            { arg: 390, y1: -32, y2: 30, y3: 12 },
            { arg: 400, y1: -20, y2: 20, y3: 30 },
            { arg: 410, y1: -39, y2: 50, y3: 19 },
            { arg: 420, y1: -10, y2: 10, y3: 15 },
            { arg: 430, y1: 10, y2: 10, y3: 15 },
            { arg: 440, y1: 30, y2: 100, y3: 13 },
            { arg: 450, y1: 40, y2: 110, y3: 14 },
            { arg: 460, y1: 50, y2: 90, y3: 90 },
            { arg: 470, y1: 40, y2: 95, y3: 120 },
            { arg: 480, y1: -12, y2: 10, y3: 32 },
            { arg: 490, y1: -32, y2: 30, y3: 12 },
            { arg: 500, y1: -20, y2: 20, y3: 30 },
            { arg: 510, y1: -12, y2: 10, y3: 32 },
            { arg: 520, y1: -32, y2: 30, y3: 12 },
            { arg: 530, y1: -20, y2: 20, y3: 30 },
            { arg: 540, y1: -39, y2: 50, y3: 19 },
            { arg: 550, y1: -10, y2: 10, y3: 15 },
            { arg: 555, y1: 10, y2: 10, y3: 15 },
            { arg: 560, y1: 30, y2: 100, y3: 13 },
            { arg: 570, y1: 40, y2: 110, y3: 14 },
            { arg: 580, y1: 50, y2: 90, y3: 90 },
            { arg: 590, y1: 40, y2: 95, y3: 12 },
            { arg: 600, y1: -12, y2: 10, y3: 32 },
            { arg: 610, y1: -32, y2: 30, y3: 12 },
            { arg: 620, y1: -20, y2: 20, y3: 30 },
            { arg: 630, y1: -12, y2: 10, y3: 32 },
            { arg: 640, y1: -32, y2: 30, y3: 12 },
            { arg: 650, y1: -20, y2: 20, y3: 30 },
            { arg: 660, y1: -39, y2: 50, y3: 19 },
            { arg: 670, y1: -10, y2: 10, y3: 15 },
            { arg: 680, y1: 10, y2: 10, y3: 15 },
            { arg: 690, y1: 30, y2: 100, y3: 13 },
            { arg: 700, y1: 40, y2: 110, y3: 14 },
            { arg: 710, y1: 50, y2: 90, y3: 90 },
            { arg: 720, y1: 40, y2: 95, y3: 120 },
            { arg: 730, y1: 20, y2: 190, y3: 130 },
            { arg: 740, y1: -32, y2: 30, y3: 12 },
            { arg: 750, y1: -20, y2: 20, y3: 30 },
            { arg: 760, y1: -12, y2: 10, y3: 32 },
            { arg: 770, y1: -32, y2: 30, y3: 12 },
            { arg: 780, y1: -20, y2: 20, y3: 30 },
            { arg: 790, y1: -39, y2: 50, y3: 19 },
            { arg: 800, y1: -10, y2: 10, y3: 15 },
            { arg: 810, y1: 10, y2: 10, y3: 15 },
            { arg: 820, y1: 30, y2: 100, y3: 13 },
            { arg: 830, y1: 40, y2: 110, y3: 14 },
            { arg: 840, y1: 50, y2: 90, y3: 90 },
            { arg: 850, y1: 40, y2: 95, y3: 120 },
            { arg: 860, y1: -12, y2: 10, y3: 32 },
            { arg: 870, y1: -32, y2: 30, y3: 12 },
            { arg: 880, y1: -20, y2: 20, y3: 30 }
        ];
        $(function(){
    
            var zoomedChart = $("#chart").dxChart({
                palette: "Harmony Light",
                dataSource: zoomingData,
                series: [{
                    argumentField: "arg",
                    valueField: "y1"
                }, {
                    argumentField: "arg",
                    valueField: "y2"
                }],
                tooltip: {
                    enabled: true,
                },
                argumentAxis: {
                    visualRange: {
                        startValue: 300,
                        endValue: 500
                    }
                },
                scrollBar: {
                    visible: true
                },
                zoomAndPan: {
                    argumentAxis: "both"
                },
                legend:{
                    visible: false
                }
            }).dxChart("instance");
            
        });
    </script>
</body>
</html>	
```
</details>


<details>
<summary>Full code:</summary>

</details>
