# 删除ICAP服务器组（RMV ICAPSVRGRP）

- [命令功能](#ZH-CN_CONCEPT_0000203432582493__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203432582493__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203432582493__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203432582493__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203432582493__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203432582493)

**适用NF：PGW-U、UPF**

![](删除ICAP服务器组（RMV ICAPSVRGRP）_32582493.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令可能导致无可用的ICAP服务器。

该命令用于删除指定名称的ICAP Server Group实例。

#### [注意事项](#ZH-CN_CONCEPT_0000203432582493)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203432582493)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203432582493)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203432582493)

删除指定名称为isg1的ICAP Server Group实例：

```
RMV ICAPSVRGRP: ICAPSVRGRPNAME="isg1";
```
