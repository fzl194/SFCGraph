---
id: UNC@20.15.2@MMLCommand@SET IFGLOBALCONFIG
type: MMLCommand
name: SET IFGLOBALCONFIG（设置接口全局配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IFGLOBALCONFIG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 接口全局配置
status: active
---

# SET IFGLOBALCONFIG（设置接口全局配置）

## 功能

该命令用于设置接口全局属性。

## 注意事项

- 该命令执行后立即生效。
- FLOWINTERVAL和IFFIRSTDOWNSNDALM这两个参数必须至少输入一个。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| FLOWINTERVAL | IFFIRSTDOWNSNDALM |
| --- | --- |
| 5 | FALSE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWINTERVAL | 全局流量统计间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定全局流量统计的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～600，单位是秒。取值为5的整数倍。<br>默认值：无 |
| IFFIRSTDOWNSNDALM | 使能接口首次Down告警上报 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使能接口首次Down的告警上报。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。TRUE：使能接口首次Down告警上报。FALSE：去使能接口首次Down告警上报。<br>默认值：无 |

## 操作的配置对象

- [接口全局配置（IFGLOBALCONFIG）](configobject/UNC/20.15.2/IFGLOBALCONFIG.md)

## 使用实例

设置全局的流量统计间隔和接口首次Down告警上报使能：

```
SET IFGLOBALCONFIG:FLOWINTERVAL=300, IFFIRSTDOWNSNDALM = TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置接口全局配置（SET-IFGLOBALCONFIG）_50280646.md`
