---
id: UNC@20.15.2@MMLCommand@RMV PNFDNAI
type: MMLCommand
name: RMV PNFDNAI（删除对端NF的DNAI信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFDNAI
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端DNAI信息管理
status: active
---

# RMV PNFDNAI（删除对端NF的DNAI信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、PGW-C**

该命令用于删除本地配置的对端NF实例支持的数据网络接入标识信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNAI的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFDNAI]] · 对端NF的DNAI信息（PNFDNAI）

## 使用实例

删除对端NF的DNAI信息。

```
RMV PNFDNAI: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF的DNAI信息（RMV-PNFDNAI）_09652252.md`
