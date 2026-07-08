# 批量设置绑定域信息（SET MMLCFGDOMAIN）

- [命令功能](#ZH-CN_CONCEPT_0000201756064769__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201756064769__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201756064769__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201756064769__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201756064769__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201756064769)

**适用NF：SGW-U、PGW-U、UPF**

![](批量设置绑定域信息（SET MMLCFGDOMAIN）_56064769.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行本命令后将批量修改配置的域信息，且无法回退。

本命令用于批量设置或修改网元配置的域信息。

#### [注意事项](#ZH-CN_CONCEPT_0000201756064769)

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CMDNAME | NEWDOMAINNAME | OLDDOMAINNAME |
| --- | --- | --- | --- |
| 初始值 | ADD APN | 0x0b4c0dbb | 0x0b4c0b9c |
| 初始值 | SET ApnSoftPara | 0x0b580dd2 | 0x0b584718 |
| 初始值 | SET ApnDLBufTime | 0x0b580dd5 | 0x0b580c04 |
| 初始值 | SET ApnAddressAttr | 0x0b580dd6 | 0x0b580ba6 |

#### [操作用户权限](#ZH-CN_CONCEPT_0000201756064769)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201756064769)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMDNAME | 公共配置命令名称 | 可选必选说明：必选参数<br>参数含义：公共配置命令名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| NEWDOMAINNAME | 域名称 | 可选必选说明：必选参数<br>参数含义：New Domain Name。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| OLDDOMAINNAME | 原始配置域名称 | 可选必选说明：可选参数<br>参数含义：原始配置域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 原始配置域名称可通过LST PUBCFGDOMAIN命令查询。 |

#### [使用实例](#ZH-CN_CONCEPT_0000201756064769)

将ADD APN所配的原始域名为domain_b的配置的域信息批量修改为domain_a：

```
SET MMLCFGDOMAIN: CMDNAME="ADD APN", NEWDOMAINNAME="domain_a", OLDDOMAINNAME="domain_b";
```
