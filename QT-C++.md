# Ghi đọc file với C++

Dữ liệu dạng:
<text>=<value>\n
<text>=<value>\n
...
<text>=<value>\n

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
