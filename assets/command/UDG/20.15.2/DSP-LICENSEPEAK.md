---
id: UDG@20.15.2@MMLCommand@DSP LICENSEPEAK
type: MMLCommand
name: DSP LICENSEPEAK（显示话务高峰信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LICENSEPEAK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# DSP LICENSEPEAK（显示话务高峰信息）

## 功能

此命令用于查看话务高峰的相关信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LICENSEPEAK]] · 话务高峰信息（LICENSEPEAK）

## 使用实例

查询当年发生的话务峰值事件信息：

```
%%DSP LICENSEPEAK:;%%
RETCODE = 0  操作成功

已使用的峰值License记录
-----------------------
     使用日期  =  NULL
过载License项  =  NULL
(结果个数 = 1)

剩余次数
--------
 剩余使用次数  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LICENSEPEAK.md`
