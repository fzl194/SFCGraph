---
id: UDG@20.15.2@MMLCommand@LST IPV4FRAGPLCY
type: MMLCommand
name: LST IPV4FRAGPLCY（查询IPv4分片策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPV4FRAGPLCY
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
- IPv4分片策略
status: active
---

# LST IPV4FRAGPLCY（查询IPv4分片策略）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询逻辑接口在IPv4组网场景下的分片处理策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPV4FRAGPLCY]] · IPv4分片策略（IPV4FRAGPLCY）

## 使用实例

查询逻辑接口在IPv4组网场景下的分片处理策略：

```
LST IPV4FRAGPLCY:;
```

```

RETCODE = 0  操作成功。

IPV4分片策略
------------
内层为IPv4的分片策略  =  外层分片
内层为IPv6的分片策略  =  外层分片
             分片长度选项  = 内层总包长
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPV4FRAGPLCY.md`
