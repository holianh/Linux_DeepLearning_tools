# Ghi đọc file với C++

Dữ liệu dạng:
```
<text>=<value>\n
<text>=<value>\n
...
<text>=<value>\n
```

<details>
	<summary>Code đọc ghi file config</summary>


```c++
#ifndef FUNCS_H
#define FUNCS_H
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;


class funcs
{
public:
    funcs(); 

//-----------------------------------------
    int debTA=1;
    int debKhai=1;
    string filename="debugconfig.ini";

    ///
    /// \brief readDebugConfig
    /// Config file có nội dung là nhiều dòng
    /// Mỗi dòng có dạng: <string>=<value>
    /// Mục tiêu để đọc giá trị vào biến
    /// Nếu muốn thêm, thì thêm vào phần if(!ifi){
    /// và thêm biến bên trên
    void readDebugConfig(){
        ifstream ifi(filename); // config debug
        if (!ifi) {
            ofstream ofi;
            ofi.open(filename,fstream::out | fstream::trunc);
            ofi <<"debTA=1\n";
            ofi <<"debKhai=1\n";
            ofi.close();
        }else{
            string sName, line;
            int value;
            while(getline(ifi, line)){
                istringstream iss1(line);
                getline(iss1, sName, '=');
                iss1 >> value;
                if(sName.compare("debTA")==0){debTA=value;}
                if(sName.compare("debKhai")==0){debKhai=value;}
            }
        }
    }
//-----------------------------------------


};



#endif // FUNCS_H

```
	
</details>


# Hướng dẫn đọc biến của class khác từ class này

Giả sử có 2 class, Class A và Class B, Class B muốn đọc thông tin trong class A, thì làm tn?
1. Khai báo 

```c++
// file clsA.h:
class clsA:
{
	public:
	....
	static int var1; // vì là static nên không được khởi tạo trước
	....
}

int clsA:var1=1; // khởi tạo nó ở đây, hoặc trong file .cpp

```

3. Trong class B, 

```c++
#include clsA.h
clsA mA; // Khai báo handle cho class clsA
if(mA.var1){ // đọc giá trị biến trong clsA
	....
}
```

# Khai báo biến toàn cục cho nhiều file trong chường trình (extern var)

__header__:
```c++
#ifndef HEADER_H
#define HEADER_H

// any source file that includes this will be able to use "global_x"
extern int global_x;

void print_global_x();

#endif
```

__source 1__:

```c++
// since global_x still needs to be defined somewhere,
// we define it (for example) in this source file
int global_x; // Kinh nghiệm là khai báo trước khi include header cho proj lớn sẽ chạy được, không hiểu sao.

#include "header.h"

int main()
{
    //set global_x here:
    global_x = 5;

    print_global_x();
}
```

__source 2__:

```C++
#include <iostream>
#include "header.h"

void print_global_x()
{
    //print global_x here:
    std::cout << global_x << std::endl;
}
```



