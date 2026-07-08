---
id: UNC@20.15.2@MMLCommand@MOD IFIPV4UNNUMIPSEC
type: MMLCommand
name: MOD IFIPV4UNNUMIPSEC（修改接口IPv4借用地址）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IFIPV4UNNUMIPSEC
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- IPv4借用地址
status: active
---

# MOD IFIPV4UNNUMIPSEC（修改接口IPv4借用地址）

## 功能

该命令用于修改接口的借用IPv4地址。

## 注意事项

- 该命令执行后立即生效。

- 该命令只支持配置Tunnel口借用的IPv4地址。
- 被借接口可以通过[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)命令查询到。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：<br>请使用<br>[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)<br>命令查看可用接口。 |
| UNNUMIFNAME | 被借用接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定被借用的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IFIPV4UNNUMIPSEC]] · 接口IPv4借用地址（IFIPV4UNNUMIPSEC）

## 使用实例

修改tunnel口借用的IPv4地址：

```
MOD IFIPV4UNNUMIPSEC:IFNAME="tunnel1",UNNUMIFNAME="loopback1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改接口IPv4借用地址（MOD-IFIPV4UNNUMIPSEC）_80432532.md`
