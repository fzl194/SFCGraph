---
id: UNC@20.15.2@MMLCommand@LST DFTIPEPCFGRP
type: MMLCommand
name: LST DFTIPEPCFGRP（查询全局默认智能PCF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DFTIPEPCFGRP
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 智能双N7会话
status: active
---

# LST DFTIPEPCFGRP（查询全局默认智能PCF组）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查询全局默认智能PCF组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DFTIPEPCFGRP]] · 全局默认智能PCF组（DFTIPEPCFGRP）

## 使用实例

查询全局智能PCF组配置：

```
%%LST DFTIPEPCFGRP:;%%
RETCODE = 0  操作成功

结果如下
--------
主智能PCF组  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DFTIPEPCFGRP.md`
