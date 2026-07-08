---
id: UDG@20.15.2@MMLCommand@LST FEHBRESET
type: MMLCommand
name: LST FEHBRESET（查询FE心跳故障复位功能开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FEHBRESET
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 转发引擎实例FEI
- 心跳故障复位开关
status: active
---

# LST FEHBRESET（查询FE心跳故障复位功能开关）

## 功能

该命令用来查询FE心跳故障复位功能开关状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [FE心跳故障复位功能开关（FEHBRESET）](configobject/UDG/20.15.2/FEHBRESET.md)

## 使用实例

查询FE心跳故障复位功能开关状态：

```
LST FEHBRESET:;
RETCODE = 0  操作成功

结果如下
--------
心跳复位开关  =  Disable
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询FE心跳故障复位功能开关（LST-FEHBRESET）_12383445.md`
