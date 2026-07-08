---
id: UDG@20.15.2@MMLCommand@LST SIGDSCP
type: MMLCommand
name: LST SIGDSCP（查询信令报文DSCP值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SIGDSCP
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
- 信令QOS控制
- 信令DSCP
status: active
---

# LST SIGDSCP（查询信令报文DSCP值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询信令报文的DSCP值。

## 注意事项

TM信令和GTP信令在未配置时不显示。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SIGDSCP]] · 信令报文DSCP值（SIGDSCP）

## 使用实例

查询所有协议的DSCP值：

```
LST SIGDSCP:;
```

```

RETCODE = 0  操作成功。

信令报文DSCP值
--------------
信令协议      DSCP值

PFCP信令      46          
L2tp信令      46          
PPP信令       46          
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SIGDSCP.md`
