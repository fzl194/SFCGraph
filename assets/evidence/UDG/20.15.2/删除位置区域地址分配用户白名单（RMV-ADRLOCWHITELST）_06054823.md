# 删除位置区域地址分配用户白名单（RMV ADRLOCWHITELST）

- [命令功能](#ZH-CN_CONCEPT_0206054823__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0206054823__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0206054823__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0206054823__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0206054823__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0206054823)

**适用NF：PGW-U、UPF**

![](删除位置区域地址分配用户白名单（RMV ADRLOCWHITELST）_06054823.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会改变指定用户的地址分配属性，可能会导致用户激活失败。

该命令用于删除按照区域地址分配用户白名单。

#### [注意事项](#ZH-CN_CONCEPT_0206054823)

该命令执行后只对新激活用户生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0206054823)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0206054823)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSISDN | MSISDN | 可选必选说明：必选参数<br>参数含义：用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0206054823)

删除用户MSISDN为123456的区域地址分配白名单：

```
RMV ADRLOCWHITELST: MSISDN="123456";
```
