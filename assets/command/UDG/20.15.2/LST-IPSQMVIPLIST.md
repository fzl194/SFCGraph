---
id: UDG@20.15.2@MMLCommand@LST IPSQMVIPLIST
type: MMLCommand
name: LST IPSQMVIPLIST（查询IPSQM VIP用户列表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPSQMVIPLIST
command_category: 查询类
applicable_nf:
- SGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- IPSQM控制
- IPSQM VIP用户列表
status: active
---

# LST IPSQMVIPLIST（查询IPSQM VIP用户列表）

## 功能

**适用NF：SGW-U、UPF**

该命令用于查询不做IPSQM流量整形的VIP用户列表。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPSQMVIPLIST]] · IPSQM VIP用户列表（IPSQMVIPLIST）

## 使用实例

查询不做IPSQM流量整形的VIP用户列表：

```
LST IPSQMVIPLIST:;
```

```

RETCODE = 0  操作成功

IPSQM VIP用户列表
-----------------
  用户标识  =  MSISDN
用户ID信息  =  140000000098500
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPSQMVIPLIST.md`
