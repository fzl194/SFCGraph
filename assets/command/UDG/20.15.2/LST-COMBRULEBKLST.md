---
id: UDG@20.15.2@MMLCommand@LST COMBRULEBKLST
type: MMLCommand
name: LST COMBRULEBKLST（显示组合规则黑名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: COMBRULEBKLST
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- CombRuleBkLst
status: active
---

# LST COMBRULEBKLST（显示组合规则黑名单）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示组合规则的黑名单。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/COMBRULEBKLST]] · 组合规则黑名单（COMBRULEBKLST）

## 使用实例

查询组合规则的黑名单：

```
LST COMBRULEBKLST:;
```

```

RETCODE = 0  操作成功

组合规则黑名单信息
------------------
黑名单策略类型  =  Captive Portal智能重定向&ADC&QOS
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示组合规则黑名单（LST-COMBRULEBKLST）_86530160.md`
