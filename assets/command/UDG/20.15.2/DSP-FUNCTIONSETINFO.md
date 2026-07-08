---
id: UDG@20.15.2@MMLCommand@DSP FUNCTIONSETINFO
type: MMLCommand
name: DSP FUNCTIONSETINFO（显示网络功能集全局列表）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FUNCTIONSETINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 部署规格管理
status: active
---

# DSP FUNCTIONSETINFO（显示网络功能集全局列表）

## 功能

该命令用于显示全量网络功能列表。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/FUNCTIONSETINFO]] · 网络功能集全局列表（FUNCTIONSETINFO）

## 使用实例

DSP FUNCTIONSETINFO;

```
%%DSP FUNCTIONSETINFO:;%%
RETCODE =0 操作成功
结果如下
-------
网络功能集名称      Pod类型                               动态上下线开关
xxx-4G              vusn-pod:0,gtp-pod:0,vusnom-pod:0     是
xxx-pfcp            vsm-pod:0                             是
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-FUNCTIONSETINFO.md`
