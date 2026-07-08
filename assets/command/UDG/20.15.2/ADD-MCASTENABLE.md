---
id: UDG@20.15.2@MMLCommand@ADD MCASTENABLE
type: MMLCommand
name: ADD MCASTENABLE（添加组播使能）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: MCASTENABLE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MGMD
- 组播使能配置
status: active
---

# ADD MCASTENABLE（添加组播使能）

## 功能

该命令用于添加组播使能配置。

只有在公网实例或VPN实例下使能组播功能，才能配置该实例下的其它所有组播命令。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1024。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MCASTENABLE]] · 组播使能配置（MCASTENABLE）

## 使用实例

添加组播使能配置：

```
ADD MCASTENABLE:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-MCASTENABLE.md`
