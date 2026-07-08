---
id: UDG@20.15.2@MMLCommand@LST ANTISPOOFINGTHD
type: MMLCommand
name: LST ANTISPOOFINGTHD（查询攻击用户去活报文的阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ANTISPOOFINGTHD
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- IP Spoofing攻击防护
- 攻击用户去活的报文一分钟内个数门限
status: active
---

# LST ANTISPOOFINGTHD（查询攻击用户去活报文的阈值）

## 功能

**适用NF：UPF**

该参数用于查询攻击用户去活报文的阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [攻击用户去活报文的阈值（ANTISPOOFINGTHD）](configobject/UDG/20.15.2/ANTISPOOFINGTHD.md)

## 使用实例

使用LST ANTISPOOFINGTHD命令查询当前配置的ANTISPOOFING对攻击用户使用的阈值：

```
LST ANTISPOOFINGTHD:;
```

```

RETCODE = 0  Operation succeeded

AntiSpoofingThd Value
---------------------
Anti-spoofing Threshold for Subscriber Deactivation  =  100
(Number of results = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询攻击用户去活报文的阈值（LST-ANTISPOOFINGTHD）_16615233.md`
