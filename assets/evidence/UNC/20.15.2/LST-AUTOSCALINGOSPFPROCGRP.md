# 查询OSPF进程组自动化配置模板（LST AUTOSCALINGOSPFPROCGRP）

- [命令功能](#ZH-CN_CONCEPT_0000001549960986__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549960986__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549960986__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549960986__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549960986__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001549960986__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549960986)

该命令用于查询OSPF进程组自动化配置模板。

#### [注意事项](#ZH-CN_CONCEPT_0000001549960986)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549960986)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549960986)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | OSPF进程组ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定OSPF进程组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～16。<br>默认值：无 |
| VERSION | OSPF版本号 | 可选必选说明：可选参数<br>参数含义：该参数用来表示自动化配置模板中OSPF版本号。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OSPFv2：OSPFv2。<br>- OSPFv3：OSPFv3。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549960986)

查询OSPF进程组ID为1的自动化配置模板：

```
LST AUTOSCALINGOSPFPROCGRP:GROUPID=1,VERSION=OSPFv2;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                          OSPF进程组ID   =  1
                            OSPF版本号   =  OSPFv2
                        OSPF起始进程ID   =  1000
                            OSPF区域ID   =  10.10.10.10
                            OSPF实例ID   =  0
                              OSPF开销   =  10
           邻居发送Hello包时间间隔（s）  =  11
                    邻居失效的时间（s）  =  44
                           BFD模板名称   =  BFD4OSPF1
                          OSPF区域类型   =  普通区域
                  是否配置环回口地址池   =  FALSE
                  环回口地址池起始地址   =  NULL
                  环回口地址池结束地址   =  NULL
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001549960986)

参见ADD AUTOSCALINGOSPFPROCGRP的参数说明。
