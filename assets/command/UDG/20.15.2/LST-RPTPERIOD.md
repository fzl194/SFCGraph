---
id: UDG@20.15.2@MMLCommand@LST RPTPERIOD
type: MMLCommand
name: LST RPTPERIOD（显示APN N6故障状态上报周期）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTPERIOD
command_category: 查询类
applicable_nf:
- SGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- N6路径管理
- APN周期上报参数
status: active
---

# LST RPTPERIOD（显示APN N6故障状态上报周期）

## 功能

**适用NF：SGW-U、UPF**

该命令用于查询APN N6故障状态上报周期。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPERIOD]] · APN N6故障状态上报周期（RPTPERIOD）

## 使用实例

查询APN N6故障状态上报周期,使用一下命令：

```
LST RPTPERIOD:;
```

```

RETCODE = 0  操作成功

APN N6故障状态上报周期
------------------------------------------
APN N6故障状态上报周期  =  4
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示APN-N6故障状态上报周期（LST-RPTPERIOD）_12563795.md`
