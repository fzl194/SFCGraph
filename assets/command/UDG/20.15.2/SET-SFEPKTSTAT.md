---
id: UDG@20.15.2@MMLCommand@SET SFEPKTSTAT
type: MMLCommand
name: SET SFEPKTSTAT（设置报文统计记录开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SFEPKTSTAT
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 转发报文统计记录
status: active
---

# SET SFEPKTSTAT（设置报文统计记录开关）

## 功能

设置报文统计记录开关。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISENABLE | 报文统计记录开关使能 | 可选必选说明：必选参数<br>参数含义：报文统计记录开关使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFEPKTSTAT]] · SFE报文统计信息（SFEPKTSTAT）

## 使用实例

软转发报文统计记录使能：

```
SET SFEPKTSTAT: ISENABLE = TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置报文统计记录开关（SET-SFEPKTSTAT）_50280870.md`
