# 删除PCC组业务属性绑定（RMV SRVPBINDPCCPG）

- [命令功能](#ZH-CN_CONCEPT_0182837613__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837613__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837613__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837613__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837613__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837613)

**适用NF：PGW-U、UPF**

![](删除PCC组业务属性绑定（RMV SRVPBINDPCCPG）_82837613.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定PCC组与指定或所有业务属性间的绑定关系，可能会导致计费或控制策略发生变化，请谨慎使用。

此命令用于删除PCC策略组业务属性绑定组合。

支持删除指定PCCPOLICYGRPNM或所有的PCC策略组业务属性绑定组合。

#### [注意事项](#ZH-CN_CONCEPT_0182837613)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837613)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837613)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：必选参数<br>参数含义：设置PCC策略组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SRVPROPNAME | 业务属性名称 | 可选必选说明：可选参数<br>参数含义：设置业务属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837613)

删除TestPccPolicyGrpName的PCC策略组的PCC策略组业务属性绑定组合，即删除所有非默认组合：

```
RMV SRVPBINDPCCPG:PCCPOLICYGRPNM ="TestPccPolicyGrpName";
```
