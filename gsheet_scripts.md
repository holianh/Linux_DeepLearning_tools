# Nhập data vào ô B4:E4, tự động copy, sắp xếp xuống vùng bên dưới
Dòng 1  Tiêu đề
Dòng 2: tổng cộng
Dòng 3: "Chi tiết"
Dòng 4: input
Dòng 5: Tiêu đề của data
Dòng 6 trở đi: data tự động sắp xếp

Copy code này thay cho macro.gs của google spreadsheet:

```javascript
function onOpen( ){
// This line calls the SpreadsheetApp and gets its UI   
// Or DocumentApp or FormApp.
  var ui = SpreadsheetApp.getUi();
 
//These lines create the menu items and 
// tie them to functions we will write in Apps Script
  
 ui.createMenu('Đường Hoàng Yến')
      .addItem('Mong cho số tiền quyên góp đầy đủ!', 'Add_Data_sort')
      .addToUi();
}

function ta_Datetime(){
  var ss = SpreadsheetApp.getActive();
  ss.getRange("B3").setValue(new Date()).setNumberFormat("dd/mm/yyyy hh:mm")
  
}

function Add_Data_sort() {
  Browser.msgBox("Chào mừng đến với Đường hoàng Yến, sắp tới đích rồi, cố lên");
}

/** @OnlyCurrentDoc */

function TA_Tu_dong_sap_sep() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('B6:G700').activate()
  .sort([{column: 3, ascending: false}, {column: 2, ascending: true}]);
};

function CheckBlank(){
  var ss = SpreadsheetApp.getActive();
  var b4 = ss.getRange("B4").getValues();
  var c4 = ss.getRange("C4").getValues(); 
  var f4 = ss.getRange("F4").getValues();
  var g4 = ss.getRange("G4").getValues();
  var blk=1;
  if (b4=="") {blk=0;
               Browser.msgBox("Nhập tên vào đi em ơi!")
               return 0;
              }
  if (c4=="") {blk=0;
               Browser.msgBox("Nhập số tiền vào chứ, quan trọng thế cơ mà!");
              return 0;
              } 
  if (f4=="") {blk=0;
               Browser.msgBox("Nhập số điện thoại vào, không có thì nhập tạm số 0!");
              return 0;}
  if (g4=="") {blk=0;
               Browser.msgBox("Loại tiền: TM hay CK?");
              return 0;}
  return blk;
}

function TA_Them_Sapxep(){
  if (CheckBlank()==1){
    //1. Lưu dữ liệu vào bảng:
    //    '1.1 tìm dòng cuối
    var ss = SpreadsheetApp.getActive();
    var Avals = ss.getRange("B6:B").getValues();
    var DongCuoi = Avals.filter(String).length;
    DongCuoi=DongCuoi+6; // offset từ đầu xuống
    var des="B" + DongCuoi + ":G" + DongCuoi;
    //Browser.msgBox(des);
    ss.getRange("A"+DongCuoi).setValue(DongCuoi-5)
    //SpreadsheetApp.getActiveSheet().getRange('F2').setValue('Hello');
    
    ss.getRange("E4").setValue(new Date()).setNumberFormat("dd/mm/yyyy")
    
    ss.getRange("B4:G4").copyTo(ss.getRange(des));
    ss.getRange("B4:G4").clearContent();
    TA_Tu_dong_sap_sep();
    ss.setActiveSelection("B4");
    ta_Datetime();
  }
};
  
```  


