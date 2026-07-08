# 设置SGW APN计费方式（SET SGWAPNCHGMETH）

- [命令功能](#ZH-CN_CONCEPT_0209896992__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896992__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896992__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896992__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896992__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896992)

**适用NF：SGW-C**

![](设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改配置会影响新激活的SGW用户是否产生S-GW话单，可能导致用户无法计费。

SET SGWAPNCHGMETH命令用来控制APN下的用户是否产生S-GW话单。

#### [注意事项](#ZH-CN_CONCEPT_0209896992)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- 参数APN在表APN中必须存在才能配置成功。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | Offline |
| --- | --- |
| 初始值 | INHERIT |

#### [操作用户权限](#ZH-CN_CONCEPT_0209896992)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896992)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等。<br>默认值：无<br>配置原则：无 |
| OFFLINE | APN离线计费开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置APN下的用户是否产生S-GW离线话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：禁止。<br>- ENABLE：允许。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：<br>- ENABLE：用户执行离线计费功能，生成SGW离线话单。<br>- DISABLE：用户不执行离线计费功能。<br>- INHERIT：继承基于计费属性的配置。 |

#### [使用实例](#ZH-CN_CONCEPT_0209896992)

修改APN实例aa用户不产生S-GW话单：

```
SET SGWAPNCHGMETH: APN="aa",OFFLINE=DISABLE;
```
