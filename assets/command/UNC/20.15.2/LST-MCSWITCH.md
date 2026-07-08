---
id: UNC@20.15.2@MMLCommand@LST MCSWITCH
type: MMLCommand
name: LST MCSWITCH（查询多连接开关配置数据）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MCSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST MCSWITCH（查询多连接开关配置数据）

## 功能

该命令用于查询多连接开关的配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MCSWITCH]] · 多连接开关配置数据（MCSWITCH）

## 使用实例

查询多连接开关的配置：

```
%%LST MCSWITCH:;%%
RETCODE = 0  操作成功

结果如下
--------
多连接开关  =  开启
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MCSWITCH.md`
