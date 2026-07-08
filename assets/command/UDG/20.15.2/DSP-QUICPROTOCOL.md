---
id: UDG@20.15.2@MMLCommand@DSP QUICPROTOCOL
type: MMLCommand
name: DSP QUICPROTOCOL（查询Quic类协议）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: QUICPROTOCOL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- QUIC类协议信息
status: active
---

# DSP QUICPROTOCOL（查询Quic类协议）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询设备支持的Quic类协议。

## 注意事项

- 该命令显示的是设备支持的Quic类协议信息，加载知识库完成后需要等待至少1分钟，才能查询设备支持的Quic类协议信息。
- 该命令显示结果为设备加载过的最新知识库支持解析的全量QUIC类应用协议。回退知识库后显示协议不会发生变化。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@QUICPROTOCOL]] · Quic类协议（QUICPROTOCOL）

## 使用实例

查询设备支持的Quic类协议：

```
DSP QUICPROTOCOL:;
```

```

RETCODE = 0 操作成功。

Quic类协议
-----------
协议名称  =  google_quic
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-QUICPROTOCOL.md`
