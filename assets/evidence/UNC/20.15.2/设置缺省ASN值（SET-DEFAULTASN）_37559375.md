# 设置缺省ASN值（SET DEFAULTASN）

- [命令功能](#ZH-CN_MMLREF_0000001137559375__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001137559375__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001137559375__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001137559375__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001137559375)

**适用NF：PGW-C、GGSN、SGW-C**

该命令用于配置SGSN/SGW-C对应的缺省ASN值及删除SGSN/SGW-C对应的缺省ASN值。

## [注意事项](#ZH-CN_MMLREF_0000001137559375)

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ASNVALUE | DEFAULTASN |
| --- | --- |
| UNSPECIFIEDASN | 0 |

#### [操作用户权限](#ZH-CN_MMLREF_0000001137559375)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001137559375)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ASNVALUE | 指定ASN值 | 可选必选说明：必选参数<br>参数含义：该参数用于控制是否指定ASN值。<br>数据来源：本端规划<br>取值范围：<br>- UNSPECIFIEDASN（不指定ASN值）<br>- SPECIFIEDASN（指定ASN值）<br>默认值：无。<br>配置原则：无 |
| DEFAULTASN | 缺省ASN | 可选必选说明：该参数在"ASNVALUE"配置为"SPECIFIEDASN"时为条件必选参数。<br>参数含义：该参数用于指定缺省ASN值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFAULTASN查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001137559375)

- 配置缺省ASN值为1000：
  ```
  SET DEFAULTASN:ASNVALUE=SPECIFIEDASN,DEFAULTASN=1000;
  ```
- 删除缺省ASN值：
  ```
  SET DEFAULTASN:ASNVALUE=UNSPECIFIEDASN;
  ```
