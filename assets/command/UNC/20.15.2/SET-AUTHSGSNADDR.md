---
id: UNC@20.15.2@MMLCommand@SET AUTHSGSNADDR
type: MMLCommand
name: SET AUTHSGSNADDR（设置向AAA鉴权服务器发送消息中携带的地址信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AUTHSGSNADDR
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 鉴权管理
- 服务节点地址信息
status: active
---

# SET AUTHSGSNADDR（设置向AAA鉴权服务器发送消息中携带的地址信息）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用来控制SPW-C和PGW-C合一形态向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| AUTHSGSNADDR |
| --- |
| PAIF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AUTHSGSNADDR | 3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元中携带的地址信息 | 可选必选说明：可选参数<br>参数含义：SPW-C和PGW-C合一形态向AAA鉴权服务器发送消息中携带的3GPP-SGSN-Address或者3GPP-SGSN-IPv6–Address信元携带的地址信息。<br>数据来源：本端规划<br>取值范围：<br>- “PAIF（Pa接口）”：3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元填充Pa接口地址<br>- “S5_SIF（S5-s接口）”：3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元填充S5-sif接口地址<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AUTHSGSNADDR查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTHSGSNADDR]] · 向AAA鉴权服务器发送消息中携带的地址信息（AUTHSGSNADDR）

## 使用实例

设置3GPP-SGSN-Address或者3GPP-SGSN-IPv6-Address信元填充Pa接口地址：

```
SET AUTHSGSNADDR: AUTHSGSNADDR=PAIF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置向AAA鉴权服务器发送消息中携带的地址信息（SET-AUTHSGSNADDR）_96243089.md`
