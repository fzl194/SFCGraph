---
id: UNC@20.15.2@MMLCommand@SET IPV6THRESHOLD
type: MMLCommand
name: SET IPV6THRESHOLD（设置IPv6阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IPV6THRESHOLD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由基础
- IPv6阈值
status: active
---

# SET IPV6THRESHOLD（设置IPv6阈值）

## 功能

该命令用来设置IPv6整机路由前缀的告警阈值，在整机路由前缀数量超过阈值时，上报告警，提示用户检查是否存在异常，提前干预。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| UPPERPERCENT | LOWERPERCENT |
| --- | --- |
| 80 | 70 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPPERPERCENT | 最大百分比（%） | 可选必选说明：必选参数<br>参数含义：该参数用于指定触发整机路由前缀阈值告警的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。这里代表百分数。<br>默认值：无<br>配置原则：要大于最小百分比。 |
| LOWERPERCENT | 最小百分比（%） | 可选必选说明：必选参数<br>参数含义：该参数用于指定触发整机路由前缀阈值清除告警的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。这里代表百分数。<br>默认值：无<br>配置原则：要小于最大百分比。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV6THRESHOLD]] · IPv6阈值（IPV6THRESHOLD）

## 使用实例

配置触发整机路由前缀阈值告警的阈值为85%，触发整机路由前缀阈值清除告警的阈值为65%：

```
SET IPV6THRESHOLD:UPPERPERCENT=85,LOWERPERCENT=65;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IPV6THRESHOLD.md`
