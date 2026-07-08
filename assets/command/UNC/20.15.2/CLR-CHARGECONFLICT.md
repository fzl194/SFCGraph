---
id: UNC@20.15.2@MMLCommand@CLR CHARGECONFLICT
type: MMLCommand
name: CLR CHARGECONFLICT（清除计费配置冲突）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: CHARGECONFLICT
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费维护
- 清除冲突配置
status: active
---

# CLR CHARGECONFLICT（清除计费配置冲突）

## 功能

**适用NF：PGW-C、SMF**

该命令用来清除当前系统中所有保存的计费业务冲突配置的信息并恢复告警。

## 注意事项

- 该命令执行后立即生效。
- 当系统中有计费业务冲突的配置时，系统提示告警（ALM-81033 配置与业务冲突）信息，执行该命令后，系统的冲突计费配置信息立即清除，告警恢复。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHARGECONFLICT]] · 计费配置冲突（CHARGECONFLICT）

## 使用实例

清除计费配置冲突：

```
CLR CHARGECONFLICT:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-CHARGECONFLICT.md`
