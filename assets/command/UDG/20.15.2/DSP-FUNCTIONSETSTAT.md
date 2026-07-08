---
id: UDG@20.15.2@MMLCommand@DSP FUNCTIONSETSTAT
type: MMLCommand
name: DSP FUNCTIONSETSTAT（显示网络功能集状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FUNCTIONSETSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 部署规格管理
status: active
---

# DSP FUNCTIONSETSTAT（显示网络功能集状态）

## 功能

该命令用于显示网络功能集。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/FUNCTIONSETSTAT]] · 网络功能集状态（FUNCTIONSETSTAT）

## 使用实例

显示当前网络功能集: DSP FUNCTIONSETSTAT :;

```
%%DSP FUNCTIONSETSTAT :;%%
RETCODE = 0  操作成功 
结果如下 
--------
网络功能集名称       状态信息
Plat_Base            online
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-FUNCTIONSETSTAT.md`
