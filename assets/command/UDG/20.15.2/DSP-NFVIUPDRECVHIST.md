---
id: UDG@20.15.2@MMLCommand@DSP NFVIUPDRECVHIST
type: MMLCommand
name: DSP NFVIUPDRECVHIST（查询分批升级历史）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NFVIUPDRECVHIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- NFVI分批升级管理
status: active
---

# DSP NFVIUPDRECVHIST（查询分批升级历史）

## 功能

该命令用于查询NFVI分批升级恢复历史记录。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/NFVIUPDRECVHIST]] · 分批升级历史（NFVIUPDRECVHIST）

## 使用实例

查询NFVI分批升级历史记录。

```
%%DSP NFVIUPDRECVHIST:;%%
RETCODE = 0  操作成功

结果如下
------------------------
操作模式  =  Recovery
处理结果  =  Succeed
处理详情  =  NULL
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询分批升级历史（DSP-NFVIUPDRECVHIST）_63673344.md`
