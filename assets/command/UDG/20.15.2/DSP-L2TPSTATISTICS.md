---
id: UDG@20.15.2@MMLCommand@DSP L2TPSTATISTICS
type: MMLCommand
name: DSP L2TPSTATISTICS（查询L2TP报文统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: L2TPSTATISTICS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP报文统计维护
status: active
---

# DSP L2TPSTATISTICS（查询L2TP报文统计信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查看系统的L2TP控制报文统计信息。运营商需要查看控制报文数场景，可以使用该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/L2TPSTATISTICS]] · L2TP报文统计信息（L2TPSTATISTICS）

## 使用实例

假设运营商想查看L2TP控制报文统计信息：

```
DSP L2TPSTATISTICS:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
    收到控制报文数  =  0
收到无效控制报文数  =  0
    发送控制报文数  =  0
发送无效控制报文数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询L2TP报文统计信息（DSP-L2TPSTATISTICS）_35373533.md`
