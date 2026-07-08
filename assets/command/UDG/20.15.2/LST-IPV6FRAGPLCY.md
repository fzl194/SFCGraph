---
id: UDG@20.15.2@MMLCommand@LST IPV6FRAGPLCY
type: MMLCommand
name: LST IPV6FRAGPLCY（查询IPv6分片策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPV6FRAGPLCY
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 传输层控制
- IPv6分片策略
status: active
---

# LST IPV6FRAGPLCY（查询IPv6分片策略）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询逻辑接口支持IPv6组网情况下的分片处理策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [IPv6分片策略（IPV6FRAGPLCY）](configobject/UDG/20.15.2/IPV6FRAGPLCY.md)

## 使用实例

查询逻辑接口支持IPv6组网情况下的分片处理策略：

```
LST IPV6FRAGPLCY:;
```

```

RETCODE = 0  操作成功。

IPV6分片策略
------------
内层为IPv6的分片策略  =  回复too big消息并对原始报文外层分片后转发
内层为IPv4的分片策略  =  外层分片
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPv6分片策略（LST-IPV6FRAGPLCY）_82837703.md`
