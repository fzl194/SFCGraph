---
id: UDG@20.15.2@MMLCommand@LST TCPKEEPALIVECFG
type: MMLCommand
name: LST TCPKEEPALIVECFG（查询TCP保活参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TCPKEEPALIVECFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TCP保活配置
status: active
---

# LST TCPKEEPALIVECFG（查询TCP保活参数）

## 功能

该命令用于查询TWAMP的Full模式TCP保活参数配置。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/TCPKEEPALIVECFG]] · TCP保活参数（TCPKEEPALIVECFG）

## 使用实例

查询TWAMP的TCP保活参数的实例：

```
%%LST TCPKEEPALIVECFG: ;%%
RETCODE = 0  操作成功
 
结果如下
--------
保活时间  =  90
保活间隔  =  30
保活重试  =  9
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TCPKEEPALIVECFG.md`
