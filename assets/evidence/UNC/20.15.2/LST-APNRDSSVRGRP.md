# 查询APN Radius服务器组（LST APNRDSSVRGRP）

- [命令功能](#ZH-CN_CONCEPT_0209896738__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896738__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896738__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896738__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896738__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896738__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896738)

**适用NF：PGW-C、SMF**

LST APNRDSSVRGRP命令是用来查询指定APN实例下绑定RADIUS服务器组。

#### [注意事项](#ZH-CN_CONCEPT_0209896738)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896738)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896738)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896738)

查询APN Radius服务器组，APN为apntest，命令为：

```
LST APNRDSSVRGRP:APN="apntest";
```

```

RETCODE = 0  操作成功

APN Radius服务器组
----------------------
                   APN名称  =  apntest
   RADIUS Server Group名称  =  rgtest
抄送Interim-Update Request  =  允许
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896738)

参见ADD APNRDSSVRGRP的参数说明。
