# timezone +7 HoChiMinh

```php
session_start();
date_default_timezone_set('Asia/Ho_Chi_Minh');
$email=$_COOKIE["email"];
```

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
	
```html
<style>
    pre {
      max-height: 400px;
      overflow: auto;
    }
    </style>
```

<details>
<summary>Full code:</summary>
	
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

# Hàm loại bỏ dấu tiếng Việt
<details> 
<summary>Hàm JS loại bỏ dấu tiếng Việt:</summary>

```javascript
      function removeVietnameseTones(str) {
        str = str.replace(/à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ/g,"a"); 
        str = str.replace(/è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ/g,"e"); 
        str = str.replace(/ì|í|ị|ỉ|ĩ/g,"i"); 
        str = str.replace(/ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ/g,"o"); 
        str = str.replace(/ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ/g,"u"); 
        str = str.replace(/ỳ|ý|ỵ|ỷ|ỹ/g,"y"); 
        str = str.replace(/đ/g,"d");
        str = str.replace(/À|Á|Ạ|Ả|Ã|Â|Ầ|Ấ|Ậ|Ẩ|Ẫ|Ă|Ằ|Ắ|Ặ|Ẳ|Ẵ/g, "A");
        str = str.replace(/È|É|Ẹ|Ẻ|Ẽ|Ê|Ề|Ế|Ệ|Ể|Ễ/g, "E");
        str = str.replace(/Ì|Í|Ị|Ỉ|Ĩ/g, "I");
        str = str.replace(/Ò|Ó|Ọ|Ỏ|Õ|Ô|Ồ|Ố|Ộ|Ổ|Ỗ|Ơ|Ờ|Ớ|Ợ|Ở|Ỡ/g, "O");
        str = str.replace(/Ù|Ú|Ụ|Ủ|Ũ|Ư|Ừ|Ứ|Ự|Ử|Ữ/g, "U");
        str = str.replace(/Ỳ|Ý|Ỵ|Ỷ|Ỹ/g, "Y");
        str = str.replace(/Đ/g, "D");
        // Some system encode vietnamese combining accent as individual utf-8 characters
        // Một vài bộ encode coi các dấu mũ, dấu chữ như một kí tự riêng biệt nên thêm hai dòng này
        str = str.replace(/\u0300|\u0301|\u0303|\u0309|\u0323/g, ""); // ̀ ́ ̃ ̉ ̣  huyền, sắc, ngã, hỏi, nặng
        str = str.replace(/\u02C6|\u0306|\u031B/g, ""); // ˆ ̆ ̛  Â, Ê, Ă, Ơ, Ư
        // Remove extra spaces
        // Bỏ các khoảng trắng liền nhau
        str = str.replace(/ + /g," ");
        str = str.trim();
        // Remove punctuations
        // Bỏ dấu câu, kí tự đặc biệt
        str = str.replace(/!|@|%|\^|\*|\(|\)|\+|\=|\<|\>|\?|\/|,|\.|\:|\;|\'|\"|\&|\#|\[|\]|~|\$|_|`|-|{|}|\||\\/g," ");
        return str;
    };	
```	
</details>

<details> 
<summary>Hàm PHP loại bỏ dấu tiếng Việt:</summary>

```PHP
function vn_str_filter ($str){
       $unicode = array(
           'a'=>'á|à|ả|ã|ạ|ă|ắ|ặ|ằ|ẳ|ẵ|â|ấ|ầ|ẩ|ẫ|ậ',
           'd'=>'đ',
           'e'=>'é|è|ẻ|ẽ|ẹ|ê|ế|ề|ể|ễ|ệ',
           'i'=>'í|ì|ỉ|ĩ|ị',
           'o'=>'ó|ò|ỏ|õ|ọ|ô|ố|ồ|ổ|ỗ|ộ|ơ|ớ|ờ|ở|ỡ|ợ',
           'u'=>'ú|ù|ủ|ũ|ụ|ư|ứ|ừ|ử|ữ|ự',
           'y'=>'ý|ỳ|ỷ|ỹ|ỵ',
           'A'=>'Á|À|Ả|Ã|Ạ|Ă|Ắ|Ặ|Ằ|Ẳ|Ẵ|Â|Ấ|Ầ|Ẩ|Ẫ|Ậ',
           'D'=>'Đ',
           'E'=>'É|È|Ẻ|Ẽ|Ẹ|Ê|Ế|Ề|Ể|Ễ|Ệ',
           'I'=>'Í|Ì|Ỉ|Ĩ|Ị',
           'O'=>'Ó|Ò|Ỏ|Õ|Ọ|Ô|Ố|Ồ|Ổ|Ỗ|Ộ|Ơ|Ớ|Ờ|Ở|Ỡ|Ợ',
           'U'=>'Ú|Ù|Ủ|Ũ|Ụ|Ư|Ứ|Ừ|Ử|Ữ|Ự',
           'Y'=>'Ý|Ỳ|Ỷ|Ỹ|Ỵ',
       );
      foreach($unicode as $nonUnicode=>$uni){
           $str = preg_replace("/($uni)/i", $nonUnicode, $str);
      }
       return $str;
   }	
```	
</details>

# PHP sort multi column array
Sắp xếp mảng theo nhiều cột trong PHP
	
<details>
<summary>Cách số 1, sắp xếp theo ID cột:</summary>

```php
 $tallest_buildings = [
            ["Burj Khalifa"           , "Dubai"    , "United Arab Emirates" , 828 , 163 , 2010] ,
            ["Burj Khalifa"           , "Dubai"    , "United Arab Emirates" , 666 , 163 , 2010] ,
            ["Burj Khalifa"           , "Dubai"    , "United Arab Emirates" , 666 , 163 , 444]  ,
            ["Shanghai Tower"         , "Shanghai" , "China"                , 632 , 128 , 2015] ,
            ["Abraj Al-Bait Towers"   , "Mecca"    , "Saudi Arabia"         , 601 , 120 , 2012] ,
            ["Ping An Finance Center" , "Shenzhen" , "China"                , 599 , 115 , 2017] ,
            ["Lotte World Tower"      , "Seoul"    , "South Korea"          , 554 , 123 , 2016]
        ];
         
        function storey_sort($building_a, $building_b) { // Sort by: Floors => Height => Year
            list($c0,$c1,$c2)=array_values([3,4,5]); // The column index
            $v1= $building_a[$c0] - $building_b[$c0];
            if($v1==0){
                $v1= $building_a[$c1] - $building_b[$c1];
                if($v1==0){
                    $v1= $building_a[$c2] - $building_b[$c2];
                }
            }
            return $v1;
        }
         
        usort($tallest_buildings, "storey_sort" );
         
        foreach($tallest_buildings as $tall_building) {
            list($building, $city, $country, $height, $floors,$year) = array_values($tall_building);
            echo $building." is in ".$city.", ".$country.". It is ".$height." meters tall with ".$floors." floors. $year\n<br>";
        }
```
	
</details>

<details>
<summary>Cách số 2, mảng có tên, sắp xếp theo tên:</summary>

```php
	
 $tallest_buildings = [
            ["Building" => "Burj Khalifa","City" => "Dubai","Country" => "United Arab Emirates","Height" => 828,"Floors" => 163,"Year" => 2010],
            ["Building" => "Burj Khalifa","City" => "Dubai","Country" => "United Arab Emirates","Height" => 666,"Floors" => 163,"Year" => 2010],
            ["Building" => "Burj Khalifa","City" => "Dubai","Country" => "United Arab Emirates","Height" => 666,"Floors" => 163,"Year" => 444],
            ["Building" => "Shanghai Tower","City" => "Shanghai","Country" => "China","Height" => 632,"Floors" => 128,"Year" => 2015],
            ["Building" => "Abraj Al-Bait Towers","City" => "Mecca","Country" => "Saudi Arabia","Height" => 601,"Floors" => 120,"Year" => 2012],
            ["Building" => "Ping An Finance Center","City" => "Shenzhen","Country" => "China","Height" => 599,"Floors" => 115,"Year" => 2017],
            ["Building" => "Lotte World Tower","City" => "Seoul","Country" => "South Korea" ,"Height" => 554,"Floors" => 123,"Year" => 2016]
        ];
         
        function storey_sort($building_a, $building_b) { // Sort by: Floors => Height => Year
            $v1= $building_a["Floors"] - $building_b["Floors"];
            if($v1==0){
                $v1= $building_a["Height"] - $building_b["Height"];
                if($v1==0){
                    $v1= $building_a["Year"] - $building_b["Year"];
                }
            }
            return $v1;
        }
         
        usort($tallest_buildings, "storey_sort");
         
        foreach($tallest_buildings as $tall_building) {
            list($building, $city, $country, $height, $floors,$year) = array_values($tall_building);
            echo $building." is in ".$city.", ".$country.". It is ".$height." meters tall with ".$floors." floors. $year\n<br>";
        }
```	
</details>

# Các loại checkbox đẹp
<details>
<summary>Full code:</summary>

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
<label class="custom-control custom-checkbox">
      <input type="checkbox" class="custom-control-input">
      <span class="custom-control-indicator"></span>
      <span class="custom-control-description">Check this<br> custom checkbox</span>
</label>	
```	

Loại 2: tham khảo: [Xem](https://gitbrent.github.io/bootstrap4-toggle/)
	
```html
	

<link href="https://cdn.jsdelivr.net/gh/gitbrent/bootstrap-switch-button@1.1.0/css/bootstrap-switch-button.min.css" rel="stylesheet" />
<script src="https://cdn.jsdelivr.net/gh/gitbrent/bootstrap-switch-button@1.1.0/dist/bootstrap-switch-button.min.js"></script>

<link href="https://cdn.jsdelivr.net/gh/gitbrent/bootstrap4-toggle@3.6.1/css/bootstrap4-toggle.min.css" rel="stylesheet"/>
<script src="https://cdn.jsdelivr.net/gh/gitbrent/bootstrap4-toggle@3.6.1/js/bootstrap4-toggle.min.js"></script>

<input id="toggle-trigger" type="checkbox" data-toggle="toggle">
<button class="btn btn-success" onclick="toggleApiOn()">On by API</button>
<button class="btn btn-danger" onclick="toggleApiOff()">Off by API</button>
<button class="btn btn-success" onclick="toggleInpOn()">On by Input</button>
<button class="btn btn-danger" onclick="toggleInpOff()">Off by Input</button>
<script>
  function toggleApiOn() {
    $('#toggle-trigger').bootstrapToggle('on');
  }
  function toggleApiOff() {
    $('#toggle-trigger').bootstrapToggle('off');
  }
  function toggleInpOn() {
    $('#toggle-trigger').prop('checked', true).change();
  }
  function toggleInpOff() {
    $('#toggle-trigger').prop('checked', false).change();
  }
</script>
<input type="checkbox" id=cb checked data-toggle="toggle" data-on="<i class='fa fa-play'></i> Play" data-off="<i class='fa fa-pause'></i> Pause"> 


```
</details>

# PHP data SQLite:
<details>
<summary>Full code:</summary>
	
```PHP
<?php
echo "connecting via SQLite3<BR>";

unlink('mysqlitedb.db');
$db = new SQLite3('mysqlitedb.db');

$db->exec('CREATE TABLE foo (id INTEGER, bar STRING)');
$db->exec("INSERT INTO foo (id, bar) VALUES (1, 'This is a test')");

$stmt = $db->prepare('SELECT bar FROM foo WHERE id=:id');
$stmt->bindValue(':id', 1, SQLITE3_INTEGER);

$result = $stmt->execute();
var_dump($result->fetchArray());

echo "<P>Connecting via PDO<BR>";

unlink('mysqlitepdo.db');
$db = new PDO('sqlite:mysqlitepdo.db');

$db->exec('CREATE TABLE foo (id INTEGER, bar STRING)');
$db->exec("INSERT INTO foo (id, bar) VALUES (1, 'This is a test')");

$stmt = $db->prepare('SELECT bar FROM foo WHERE id=:id');
$stmt->bindValue(':id', 1, SQLITE3_INTEGER);

$result = $stmt->execute();
var_dump($stmt->fetchAll());

?>	
```
https://stackoverflow.com/questions/18659913/what-is-the-difference-between-sqlite3-and-pdo-sqlite
	
</details>


# Send Array to PHP server
<details>
<summary>Full code:</summary>

```html
// in js
arrItem=[
	["1", "2","5","4","6"],
	["2", "2","6","8","0"],
	["3", "4","6","7","5"],
	];
myIDidx=1;
	
	html="<span  id='"+arrItem[myIDidx]+"'><button type='button' class='btn btn-primary' onclick='fnAdd2Data(\""+arrItem[myIDidx]+" \",\""+ fixedEncodeURIComponent(JSON.stringify(arrItem)) +"\")'>Thêm vào Hệ thống</button> </span>"
	// $("#IDabc").html(html) // Gán giá trị này cho 1 id nào đó.
	
	function fixedEncodeURIComponent(str) {
	    return encodeURIComponent(str).replace(/[!'()*]/g, function(c) {
		return '%' + c.charCodeAt(0).toString(16);
	    });
	}
	function fnAdd2Data(ID,mStr){
		console.log(mStr);
		 $.ajax({
		    type: "POST",
		    url: "",
		    data: {mStr:mStr},
		    success: function(res) {
		       $("#"+ID).html("Done!");
		       console.log(res);
		    },
		    error: function() {
			alert('Lỗi, không gửi lên server được');
		    }
		});
	}	
```
	
Trên server php chạy:
```PHP
if (isset($_POST['mStr'])){
	$mStr=$_POST['mStr'];
	$mStr1=urldecode($mStr);
	echo $mStr1;
	die();
}		
```	
	
</details>


# Table filter
	
<details>
<summary>Full code:</summary>
	
```html
<div class="container-fluid shadow-lg bg-white rounded" style="max-width:90%;">		
		<form>
			<div class="input-group">
			    <div class="input-group-prepend">
			      <div class="input-group-text" id="btnGroupAddon">Tìm kiếm</div>
			    </div>
			    <input id="myInput" onkeyup="myFunction()" type="text" class="form-control" placeholder="Nhập từ khoá tìm kiếm" aria-label="Nhập từ khoá tìm kiếm" aria-describedby="btnGroupAddon">
			    <input type="reset" value="Reset" onclick="mClear()"> <button type="button" onclick="toExcel()">Download</button>
			</div>
		</form> 

		<div class="row" style="max-height: 1200px; overflow: auto;">
		 <script src="https://cdn.jsdelivr.net/gh/linways/table-to-excel@v1.0.4/dist/tableToExcel.js"></script>
		 <script type="text/javascript">            
			  function toExcel(){
			      TableToExcel.convert(document.querySelector("#myTable"));
			  }
		  </script>

	  	<table class="table table-inverse table-hover" id="myTable">
		  	<thead>
		  		<tr>
		  			<th>#</th>
		  			<th style="width:30%;">Câu chú</th>
		  			<th>Số lần đọc</th>
		  			<th>Tác dụng</th>
		  			<th>Chú ý</th>
		  		</tr>
		  	</thead>
		  	<tbody>		  		
				<tr><td>49</td><td>94242</td><td></td><td>Luân xa 7: Não, Thần niệm </td><td>PHÁP<br></td></tr>
				<tr><td>50</td><td>2116</td><td></td><td>Luân xa 6: Tai, Mắt, Xoang </td><td>PHÁP<br></td></tr>
				<tr><td>51</td><td>6122</td><td></td><td>Luân xa 5: Cổ họng </td><td>PHÁP<br></td></tr>
				<tr><td>52</td><td>3102</td><td></td><td>Luân xa 4: Khu vực Tim </td><td>PHÁP<br></td></tr>
				<tr><td>53</td><td>2106</td><td></td><td>Luân xa 4: Khu vực Phổi, Khí quản, Phế quản </td><td>PHÁP<br></td></tr>
				<tr><td>54</td><td>6404</td><td></td><td>Luân xa 3: Gan, Mật, Tụy, Ruột, Thận, Bao tử </td><td>PHÁP<br></td></tr>
				<tr><td>55</td><td>1312</td><td></td><td>Luân xa 2: Ruột, Tử cung, Bọng đái </td><td>PHÁP<br></td></tr>
				<tr><td>56</td><td>2106</td><td></td><td>Luân xa 1: Âm đạo, Dương vật, Hậu môn </td><td>PHÁP<br></td></tr>			
		  	</tbody>
		  </table>
		   <script type="text/javascript">
		        const myFunction = () => {
					  const trs = document.querySelectorAll('#myTable tr:not(.header)')
					  const filter = document.querySelector('#myInput').value
					  const regex = new RegExp(filter, 'i')
					  const isFoundInTds = td => regex.test(td.innerHTML)
					  const isFound = childrenArr => childrenArr.some(isFoundInTds)
					  const setTrStyleDisplay = ({ style, children }) => {
					    style.display = isFound([
					      ...children // <-- All columns
					    ]) ? '' : 'none' 
					  }
					  
					  trs.forEach(setTrStyleDisplay)
					}
				function mClear( ){ 
					document.querySelector('#myInput').value="";
					myFunction();
				}
		    </script>

		  <br>
		  <br>
		  <br>
		</div>
		</div>
			   
```
		
</details>

# SerializeArray JS PHP
Lưu ý: phải có __name__ trong các input/textares/select,... mới nhận được giá trị
	
```javascript
datastring = $("#frmOrders").serializeArray(); 
datastring.push({name: "taUpdateOrders",value:"1"});
```	
<details>
<summary>Full code:</summary>

```js
<script type="text/javascript">
	function fnOrders(){
	    datastring = $("#frmOrders").serializeArray(); 
	    datastring.push({name: "taUpdateOrders",value:"1"});
	    console.table(datastring);
	    $.ajax({
		    url: '',  
		    method: 'post', 
		    data: datastring, 
		    success: function(r) { 
			console.log(r); 
			// alert(r);
			// $("#dInfo").html(r);  
		    },
		    error: function(r) {                   
		    }
		});  
	}
	</script>	
```	
</details>

# Khác

<details>
<summary>Full code:</summary>

</details>



