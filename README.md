##  bilibili_followers 

### 基于哔哩哔哩粉丝系统开发的扩展系统

#### 项目地址：	

GitHub：https://github.com/icomgx/bilibili_followers

Gitee：https://gitee.com/ikcty/bilibili_followers

##### B站主页 https://space.bilibili.com/23106193 有想法和建议欢迎私信我

##### 开发工具：pycharm 环境：Anaconda3（python 3.7.4）

##### 使用库（暂时）： Flask，flask_restful，requests

***

#### 目录结构

##### d2ta/ 为数据库存放目录

##### main/ 各个功能模块存放目录
​	/b2il.py B站主要功能模块   
​	/b2rrage.py 弹幕功能功能模块    
​	/controller.py 主控制器模块   
​	/d2evice.py 设备使用功能模块    
​	/e2xternal.py 外部API功能模块     
​	/error.py 错误信息功能模块  
​	/k2ey.py 密钥功能模块     
​	/models.py 数据库操作功能模块    


##### static/ 静态资源存放目录

##### app.py 程序主入口

##### config.py 程序配置

##### requirements.txt 程序所使用的库

***

#### 主要API定义

> 弹幕大屏地址: /barrageDisplay 

###### 即打开粉丝弹幕大屏



#### 粉丝弹幕相关 （Barrage）->Modify Data: 2020-03-19

|       接口定义        | 请求方式 |          描述          |
| :-------------------: | :------: | :--------------------: |
| /api/barrage/display  |   GET    | 返回弹幕大屏用粉丝弹幕 |
| /api/barrage/standard |   GET    |    返回标准粉丝弹幕    |
|  /api/barrage/device  |   GET    |   返回设备用粉丝弹幕   |

