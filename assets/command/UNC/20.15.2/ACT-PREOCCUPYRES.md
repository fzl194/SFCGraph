---
id: UNC@20.15.2@MMLCommand@ACT PREOCCUPYRES
type: MMLCommand
name: ACT PREOCCUPYRES（预占RU资源）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: PREOCCUPYRES
command_category: 动作类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- RU资源
status: active
---

# ACT PREOCCUPYRES（预占RU资源）

## 功能

**适用NF：NCG**

该命令用于触发预占的RU资源。

## 注意事项

- 该命令执行后立即生效。
- 再次执行该命令需间隔30秒。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUTYPE | RU类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定预占RU的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CG_SP_RU：CG_SP_RU。<br>默认值：无<br>配置原则：无 |
| IDLENUM | 预占数量 | 可选必选说明：必选参数<br>参数含义：该参数用于指定预占RU的个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～7。<br>默认值：无<br>配置原则：目前只支持1-2。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PREOCCUPYRES]] · 预占RU资源（PREOCCUPYRES）

## 使用实例

预占RU资源：

```
ACT PREOCCUPYRES: RUTYPE=CG_SP_RU, IDLENUM=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/预占RU资源（ACT-PREOCCUPYRES）_51174356.md`
