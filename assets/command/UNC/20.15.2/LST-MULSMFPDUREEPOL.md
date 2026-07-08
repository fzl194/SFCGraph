---
id: UNC@20.15.2@MMLCommand@LST MULSMFPDUREEPOL
type: MMLCommand
name: LST MULSMFPDUREEPOL（查询是否支持多SMFInfo场景下的会话重建功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MULSMFPDUREEPOL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 跨区域PDU会话管理
- 多SMFInfo会话重建策略
status: active
---

# LST MULSMFPDUREEPOL（查询是否支持多SMFInfo场景下的会话重建功能）

## 功能

**适用NF：SMF**

该命令用于查询SMF是否支持多SMFInfo场景下的会话重建功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [是否支持多SMFInfo场景下的会话重建功能（MULSMFPDUREEPOL）](configobject/UNC/20.15.2/MULSMFPDUREEPOL.md)

## 使用实例

查询SMF是否支持多SMFInfo场景下的会话重建功能。

```
%%LST MULSMFPDUREEPOL;%%
RETCODE = 0  操作成功

结果如下
--------
是否支持多SMFInfo下PDU会话重建 = 不支持
（结果个数 = 1）
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询是否支持多SMFInfo场景下的会话重建功能（LST-MULSMFPDUREEPOL）_70382321.md`
