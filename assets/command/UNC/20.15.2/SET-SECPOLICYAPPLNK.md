---
id: UNC@20.15.2@MMLCommand@SET SECPOLICYAPPLNK
type: MMLCommand
name: SET SECPOLICYAPPLNK（设置应用联动默认动作）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SECPOLICYAPPLNK
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略应用层联动默认动作
status: active
---

# SET SECPOLICYAPPLNK（设置应用联动默认动作）

## 功能

该命令用于设置应用联动的缺省动作。

执行SET SECPOLICYAPPLNK命令可以设置应用层联动功能对上送CPU的报文的默认处理方式。当需要进行应用层协议攻击分析时，可以将协议报文的处理方式配置成Min_to_cp模式，这样就可以获取上送的协议报文，从而进行攻击溯源。

缺省情况下，应用层联动功能是使能的。

只有应用层联动使能情况下，此命令才有效。

## 注意事项

- 该命令执行后立即生效。
- 该命令的设定值可通过DSP SECPOLICYAPPLNK命令进行查询。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| SECDFTACTION |
| --- |
| Min_to_cp |

- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 策略编号 | 可选必选说明：必选参数<br>参数含义：策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：需要先添加安全策略，下发本MML命令前可使用LST SECPOLICY查看已添加的安全策略。 |
| SECDFTACTION | 默认处理方式 | 可选必选说明：必选参数<br>参数含义：默认处理方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Drop：丢弃。<br>- Min_to_cp：传给CPU。<br>默认值：无 |

## 操作的配置对象

- [应用联动默认动作（SECPOLICYAPPLNK）](configobject/UNC/20.15.2/SECPOLICYAPPLNK.md)

## 使用实例

设置应用联动的缺省动作：

```
SET SECPOLICYAPPLNK: SECPOLICYID=1,SECDFTACTION=Min_to_cp;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置应用联动默认动作（SET-SECPOLICYAPPLNK）_49801822.md`
