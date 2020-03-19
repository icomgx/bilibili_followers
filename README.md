# bilibili_followers
## bilibili粉丝系统(粉丝关注弹幕，粉丝数，外接API服务，包括以后的BI Cube（B站魔方）服务等等...) 
## B站主页 https://space.bilibili.com/23106193 有想法和建议欢迎私信我
## 开发工具：pycharm 环境：Anaconda3（python 3.7.4）  
## 使用库（暂时）： Flask，requests  

## 目录结构：
### d2ta/ 为数据库存放目录  
### main/ 各个功能模块存放目录    
##### /b2il.py B站主要功能模块    
##### /b2rrage.py 弹幕功能功能模块   
##### /controller.py 主控制器模块  
##### /d2evice.py 设备使用功能模块   
##### /e2xternal.py 外部API功能模块
##### /error.py 错误信息功能模块 
##### /k2ey.py 密钥功能模块    
##### /models.py 数据库操作功能模块   
### static/ 静态资源存放目录    
### app.py 程序主入口    
### config.py 程序配置  
### requirements.txt 程序所使用的库  
## 2020-03-19： 
### （1）重新构建控制器
### （2）基本功能接口完成，尚未写入功能
## 2020-03-04： 
### （1）项目建立
### （2）基础构建完成