---
id: UNC@20.15.2@MMLCommand@LST USERPRIORARP
type: MMLCommand
name: LST USERPRIORARP（查询用户ARP优先级配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USERPRIORARP
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 全局QoS功能配置
- 全局QoS参数
status: active
---

# LST USERPRIORARP（查询用户ARP优先级配置）

## 功能

**适用NF：PGW-C、GGSN**

该命令用来显示全局的QoS信息，包括漫游以及拜访用户的级别限制功能，以及限制级别。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/USERPRIORARP]] · 用户ARP优先级配置（USERPRIORARP）

## 使用实例

查询整机的拜访以及漫游用户的级别：

```
LST USERPRIORARP:;

RETCODE = 0  操作成功。

拜访或漫游用户的级别信息
------------------------
限制漫游用户级别  =  使能
漫游用户最高级别  =  中
限制拜访用户级别  =  使能
拜访用户最高级别  =  中
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户ARP优先级配置（LST-USERPRIORARP）_28093181.md`
