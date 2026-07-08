# 显示SFE健康状况（DSP SFEHEALTH）

- [命令功能](#ZH-CN_CONCEPT_0000001600841757__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600841757__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600841757__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600841757__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600841757__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600841757__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600841757)

该命令用于显示SFE健康信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600841757)

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600841757)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600841757)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600841757)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600841757)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 类型 | 该参数用于显示被检项目类型名称，包含如下三种类型：<br>- 告警检查类型信息：Thread，Queue，Buffer，Memory。<br>- 初始化类型信息：MSS，Channel，Queue，FB，WorkInfo，SFE，Queue num。<br>- 应答类型信息：ARP，Fast Ping，GRE KA，ND。 |
| 状态/是否使能 | 用于说明当前状态是否正常或是否使能。 |
