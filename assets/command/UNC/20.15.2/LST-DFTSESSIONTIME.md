---
id: UNC@20.15.2@MMLCommand@LST DFTSESSIONTIME
type: MMLCommand
name: LST DFTSESSIONTIME（查询默认会话上下文定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DFTSESSIONTIME
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- SMF公共配置
- 空闲上下文定时器
status: active
---

# LST DFTSESSIONTIME（查询默认会话上下文定时器）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询SessionTimeout的全局配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DFTSESSIONTIME]] · 默认会话上下文定时器（DFTSESSIONTIME）

## 使用实例

查询SessionTimeout的全局配置：

```
%%LST DFTSESSIONTIME:;%%
RETCODE = 0  操作成功

结果如下
--------
会话时长开关  =  使能
    会话时长  =  120
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询默认会话上下文定时器（LST-DFTSESSIONTIME）_96242121.md`
