---
id: UNC@20.15.2@MMLCommand@SET DEFAULTASN
type: MMLCommand
name: SET DEFAULTASN（设置缺省ASN值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DEFAULTASN
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- 缺省ASN管理
status: active
---

# SET DEFAULTASN（设置缺省ASN值）

## 功能

**适用NF：PGW-C、GGSN、SGW-C**

该命令用于配置SGSN/SGW-C对应的缺省ASN值及删除SGSN/SGW-C对应的缺省ASN值。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ASNVALUE | DEFAULTASN |
| --- | --- |
| UNSPECIFIEDASN | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ASNVALUE | 指定ASN值 | 可选必选说明：必选参数<br>参数含义：该参数用于控制是否指定ASN值。<br>数据来源：本端规划<br>取值范围：<br>- UNSPECIFIEDASN（不指定ASN值）<br>- SPECIFIEDASN（指定ASN值）<br>默认值：无。<br>配置原则：无 |
| DEFAULTASN | 缺省ASN | 可选必选说明：该参数在"ASNVALUE"配置为"SPECIFIEDASN"时为条件必选参数。<br>参数含义：该参数用于指定缺省ASN值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFAULTASN查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [缺省ASN值（DEFAULTASN）](configobject/UNC/20.15.2/DEFAULTASN.md)

## 使用实例

- 配置缺省ASN值为1000：
  ```
  SET DEFAULTASN:ASNVALUE=SPECIFIEDASN,DEFAULTASN=1000;
  ```
- 删除缺省ASN值：
  ```
  SET DEFAULTASN:ASNVALUE=UNSPECIFIEDASN;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置缺省ASN值（SET-DEFAULTASN）_37559375.md`
