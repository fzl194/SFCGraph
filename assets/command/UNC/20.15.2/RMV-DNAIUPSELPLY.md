---
id: UNC@20.15.2@MMLCommand@RMV DNAIUPSELPLY
type: MMLCommand
name: RMV DNAIUPSELPLY（删除DNAI粒度的UPF选择策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNAIUPSELPLY
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- DNAI粒度的UPF选择策略
status: active
---

# RMV DNAIUPSELPLY（删除DNAI粒度的UPF选择策略）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除DNAI粒度的UPF选择策略。

## 注意事项

- 该命令执行后立即生效。

- 删除本配置后，在此DNAI内的UPF选择策略由更粗粒度的配置(UPSELECTFLAG、APNUPSEPLY)控制。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNAIUPSELPLY]] · DNAI粒度的UPF选择策略（DNAIUPSELPLY）

## 使用实例

删除指定DNAI的UPF选择策略，DNAI名称为huawei.com。

```
RMV DNAIUPSELPLY:DNAI="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNAI粒度的UPF选择策略（RMV-DNAIUPSELPLY）_18037981.md`
