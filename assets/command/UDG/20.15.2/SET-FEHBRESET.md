---
id: UDG@20.15.2@MMLCommand@SET FEHBRESET
type: MMLCommand
name: SET FEHBRESET（设置FE心跳故障复位功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FEHBRESET
command_category: 配置类
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

# SET FEHBRESET（设置FE心跳故障复位功能开关）

## 功能

![](设置FE心跳故障复位功能开关（SET FEHBRESET）_65383310.assets/notice_3.0-zh-cn.png)

当设置心跳复位开关为使能状态时，心跳故障会进行复位单板操作。

该命令用来设置FE心跳故障复位功能开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。
- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
  | SWITCH |
  | --- |
  | Disable |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 心跳复位开关 | 可选必选说明：必选参数<br>参数含义：FE心跳故障时，是否需要复位单板。<br>数据来源：本端规划<br>取值范围：<br>“Enable”：表示心跳故障后，复位单板。<br>“Disable”：表示心跳故障后，不复位单板。<br>默认值：无。<br>配置原则：建议值为“Enable”。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FEHBRESET]] · FE心跳故障复位功能开关（FEHBRESET）

## 使用实例

设置FE心跳故障复位单板功能开关为启用：

```
SET FEHBRESET: SWITCH=Enable;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-FEHBRESET.md`
