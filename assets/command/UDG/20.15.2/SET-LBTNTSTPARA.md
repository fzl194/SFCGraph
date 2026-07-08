---
id: UDG@20.15.2@MMLCommand@SET LBTNTSTPARA
type: MMLCommand
name: SET LBTNTSTPARA（设置CSLB隧道探测参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: LBTNTSTPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 隧道管理
- CSLB隧道探测参数
status: active
---

# SET LBTNTSTPARA（设置CSLB隧道探测参数）

## 功能

该命令用于设置CSLB隧道探测参数。

## 注意事项

- 系统初次上电运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DELAYDETPERIOD | 隧道时延探测周期（秒） | 可选必选说明：可选参数<br>参数含义：该参数表示隧道时延探测周期，即隧道时延探测报文的发送时间间隔。<br>数据来源：本端规划<br>取值范围：1~100<br>默认值：无<br>系统初始设置值：10<br>配置原则：无特殊情况不需要修改。 |
| DROPSTATPERIOD | 隧道丢包率统计周期（秒） | 可选必选说明：可选参数<br>参数含义：该参数表示隧道丢包率统计周期。<br>数据来源：本端规划<br>取值范围：1~60<br>默认值：无<br>系统初始设置值：5<br>配置原则：无特殊情况不需要修改。 |

## 操作的配置对象

- [CSLB隧道探测参数（LBTNTSTPARA）](configobject/UDG/20.15.2/LBTNTSTPARA.md)

## 使用实例

设置隧道时延探测周期为20秒，隧道丢包率统计周期为10秒:

SET LBTNTSTPARA: DELAYDETPERIOD=20, DROPSTATPERIOD=10;

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置CSLB隧道探测参数（SET-LBTNTSTPARA）_50911922.md`
