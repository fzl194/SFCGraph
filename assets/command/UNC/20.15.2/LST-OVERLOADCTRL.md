---
id: UNC@20.15.2@MMLCommand@LST OVERLOADCTRL
type: MMLCommand
name: LST OVERLOADCTRL（查询过载控制的配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OVERLOADCTRL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 信令抑制
status: active
---

# LST OVERLOADCTRL（查询过载控制的配置信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来查询过载控制的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OVERLOADCTRL]] · 过载控制的配置信息（OVERLOADCTRL）

## 使用实例

显示当前UNC过载控制的配置信息：

```
LST OVERLOADCTRL:;
RETCODE = 0  Operation Success.

The result is as follows
------------------------
 Signaling Control Switch  =  DISABLE
           Aging Time (s)  =  60
             CCR-I Switch  =  DISABLE
  Accounting Start Switch  =  DISABLE
NAS Message Failure Cause  =  INSUFFICIENT_RESOURCES
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OVERLOADCTRL.md`
