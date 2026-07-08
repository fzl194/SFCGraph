# 删除Diameter路由域名信息（RMV UPDIAMRTREALM）

- [命令功能](#ZH-CN_CONCEPT_0000206145432706__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206145432706__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206145432706__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206145432706__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206145432706__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206145432706)

**适用NF：UPF**

![](删除Diameter路由域名信息（RMV UPDIAMRTREALM）_45432706.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会删除Diameter路由域名信息，可能会影响DRA的选择。

该命令用于删除指定的Diameter路由的配置信息以及指定的Diameter路由的所有下一跳。

#### [注意事项](#ZH-CN_CONCEPT_0000206145432706)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206145432706)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206145432706)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206145432706)

删除Swm应用在realm名为“example.com”的Diameter路由：

```
RMV UPDIAMRTREALM:REALMNAME="example.com",APPLICATION=SWM;
```
