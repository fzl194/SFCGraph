---
id: UDG@20.15.2@MMLCommand@LST IPSPOOFALMTHD
type: MMLCommand
name: LST IPSPOOFALMTHD（查询IP Spoofing攻击告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPSPOOFALMTHD
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- IP Spoofing攻击防护
- 反嗅探告警
status: active
---

# LST IPSPOOFALMTHD（查询IP Spoofing攻击告警阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询ip spoofing告警产生的条件。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSPOOFALMTHD]] · IP Spoofing攻击告警阈值（IPSPOOFALMTHD）

## 使用实例

假设运营商需要查看产生ip spoofing告警时：

```
LST IPSPOOFALMTHD:;
```

```

RETCODE = 0  操作成功。

IP Spoofing占用率告警阈值
-------------------------
anti spoofing告警开关  =  使能
             初始阈值  =  1500
             增量阈值  =  1500
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IP-Spoofing攻击告警阈值（LST-IPSPOOFALMTHD）_82837780.md`
