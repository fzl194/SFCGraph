# 添加基于位置区+PLMN分配地址的开关（ADD IPALLOCBYPLMNLOCSW）

- [命令功能](#ZH-CN_CONCEPT_0000202737484063__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202737484063__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202737484063__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202737484063__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202737484063__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202737484063)

**适用NF：PGW-U、UPF**

该命令用于配置基于位置区+PLMN分配地址开关。

#### [注意事项](#ZH-CN_CONCEPT_0000202737484063)

- 该命令执行后立即生效。
- 该命令最大记录数为30000。
- 在位置区组+PLMN映射地址池存在的情况下，若对应 ‘基于位置区组+PLMN分配地址开关-ADD IPALLOCBYPLMNLOCSW’ 配置为使能： 漫游用户需严格基于位置区组+PLMN匹配地址池组，即仅能匹配中位置区组+PLMN映射地址池。 本地用户优先匹配位置区组+PLMN映射址池组；若匹配不中，二次匹配单独基于位置区组映射地址池。
- 在位置区组+PLMN映射地址池存在的情况下，若对应 ‘基于位置区组+PLMN分配地址开关-ADD IPALLOCBYPLMNLOCSW’ 不存在或者配置为INHERIT状态时，地址分配流程受 ‘基于位置区组分配地址的开关-SET IPALLOCBYLOCSW’ 的控制。
- 在位置区组+PLMN映射地址池不存在的情况下，地址分配流程受 ‘基于位置区组分配地址的开关-SET IPALLOCBYLOCSW’ 的控制，不受 ‘基于位置区组+PLMN分配地址开关-ADD IPALLOCBYPLMNLOCSW’ 的控制。
- 当全局地址分配规则SET IPALLOCRULE配置了按照位置区映射的地址范围分配地址的规则时，‘基于位置区组+PLMN分配地址开关-ADD IPALLOCBYPLMNLOCSW’ 的配置才生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202737484063)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202737484063)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCATIONGRPTYPE | 位置区组类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区组类型。<br>数据来源：本端规划<br>取值范围：枚举类型。只能选取一个选项。<br>- LAC：LAC。<br>- TAC：TAC。<br>默认值：无<br>配置原则：无 |
| LOCATIONGRPNAME | 位置区组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该位置区组名称必须通过ADD LACGROUP或ADD TACGROUP命令配置过。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网络号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网络号。<br>数据来源：全网规划<br>取值范围：字符串类型，可为2或3位数字，00~99或000~999。<br>默认值：无<br>配置原则：MNC有效配置长度为两位或三位。配置长度取决于PFCP Session Establishment Request消息ULI信元中携带的MNC有效值的长度，两位有效数字即配置两位，三位有效数字需配置三位。不受ADD MNCLEN影响。 |
| SWITCH | IPv4 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于位置区分配地址的IPv4开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |
| IPV6SWITCH | IPv6 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于位置区分配地址的IPv6开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000202737484063)

在位置区组tacgrp1+PLMN 460011映射地址池存在的情况下，允许激活携带信源tac属于tacgrp1，且PLMN为460011的用户基于位置区分配IPV4地址；不允许该用户基于位置区分配IPV6地址：

```
ADD IPALLOCBYPLMNLOCSW: LOCATIONGRPTYPE=TAC, LOCATIONGRPNAME="tacgrp1", MCC="460", MNC="011", SWITCH=ENABLE, IPV6SWITCH=DISABLE;
```
