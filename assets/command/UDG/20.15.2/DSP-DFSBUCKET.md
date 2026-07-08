---
id: UDG@20.15.2@MMLCommand@DSP DFSBUCKET
type: MMLCommand
name: DSP DFSBUCKET（查询DFS桶信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DFSBUCKET
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- CoreMind操作维护命令
- DFS信息维护
status: active
---

# DSP DFSBUCKET（查询DFS桶信息）

## 功能

该命令用于查询当前环境中桶的信息。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BUCKETNAME | 桶名称 | 可选必选说明：可选参数。<br>参数含义：桶名称。<br>取值范围：字符串类型，输入长度范围为0~100。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DFSBUCKET]] · DFS桶信息（DFSBUCKET）

## 使用实例

1、查询model桶的基本信息。

```
%%DSP DFSBUCKET: BUCKETNAME="model";
%% RETCODE = 0  操作成功  

存储桶信息 
----------       
             应用ID  =  0      
             桶名称  =  model      
       总大小（MB）  =  20480   
   已使用空间（MB）  =  93.693     
     剩余空间（MB）  =  20386.307 
单个文件大小限额(MB) =  100     
           备份数量  =  2 
(结果个数 = 1)  

---    END 
```

2、查询所有桶的基本信息

```
%%DSP DFSBUCKET:;%% 
RETCODE = 0  操作成功
  
存储桶信息 
---------- 
应用ID  桶名称   总大小（MB）  已使用空间（MB）  剩余空间（MB）    单个文件大小限额（MB）  备份数量    
0       dataset  20480         0                 20480             100                      2         
0       model    20480         93.693            20386.307         100                      2          
0       sample   20480         2.0031            20477.9969        100                      2          
(结果个数 = 3)  

---    END 
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DFSBUCKET.md`
