---
id: UNC@20.15.2@MMLCommand@SET GLBIPV6INFID
type: MMLCommand
name: SET GLBIPV6INFID（设置整机IPv6接口ID配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GLBIPV6INFID
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- IPv6接口标识管理
- 全局IPv6接口标识管理
status: active
---

# SET GLBIPV6INFID（设置整机IPv6接口ID配置）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于控制为用户分配IPv6地址时，是否开启IMSI作为用户的IPv6地址Interface ID功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| IMSI |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 配置IMSI作为IPv6 Interface ID | 可选必选说明：必选参数<br>参数含义：该参数用于控制开启和关闭IMSI作为用户的IPv6地址Interface ID功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBIPV6INFID]] · 整机IPv6接口ID配置（GLBIPV6INFID）

## 使用实例

配置IMSI作为用户的IPv6地址Interface ID功能使能：

```
SET GLBIPV6INFID: IMSI=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-GLBIPV6INFID.md`
