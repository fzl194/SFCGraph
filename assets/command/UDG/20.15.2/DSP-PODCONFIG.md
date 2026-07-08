---
id: UDG@20.15.2@MMLCommand@DSP PODCONFIG
type: MMLCommand
name: DSP PODCONFIG（POD配置查询）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PODCONFIG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Pod管理
status: active
---

# DSP PODCONFIG（POD配置查询）

## 功能

该命令用于查询系统修复Pod功能的开关状态。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PODCONFIG]] · POD配置查询（PODCONFIG）

## 使用实例

查询系统修复Pod功能的开关状态：

```
%%DSP PODCONFIG:;%%
RETCODE = 0  操作成功

操作结果如下
------------
修复开关  =  ON
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PODCONFIG.md`
