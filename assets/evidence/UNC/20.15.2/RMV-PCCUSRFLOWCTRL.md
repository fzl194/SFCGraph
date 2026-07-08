# 删除流控策略（RMV PCCUSRFLOWCTRL）

- [命令功能](#ZH-CN_MMLREF_0211712040__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0211712040__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0211712040__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0211712040__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0211712040)

**适用NF：SMF**

该命令用于删除流控策略。

## [注意事项](#ZH-CN_MMLREF_0211712040)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0211712040)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0211712040)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRFLOWCTRLNAME | Update流控策略名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Update流控策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0211712040)

删除流控策略flowctr1。

```
RMV PCCUSRFLOWCTRL: USRFLOWCTRLNAME="flowctr1";
```
