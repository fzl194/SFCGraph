---
id: UDG@20.15.2@MMLCommand@LST SAMUTEPROTOCOL
type: MMLCommand
name: LST SAMUTEPROTOCOL（查询SA EGN规则不启用协议）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SAMUTEPROTOCOL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- SA EGN规则生效控制
status: active
---

# LST SAMUTEPROTOCOL（查询SA EGN规则不启用协议）

## 功能

**适用NF：PGW-U、UPF、GGSN**

该命令用于查询SA协议规则关闭配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SAMUTEPROTOCOL]] · SA EGN规则不启用协议（SAMUTEPROTOCOL）

## 使用实例

查询SA协议规则关闭配置：

```
LST SAMUTEPROTOCOL:;
```

```

RETCODE = 0  操作成功

结果如下
--------
协议名称  =  socks5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SA-EGN规则不启用协议（LST-SAMUTEPROTOCOL）_74004971.md`
