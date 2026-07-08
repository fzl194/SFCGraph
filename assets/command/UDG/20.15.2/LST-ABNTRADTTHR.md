---
id: UDG@20.15.2@MMLCommand@LST ABNTRADTTHR
type: MMLCommand
name: LST ABNTRADTTHR（查询异常流量检测报文阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ABNTRADTTHR
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- 异常下行流量检测阈值
status: active
---

# LST ABNTRADTTHR（查询异常流量检测报文阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询异常流量检测报文阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ABNTRADTTHR]] · 异常流量检测报文阈值（ABNTRADTTHR）

## 使用实例

查询异常下行异常流量检测报文阈值个数：

```
LST ABNTRADTTHR:;
```

```

RETCODE = 0  Operation Success.

Abnormal Traffic detect threshold
---------------------------------
Abnormal Traffic detect threshold of packet  =  20
(Number of results = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ABNTRADTTHR.md`
