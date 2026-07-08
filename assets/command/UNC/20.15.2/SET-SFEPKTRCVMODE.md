---
id: UNC@20.15.2@MMLCommand@SET SFEPKTRCVMODE
type: MMLCommand
name: SET SFEPKTRCVMODE（配置SFE收包模式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SFEPKTRCVMODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP性能配置
- SFE收包模式配置
status: active
---

# SET SFEPKTRCVMODE（配置SFE收包模式）

## 功能

该命令用来配置SFE收包模式。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODE | SFE收包模式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示SFE收包模式信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ABSOLUTE_PRIORITY：绝对优先级收包模式。<br>- RELATIVE_PRIORITY：相对优先级收包模式。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFEPKTRCVMODE]] · SFE当前收包模式（SFEPKTRCVMODE）

## 使用实例

配置SFE收包模式为相对优先级：

```
SET SFEPKTRCVMODE:MODE=RELATIVE_PRIORITY;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/配置SFE收包模式（SET-SFEPKTRCVMODE）_49961330.md`
