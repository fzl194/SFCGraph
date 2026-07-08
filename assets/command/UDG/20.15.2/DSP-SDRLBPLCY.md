---
id: UDG@20.15.2@MMLCommand@DSP SDRLBPLCY
type: MMLCommand
name: DSP SDRLBPLCY（查询SDRC中缓存的下一跳组信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRLBPLCY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRLBPLCY（查询SDRC中缓存的下一跳组信息）

## 功能

该命令用于查询SDRC中缓存的下一跳组信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/SDRLBPLCY]] · SDRC中缓存的下一跳组信息（SDRLBPLCY）

## 使用实例

查询出SDRC中缓存的下一跳组信息，结果如下：

```
%%DSP SDRLBPLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
APP类型  下一跳组ID  KeyMatch类型  内核态TP  Token组  强制Hash推送  灰度拨测Token组

140      65          hash          否        0            false      4294967295
142      66          hash          否        0            false      4294967295  
1008     90          hash          否        0            false      4294967295
129      0           linear        否        0            true       4294967295
1034     75          hash          否        0            false      4294967295
1034     79          linear        否        0            false      4294967295
(结果个数 = 6)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SDRC中缓存的下一跳组信息（DSP-SDRLBPLCY）_94730429.md`
