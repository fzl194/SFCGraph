---
id: UDG@20.15.2@MMLCommand@SET FEHEARTBEAT
type: MMLCommand
name: SET FEHEARTBEAT（设置FE心跳功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FEHEARTBEAT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 转发引擎实例FEI
- 心跳开关
status: active
---

# SET FEHEARTBEAT（设置FE心跳功能开关）

## 功能

该命令用来设置FE心跳功能开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。
- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
  | FEHBSW |
  | --- |
  | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FEHBSW | 心跳开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置心跳功能开关。<br>数据来源：本端规划<br>取值范围：<br>“OFF”：表示关闭心跳开关。<br>“ON”：表示打开心跳开关。<br>默认值：无。<br>配置原则：建议值为“ON”。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FEHEARTBEAT]] · FE心跳功能开关（FEHEARTBEAT）

## 使用实例

设置FE心跳功能开关为启用：

```
SET FEHEARTBEAT: FEHBSW=ON;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置FE心跳功能开关（SET-FEHEARTBEAT）_12703105.md`
