---
id: UNC@20.15.2@MMLCommand@LST FCSWITCH
type: MMLCommand
name: LST FCSWITCH（查询流控开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FCSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 流控管理
status: active
---

# LST FCSWITCH（查询流控开关）

## 功能

该命令用于查询整系统的流控功能禁用/启用状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/FCSWITCH]] · 流控开关（FCSWITCH）

## 使用实例

查询流控功能是否启用。

```
LST FCSWITCH:;
RETCODE = 0  操作成功

结果如下
------------------------
开关  =  启用
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FCSWITCH.md`
