---
id: UDG@20.15.2@MMLCommand@LST TOMSSCFG
type: MMLCommand
name: LST TOMSSCFG（查询Tcp Mss配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOMSSCFG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP MSS配置
status: active
---

# LST TOMSSCFG（查询Tcp Mss配置）

## 功能

**适用NF：UPF**

该命令用于查询TCP MSS值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TOMSSCFG]] · Tcp Mss配置（TOMSSCFG）

## 使用实例

查询TCP MSS值：

```
LST TOMSSCFG:;
```

```

RETCODE = 0 操作成功。

TCP MSS配置
-----------
IPv4 TCP报文长度（字节） = 496
IPv6 TCP报文长度（字节） = 1500
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TOMSSCFG.md`
