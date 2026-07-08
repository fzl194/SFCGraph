# 查询Diameter链路组（LST DIAMCONNGRP）

- [命令功能](#ZH-CN_CONCEPT_0209897264__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897264__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897264__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897264__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897264__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897264__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897264)

**适用NF：PGW-C、SMF**

该命令用于查询所有Diameter链路组配置信息，或者查询指定名称、本端主机名或对端主机名的Diameter链路组配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0209897264)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897264)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897264)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONNGROUPNAME | Diameter链路组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCALHOSTNAME | 本端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的本端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD DIAMLOCINFO命令配置生成。 |
| PEERHOSTNAME | 对端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的对端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PCRF、ADD OCS、ADD DIAMETERAAA或ADD DRA命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897264)

查询diameter链路组gxconngrp的配置信息：

```
LST DIAMCONNGRP:CONNGROUPNAME="gxconngrp";
```

```

RETCODE = 0  操作成功

Diameter链路组
--------------
Diameter链路组名  =  gxconngrp
      本端主机名  =  gxlocalhost
      对端主机名  =  pcrfhost
    Diameter应用  =  Gx应用
    链路选择模式  =  基于会话（Session-id）轮询
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897264)

参见ADD DIAMCONNGRP的参数说明。
