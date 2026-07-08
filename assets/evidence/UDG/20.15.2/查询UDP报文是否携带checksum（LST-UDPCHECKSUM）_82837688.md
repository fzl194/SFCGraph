# 查询UDP报文是否携带checksum（LST UDPCHECKSUM）

- [命令功能](#ZH-CN_CONCEPT_0182837688__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837688__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837688__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837688__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837688__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837688__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837688)

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询系统发送的UDP报文是否携带checksum。

#### [注意事项](#ZH-CN_CONCEPT_0182837688)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837688)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837688)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837688)

查询系统发送的UDP报文是否携带checksum：

```
LST UDPCHECKSUM:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
UDP Type     Checksum 开关

L2TP-CTRL    使能       
L2TP-DATA    不使能           
PFCP         使能          
(结果个数 = 3)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837688)

参见SET UDPCHECKSUM的参数说明。
