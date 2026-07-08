---
id: UNC@20.15.2@MMLCommand@SET NSSFSUBTIMER
type: MMLCommand
name: SET NSSFSUBTIMER（设置订阅时长）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NSSFSUBTIMER
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF订阅时长管理
status: active
---

# SET NSSFSUBTIMER（设置订阅时长）

## 功能

**适用NF：NSSF**

该命令用于设置AMF订阅NSSF切片可用性服务的有效期时长。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NFTYPE | SUBVALIDTIMER |
| --- | --- |
| AMF | 86400 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于描述网元类型。<br>数据来源：全网规划<br>取值范围：<br>- AMF（接入和移动性管理网络功能）<br>默认值：无。<br>配置原则：无 |
| SUBVALIDTIMER | 订阅有效时长(s) | 可选必选说明：必选参数<br>参数含义：该参数用于描述订阅的有效时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~9223372036854775807，单位是秒。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFSUBTIMER]] · 订阅时长（NSSFSUBTIMER）

## 使用实例

假如运营商认为AMF订阅切片可用性服务时长的初始设置值过大，希望将AMF的订阅时长配置为86400秒，执行下列命令。

```
SET NSSFSUBTIMER:NFTYPE=AMF, SUBVALIDTIMER=86400;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置订阅时长（SET-NSSFSUBTIMER）_09653815.md`
