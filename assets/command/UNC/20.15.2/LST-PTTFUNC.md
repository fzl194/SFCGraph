---
id: UNC@20.15.2@MMLCommand@LST PTTFUNC
type: MMLCommand
name: LST PTTFUNC（查询一键通功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PTTFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 一键通
- 全局一键通配置
status: active
---

# LST PTTFUNC（查询一键通功能配置）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于查询整机一键通功能相关的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PTTFUNC]] · 一键通功能配置（PTTFUNC）

## 使用实例

显示全局一键通功能配置：

```
%%LST PTTFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
LTE一键通功能开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询一键通功能配置（LST-PTTFUNC）_06399916.md`
