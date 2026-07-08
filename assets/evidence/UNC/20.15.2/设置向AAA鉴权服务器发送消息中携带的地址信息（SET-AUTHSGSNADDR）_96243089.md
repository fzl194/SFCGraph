# 设置向AAA鉴权服务器发送消息中携带的地址信息（SET AUTHSGSNADDR）

- [命令功能](#ZH-CN_MMLREF_0296243089__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296243089__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296243089__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296243089__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0296243089)

**适用NF：PGW-C、SGW-C**

该命令用来控制SPW-C和PGW-C合一形态向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元。

## [注意事项](#ZH-CN_MMLREF_0296243089)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| AUTHSGSNADDR |
| --- |
| PAIF |

#### [操作用户权限](#ZH-CN_MMLREF_0296243089)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0296243089)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AUTHSGSNADDR | 3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元中携带的地址信息 | 可选必选说明：可选参数<br>参数含义：SPW-C和PGW-C合一形态向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6–Address信元携带的地址信息。<br>数据来源：本端规划<br>取值范围：<br>- “PAIF（Pa接口）”：3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元填充Pa接口地址<br>- “S5_SIF（S5-s接口）”：3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元填充S5-sif接口地址<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AUTHSGSNADDR查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0296243089)

设置3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元填充Pa接口地址：

```
SET AUTHSGSNADDR: AUTHSGSNADDR=PAIF;
```
