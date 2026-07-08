# 删除VXLAN隧道组绑定Rule（RMV VXLANBINDRULE）

- [命令功能](#ZH-CN_CONCEPT_0000202192033107__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202192033107__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202192033107__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202192033107__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202192033107__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202192033107)

**适用NF：PGW-U、UPF**

![](删除VXLAN隧道组绑定Rule（RMV VXLANBINDRULE）_92033107.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除配置会导致匹配到对应规则的数据报文无法转发给MEP。

该命令用于删除VXLAN隧道组与Rule的绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0000202192033107)

- 该命令执行后立即生效。
- 执行该命令时，删除Rule绑定的Vxlan组会改变业务流的转发流程,匹配到该rule的数据报文由转发给MEP修改为直接路由转发或转发到新的MEP。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202192033107)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202192033107)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数必须已经通过ADD RULE命令配置。<br>- ADD RULE命令中POLICYTYPE为WORKER，WORKERNAME为traffic-fd。其他类型的规则不能绑定VXLAN组。 |

#### [使用实例](#ZH-CN_CONCEPT_0000202192033107)

删除所有VXLAN隧道组与testrule的绑定关系：

```
RMV VXLANBINDRULE: RULENAME="rule";
```
