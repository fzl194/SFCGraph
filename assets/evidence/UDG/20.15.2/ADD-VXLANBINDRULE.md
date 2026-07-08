# 新增VXLAN隧道组绑定Rule（ADD VXLANBINDRULE）

- [命令功能](#ZH-CN_CONCEPT_0000202192513331__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202192513331__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202192513331__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202192513331__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202192513331__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202192513331)

**适用NF：PGW-U、UPF**

该命令用于配置VXLAN隧道组与Rule的绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0000202192513331)

- 该命令最大记录数为8000。
- 执行该命令时，新增Rule绑定的Vxlan组会改变业务流的转发流程,匹配到该rule的数据报文会转发到MEP。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202192513331)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202192513331)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数必须已经通过ADD RULE命令配置。<br>- ADD RULE命令中POLICYTYPE为WORKER，WORKERNAME为traffic-fd。其他类型的规则不能绑定VXLAN组。 |
| VXLANGRPNAME | VXLAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数配置Vxlan组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数必须已经通过ADD VXLANGRP命令配置。 |

#### [使用实例](#ZH-CN_CONCEPT_0000202192513331)

配置VXLAN隧道组与Rule的绑定关系，执行如下命令：

```
ADD VXLANBINDRULE: RULENAME="rule", VXLANGRPNAME="vxlangrp";
```
