---
id: UDG@20.15.2@MMLCommand@LST DRTLSMODE
type: MMLCommand
name: LST DRTLSMODE（查询容灾控制通道TLS模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DRTLSMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRTLSMODE（查询容灾控制通道TLS模式）

## 功能

该命令用于查询容灾控制通道TLS模式。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DRTLSMODE]] · 容灾控制通道TLS模式（DRTLSMODE）

## 使用实例

查询网元容灾控制通道TLS模式。

```
%%LST DRTLSMODE:;%%
RETCODE = 0  操作成功

结果如下
--------
TLS模式  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DRTLSMODE.md`
