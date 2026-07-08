---
id: UDG@20.15.2@MMLCommand@LST MSFAULTALARM
type: MMLCommand
name: LST MSFAULTALARM（查询告警开关配置数据）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MSFAULTALARM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST MSFAULTALARM（查询告警开关配置数据）

## 功能

该命令用于查询告警抑制的配置。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MSFAULTALARM]] · 告警开关配置数据（MSFAULTALARM）

## 使用实例

查询告警抑制使能开关的配置：

```
%%LST MSFAULTALARM:;%%
RETCODE = 0  操作成功

结果如下
------------------------
告警抑制使能开关  =  开启
告警抑制时间(秒)  =  300
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MSFAULTALARM.md`
