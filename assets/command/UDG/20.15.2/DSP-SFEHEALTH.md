---
id: UDG@20.15.2@MMLCommand@DSP SFEHEALTH
type: MMLCommand
name: DSP SFEHEALTH（显示SFE健康状况）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFEHEALTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE健康状态信息
status: active
---

# DSP SFEHEALTH（显示SFE健康状况）

## 功能

该命令用于显示SFE健康信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [SFE健康状况（SFEHEALTH）](configobject/UDG/20.15.2/SFEHEALTH.md)

## 使用实例

查询SFE初始化、回显信息：

```
DSP SFEHEALTH:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
类型                状态/是否使能
Thread                 false                   
Queue Alert Info       false                   
Buffer                 false                   
Memory                 false                   
MSS                    normal                  
Channel                normal                  
Queue Init Info        normal                  
FB                     normal                  
WorkInfo               normal                  
SFE                    normal                  
Queue num              79                      
Arp                    false                   
Fast Ping              true                    
GRE KA                 false                   
ND                     true
SingleFwdCore          true                    
SfeState               true                    
SFECoreNum             1                       
SFEFwdThreadDeadCnt    0                       
IpuMemResource(G)      16                      
HashMode               0                       
Channel Mode           Single-in And Single-Out
(结果个数 = 21)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示SFE健康状况（DSP-SFEHEALTH）_00841757.md`
