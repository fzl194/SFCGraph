---
id: UDG@20.15.2@MMLCommand@DSP APPVERSION
type: MMLCommand
name: DSP APPVERSION（显示系统版本信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: APPVERSION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 软件管理
- 版本管理
status: active
---

# DSP APPVERSION（显示系统版本信息）

## 功能

此命令用于显示系统版本号。

> **说明**
> 无

## 权限

G_1，管理员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/APPVERSION]] · 系统版本信息（APPVERSION）

## 使用实例

DSP APPVERSION:;

```
%%DSP APPVERSION:;%%
RETCODE = 0  操作成功
结果如下
------------------------
版本号  =  xxx 20.0.0.B080
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示系统版本信息（DSP-APPVERSION）_09587389.md`
