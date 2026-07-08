# 设置NF锁定开关（LCK NF）

- [命令功能](#ZH-CN_CONCEPT_0182837078__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837078__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837078__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837078__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837078__1.3.5.1)
- [参考信息](#ZH-CN_CONCEPT_0182837078__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837078)

**适用NF：SGW-U、PGW-U、UPF**

![](设置NF锁定开关（LCK NF）_82837078.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会改变NF的锁定状态，如果配置为锁定，会导致用户接入失败。

该命令用来设置NF的锁定状态，处于锁定状态中时，该NF无法正常接入业务。

#### [注意事项](#ZH-CN_CONCEPT_0182837078)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837078)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837078)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCKSWITCH | NF锁定状态开关 | 可选必选说明：必选参数<br>参数含义：该参数使能时，NF为锁定状态，该参数为不使能时，NF为解锁状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837078)

配置NF为锁定状态：

```
LCK NF: LOCKSWITCH=ENABLE;
```

#### [参考信息](#ZH-CN_CONCEPT_0182837078)

1、UPF通过LCK NF命令修改锁定状态后，通过PFCP Association Update Request消息向SMF上报锁定状态，收到SMF回复的PFCP Association Update Response消息后确认锁定状态上报成功。
