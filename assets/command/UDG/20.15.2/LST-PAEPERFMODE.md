---
id: UDG@20.15.2@MMLCommand@LST PAEPERFMODE
type: MMLCommand
name: LST PAEPERFMODE（查询配置表中的PAE性能模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PAEPERFMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 性能模式
status: active
---

# LST PAEPERFMODE（查询配置表中的PAE性能模式）

## 功能

该命令用于查询配置表中的PAE性能模式。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PAEPERFMODE]] · 配置表中的PAE性能模式（PAEPERFMODE）

## 使用实例

查询配置表中的PAE性能模式

```
+++    UNC/*MEID:0 MENAME:unc*/        2024-05-20 18:36:11
O&M    #73
%%LST PAEPERFMODE:;%%
RETCODE = 0  操作成功

结果如下
--------
Pod类型      PAEDP性能模式  sdra的性能模式

vusn-pod     低性能模式0    使用默认性能模式
sfpod        低性能模式0    使用默认性能模式
lbpod        低性能模式0    使用默认性能模式
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PAEPERFMODE.md`
