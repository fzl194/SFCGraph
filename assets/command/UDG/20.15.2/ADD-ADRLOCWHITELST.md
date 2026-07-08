---
id: UDG@20.15.2@MMLCommand@ADD ADRLOCWHITELST
type: MMLCommand
name: ADD ADRLOCWHITELST（添加区域地址分配用户白名单）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ADRLOCWHITELST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 20
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 位置区域地址分配用户白名单
status: active
---

# ADD ADRLOCWHITELST（添加区域地址分配用户白名单）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加位置区域地址分配用户白名单。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为20。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSISDN | MSISDN | 可选必选说明：必选参数<br>参数含义：用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：Msisdn必须为十进制数字，但是不能为19。 |

## 操作的配置对象

- [位置区域地址分配用户白名单（ADRLOCWHITELST）](configobject/UDG/20.15.2/ADRLOCWHITELST.md)

## 使用实例

添加MSISDN为123456用户到位置区域地址分配白名单中：

```
ADD ADRLOCWHITELST: MSISDN="123456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加区域地址分配用户白名单（ADD-ADRLOCWHITELST）_06054824.md`
