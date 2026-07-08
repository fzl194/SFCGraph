---
id: UNC@20.15.2@MMLCommand@SET SMSREGTIMER
type: MMLCommand
name: SET SMSREGTIMER（设置VLR/SMSF向注册中心注册的时间参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSREGTIMER
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 定时器管理
status: active
---

# SET SMSREGTIMER（设置VLR/SMSF向注册中心注册的时间参数）

## 功能

**适用NF：SMSF**

该命令用于设置VLR/SMSF向注册中心注册的时间参数。

## 注意事项

- 该命令执行后立即生效。

- 双活组网的场景下，如果需要配置此命令，则两个VLR/SMSF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SMSFREGRCTIMER | VLRREGRCTIMER |
| --- | --- |
| 50 | 54 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMSFREGRCTIMER | SMSF向注册中心注册更新的时间间隔(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSF向注册中心注册更新的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10080，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSREGTIMER查询当前参数配置值。<br>配置原则：无 |
| VLRREGRCTIMER | VLR向注册中心注册更新的时间间隔(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于表示VLR向注册中心注册更新的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10080，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSREGTIMER查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSREGTIMER]] · VLR/SMSF向注册中心注册的时间参数（SMSREGTIMER）

## 使用实例

运营商希望设置“SMSF向注册中心注册更新的时间间隔(分钟)”为“24”，“VLR向注册中心注册更新的时间间隔(分钟)”为“24”，执行如下命令：

```
SET SMSREGTIMER: SMSFREGRCTIMER=24, VLRREGRCTIMER=24;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SMSREGTIMER.md`
