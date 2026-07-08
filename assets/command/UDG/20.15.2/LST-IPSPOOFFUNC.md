---
id: UDG@20.15.2@MMLCommand@LST IPSPOOFFUNC
type: MMLCommand
name: LST IPSPOOFFUNC（展示IP防攻击功能状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPSPOOFFUNC
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
- IPSpoof攻击防护
status: active
---

# LST IPSPOOFFUNC（展示IP防攻击功能状态）

## 功能

**适用NF：UPF**

该参数用于查询当前配置的IP防欺诈功能开关状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [展示IP防攻击功能状态（IPSPOOFFUNC）](configobject/UDG/20.15.2/IPSPOOFFUNC.md)

## 使用实例

使用LST ANTISPOOFINGTHD命令查询当前配置的IP防欺诈功能开关状态：

```
LST IPSPOOFFUNC:;
```

```

RETCODE = 0 操作成功

IPSpoof攻击防护
-------------
上行IP防攻击开关 = 已使能
下行IP防攻击开关 = 已使能
(结果个数 = 1)

--- 结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/展示IP防攻击功能状态（LST-IPSPOOFFUNC）_87728428.md`
