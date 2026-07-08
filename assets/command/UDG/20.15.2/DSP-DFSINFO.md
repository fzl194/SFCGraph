---
id: UDG@20.15.2@MMLCommand@DSP DFSINFO
type: MMLCommand
name: DSP DFSINFO（查询DFS集群信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DFSINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- CoreMind操作维护命令
- DFS信息维护
status: active
---

# DSP DFSINFO（查询DFS集群信息）

## 功能

该命令用于查询分布式文件系统集群信息。

> **说明**
> 无

## 参数

无。

## 操作的配置对象

- [DFS集群信息（DFSINFO）](configobject/UDG/20.15.2/DFSINFO.md)

## 使用实例

查询hofs集群的基本信息。

```
%%DSP DFSINFO:;%% 
RETCODE = 0  操作成功
  
分布式文件系统信息 
------------------        
          应用ID  =  0       
         OSD数量  =  0      
        对象数量  =  9599
      读成功次数  =  0    
      写成功次数  =  0      
        失败次数  =  0    
      对象总大小  =  4872
    PV总大小(MB)  =  120371.5625  
PV已使用大小(MB)  =  38366.0664      
     PV使用率(%)  =  36.9902     
    Inode总数(B)  =  7864320 
Inode使用数量(B)  =  122422   
  Inode使用率(%)  =  1.5567 
(结果个数 = 1) 
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DFS集群信息（DSP-DFSINFO）_30144141.md`
