# 查询Diameter链路组（LST UPDIAMCONNGRP）

- [命令功能](#ZH-CN_CONCEPT_0000206145432690__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206145432690__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206145432690__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206145432690__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206145432690__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000206145432690__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206145432690)

**适用NF：UPF**

该命令用于查询所有Diameter链路组配置信息，或者查询指定名称、本端主机名或对端主机名的Diameter链路组配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0000206145432690)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206145432690)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206145432690)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONNGROUPNAME | Diameter链路组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCALHOSTNAME | 本端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的本端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMLOCINFO命令配置生成。 |
| PEERHOSTNAME | 对端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的对端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMETERAAA或ADD UPDRA命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0000206145432690)

查询diameter链路组swmconngrp的配置信息：

```
LST UPDIAMCONNGRP:CONNGROUPNAME="swmconngrp";
```

```

RETCODE = 0  操作成功
Diameter链路组
--------------
Diameter链路组名  =  swmconngrp
      本端主机名  =  swmlocalhost
      对端主机名  =  drahost
    Diameter应用  =  SWM
    链路选择模式  =  基于会话（Session-id）轮询
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000206145432690)

参见ADD UPDIAMCONNGRP的参数说明。
