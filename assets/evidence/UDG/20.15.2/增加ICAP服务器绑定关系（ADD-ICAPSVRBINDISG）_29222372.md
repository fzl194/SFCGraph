# 增加ICAP服务器绑定关系（ADD ICAPSVRBINDISG）

- [命令功能](#ZH-CN_CONCEPT_0000203229222372__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203229222372__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203229222372__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203229222372__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203229222372__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203229222372)

**适用NF：PGW-U、UPF**

该命令用于向ICAP Server Group实例中绑定ICAP Server信息。

#### [注意事项](#ZH-CN_CONCEPT_0000203229222372)

- 该命令执行后立即生效。
- 该命令最大记录数为300。
- 要配置此命令，需要首先配置ICAP Server和ICAP Server Group。
- 一个ICAP Server Group实例中最多可以配置10个ICAP Server。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203229222372)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203229222372)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD ICAPSVRGRP命令配置生成。 |
| ICAPSERVERNAME | ICAP服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server的服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD ICAPSERVER命令配置生成。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203229222372)

增加ICAP Server服务器绑定信息：

```
ADD ICAPSVRBINDISG:ICAPSVRGRPNAME="isg1",ICAPSERVERNAME="is1";
```
