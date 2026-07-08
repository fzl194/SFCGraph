---
id: UNC@20.15.2@MMLCommand@ADD EMGCNUM
type: MMLCommand
name: ADD EMGCNUM（增加紧急号码配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: EMGCNUM
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 64
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 紧急呼叫配置
- 紧急呼叫号码配置
status: active
---

# ADD EMGCNUM（增加紧急号码配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于配置紧急呼叫号码。系统在给MS发送ATTACH ACCEPT消息和TAU ACCEPT消息时，会将配置的MCC的紧急呼叫号码携带在消息中发送给MS。

## 注意事项

- 此命令最大记录数为64条。
- 此命令执行后立即生效。
- 紧急呼叫号码必须是运营商已经规划的号码，需要正确配置。配置错误可能导致UE的紧急呼叫接入错误，例如：
    - 将非紧急呼叫号码配置为紧急呼叫号码，用户被接入至政府部门。
    - 紧急服务分类配置错误，用户被错误接入其他政府部门。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定增加哪个移动国家码配置紧急呼叫号码。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无<br>配置原则：同一MCC配置的紧急呼叫号码必须不相同，一个MCC最多能够增加10个紧急呼叫号码，不区分紧急号码类别。一个MCC对应的紧急号码总长不能超过96位。 |
| ESC | 紧急服务分类 | 可选必选说明：必选参数<br>参数含义：该参数用于指定紧急呼叫号码的服务名称。<br>数据来源：整网规划<br>取值范围：<br>- “POLICE(报警)”<br>- “AMBULANCE(医疗救护)”<br>- “FIREBRIGADE(火警)”<br>- “MARINEGUARD(海上救援)”<br>- “MOUNTAIN(高山救援)”<br>默认值：无<br>说明：POLICE，报警服务；AMBULANCE，医疗救护；FIREBRIGADE，火警；MARINEGUARD，海上救援；MOUNTAIN，高山救援。 |
| NUM | 紧急呼叫号码 | 可选必选说明：必选参数<br>参数含义：该参数用于指示待增加的紧急业务对应的号码。<br>数据来源：整网规划<br>取值范围：长度不超过80的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EMGCNUM]] · 紧急号码信息表记录（EMGCNUM）

## 使用实例

给移动国家码为“123”的网络增加火警紧急呼叫号码“119”：

ADD EMGCNUM: MCC="123", ESC=POLICE-0&AMBULANCE-0&FIREBRIGADE-1&MARINEGUARD-0&MOUNTAIN-0, NUM="119";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加紧急号码配置信息(ADD-EMGCNUM)_26305314.md`
