---
id: UNC@20.15.2@MMLCommand@ADD MPACV4POLICY
type: MMLCommand
name: ADD MPACV4POLICY（增加IPv4 MPAC策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MPACV4POLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 16
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- 管理平面接入控制IPv4策略
status: active
---

# ADD MPACV4POLICY（增加IPv4 MPAC策略）

## 功能

该命令用于在设备上创建管理平面接入控制策略（IPv4 MPAC）。

为了防止非法用户通过某些用户的某些协议报文攻击或控制网络设备，影响网络的正常运行，可以在设备上配置管理平面接入控制特性，允许或阻止指定的协议报文上送CPU，从而提升设备的安全性和可靠性，保证网络的正常运行。管理平面接入控制策略，可以在全局使能，也可以在接口支持的接口上使能。全局使能简化配置，接口使能可以对各个接入分别定制策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为16。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定创建策略的策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无<br>配置原则：字符串形式，必须指定策略名字。 |
| STEP | 规则间步长 | 可选必选说明：可选参数<br>参数含义：该参数用于指定创建策略的规则间步长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20。<br>默认值：5 |
| DESCRIPTION | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定创建策略的策略描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。字符串区分大小写。<br>默认值：无 |

## 操作的配置对象

- [IPv4 MPAC策略（MPACV4POLICY）](configobject/UNC/20.15.2/MPACV4POLICY.md)

## 使用实例

创建管理平面接入控制策略：

```
ADD MPACV4POLICY:POLICYNAME="policyV4",STEP=19,DESCRIPTION="a test desc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IPv4-MPAC策略（ADD-MPACV4POLICY）_00865697.md`
