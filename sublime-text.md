# Lệnh hay trong Sublime-Text
  1. Multi-cusor: Bôi đen 1 vùng => Ctr-Shift-L / ctr + click
  2. insert increase number: multi cusor => ctr_alt_i
  3. 


# Chỉnh sửa snippet html để có mẫu chuẩn:
khi bấm ctr_shift_p, chọn snippet html sẽ có mẫu như mình mong muốn:
## cài đặt:
1. PackageResourceViewer
2. Ctr_ship_p => PackageResourceViewer:open...
Chọn snippet HTML: thay code trong đó bằng cái ở đây

Chú ý: trong snippet code, thay `$` bằng: `\$`

hoặc thêm cái snippet mới cho dễ.

<details> 
	<summary>title or explanatory caption</summary>  

```html
<snippet>
	<content><![CDATA[
<?php 
if (isset(\$_POST['type'])) {
    if (isset(\$_POST['short_name'])) {
          if (\$_POST['short_name']==="123"){
              http_response_code(200);
              echo 'Kết quả:'.\$_POST['short_name'];
              echo ', Thành công rồi!!!';
          }else{              
              http_response_code(333);
              echo "Có lỗi rồi nhé ...";
              echo \$_POST['short_name'];
          }   
          die();       
    }
    http_response_code(333);
    echo " Có lỗi rồi ...";
    die();
}
?>
<!-- =============================================================================================== -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>[AiSolutions.vn]</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <!-- 
    <link rel="stylesheet" href="/vendor/1.css" crossorigin="anonymous">
    <script src="/vendor/1.js" crossorigin="anonymous"></script> 
    -->
  </head>
  <body>
      <div data-include="header" id="header"></div>
    <!-- =============================================================================================== -->      
      <div class="container">        
        
          <div class="card text-center">
            <div class="card-body ">
              <div class="row ">
                <div class="col-md-6">
                    <h5 class="card-title">Face ID- Nhận diện khuôn mặt</h5>
                    <a href="#"><img src="https://aisolutions.vn/pro/imgs/01-AI-FaceID.png" width="100%"></a>
                </div>
                <div class="col-md-6">
                    <h5 class="card-title">Phương tiện giao thông</h5>
                    <a href="#"><img src="https://aisolutions.vn/pro/imgs/02-AI-Phuong%20tien.png" width="100%"></a>
                </div>        
              </div>
            </div>
          </div>
          <input  class="form-control" type="text" id="short_name" name="short_name" value="123" placeholder="123 sẽ thành công, cái khác sẽ lỗi"><br> 
          <input type="button" class="btn btn-danger" id="submit" value="Chạy" onclick="fnTA_FUNC()"><br> 
          <span id="input-validate">Waiting for user input...</span>
      </div>

    <!-- =============================================================================================== -->
      <script type="text/javascript">
        function fnTA_FUNC() {
        var short_name=\$('#short_name').val();
        var data   = {  short_name: short_name,
                        type:       'del' ,                      
                   };
            console.log('Đối tượng:' + short_name);
            \$.ajax({
                url: 'index.php', // this is the target
                method: 'post', // method
                data: data, // pass the input value to server
                success: function(response) { // if the http response code is 200
                    \$('#input-validate').css('color', 'green').html(response); 
                    document.getElementById("submit").className = "btn btn-info";  
                    console.log('Response success:');                
                    console.log(response);
                },
                error: function(r) { // if the http response code is other than 200
                    document.getElementById("submit").className = "btn btn-warning"; 
                    \$('#input-validate').css('color', 'red').html(r.responseText);
                    console.log('Response error:');                
                    console.log(r.responseText);
                    
                }
            });
      };
    </script>




    <!-- =============================================================================================== -->
  <div data-include="footer" id="footer"></div> 
  <script>
      async function fetchHtmlAsText(url) { return await (await fetch(url)).text(); }
      async function loadHome() {
          document.getElementById("header").innerHTML = await fetchHtmlAsText("/vendor/header.html");
          document.getElementById("footer").innerHTML = await fetchHtmlAsText("/vendor/footer.html");
      }
      loadHome();
  </script> 
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
  </body>
</html>    
  


 
	
]]></content>
	<tabTrigger>html</tabTrigger>
	<scope>text.html &amp; (- meta.tag | punctuation.definition.tag.begin)</scope>
</snippet>

```

 </details>
 

