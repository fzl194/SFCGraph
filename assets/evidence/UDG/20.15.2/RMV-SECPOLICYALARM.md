# 删除安全策略告警配置（RMV SECPOLICYALARM）

- [命令功能](#ZH-CN_CONCEPT_0000001600600269__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600600269__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600600269__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600600269__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600600269__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600600269)

该命令用来删除上送CPU报文产生告警参数的配置。

#### [注意事项](#ZH-CN_CONCEPT_0000001600600269)

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600600269)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600600269)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：安全策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：策略类型，如应用层联动、TCP/IP防攻击、黑白名单等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- TotalPkt：所有报文。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- Index：索引策略。<br>- UserFlow：用户自定义流策略。<br>- APP：APP应用策略。<br>- Urpf：URPF策略。<br>- WhiteListV6：IPv6白名单。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Index” 或 “UserFlow”时为必选参数。<br>参数含义：安全策略类型编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600600269)

删除上送CPU的各种报文产生告警参数的配置：

```
RMV SECPOLICYALARM:SECPOLICYID=1,SECPOLICYTYPE=WhiteList;
```
