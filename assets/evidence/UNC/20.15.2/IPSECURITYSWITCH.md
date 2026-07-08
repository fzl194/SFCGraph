# 设置IP选项安全开关（SET IPSECURITYSWITCH）

- [命令功能](#ZH-CN_CONCEPT_0000001193752960__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001193752960__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001193752960__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001193752960__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001193752960__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001193752960)

该命令用于设置CSLB中IP选项安全开关配置。

#### [注意事项](#ZH-CN_CONCEPT_0000001193752960)

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：
  | IPV4OPTION | IPV6EXTENSION |
  | --- | --- |
  | SW_DISABLE | SW_DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0000001193752960)

G_1，管理员级别命令组；G_2，操作员级别命令组；

#### [参数说明](#ZH-CN_CONCEPT_0000001193752960)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPV4OPTION | IPv4选项安全配置开关 | 可选必选说明：必选参数<br>参数含义：<br>该参数表示使能或去使能<br>IPv4<br>选项安全配置<br>。<br>数据来源：本端规划<br>取值范围：枚举类型:<br>- SW_ENABLE(IP安全开关开启)：使能IPv4选项安全开关；<br>- SW_DISABLE(IP安全开关关闭)：去使能IPv4选项安全开关；<br>默认值：无 |
| IPV6EXTENSION | IPv6扩展头选项安全配置开关 | 可选必选说明：必选参数<br>参数含义：<br>该参数表示使能或去使能<br>IPv6<br>扩展头选项安全配置<br>。<br>数据来源：本端规划<br>取值范围：枚举类型:<br>- SW_ENABLE(IP安全开关开启)：使能IPv6扩展头选项安全开关；<br>- SW_DISABLE(IP安全开关关闭)：去使能IPv6扩展头选项安全开关；<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001193752960)

设置针对带有IPv4选项的报文和带有IPv6扩展头选项的报文，执行丢弃处理，命令如下：

```
SET IPSECURITYSWITCH: IPV4OPTION=SW_ENABLE, IPV6EXTENSION=SW_ENABLE;
```
