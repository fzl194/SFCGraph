---
id: UDG@20.15.2@MMLCommand@ADD NPDIRECTCONNECTPORT
type: MMLCommand
name: ADD NPDIRECTCONNECTPORT（增加多框级联配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: NPDIRECTCONNECTPORT
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# ADD NPDIRECTCONNECTPORT（增加多框级联配置）

## 功能

![](增加多框级联配置（ADD NPDIRECTCONNECTPORT）_38407891.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，仅适用于NP多框场景或者NP单框改造成NP多框场景，错误配置可能会造成业务流量损失，请谨慎使用并联系华为技术支持协助操作。

该命令用于新增一条多框级联配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅适用于NP卡加速模式场景，并且该命令在非省交换场景下不能执行。
> - 该命令在NP卡名称（通过DSP NPNODE查询）为NP121时不生效。
> - 该命令不适用于单框场景。执行该命令后，对应的外联口会变成级联口，请谨慎使用。
> - 通过MOD INTERFACE命令操作级联口，可能导致ALM-139591683 接口状态down误告警，需要手动清除。
>
> - 最多可输入100条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRACK | 框号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示多框级联配置的框号。<br>数据来源：本端规划<br>取值范围：<br>- Subrack_0（0）<br>- Subrack_1（1）<br>- Subrack_2（2）<br>默认值：无<br>配置原则：无 |
| SLOTID | 槽位号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示多框级联配置的槽位号。<br>数据来源：本端规划<br>取值范围：<br>- Slot_1（1）<br>- Slot_2（2）<br>- Slot_3（3）<br>- Slot_4（4）<br>- Slot_5（5）<br>- Slot_6（6）<br>- Slot_7（7）<br>- Slot_8（8）<br>默认值：无<br>配置原则：无 |
| PORTID | 端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示多框级联配置的端口号。<br>数据来源：本端规划<br>取值范围：<br>- P1（P1）<br>- P2（P2）<br>- P3（P3）<br>- P4（P4）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NPDIRECTCONNECTPORT]] · 多框级联配置（NPDIRECTCONNECTPORT）

## 使用实例

新增一条框号为0，槽号为1，端口号为P1的级联口配置：

```
ADD NPDIRECTCONNECTPORT: SUBRACK=Subrack_0, SLOTID=Slot_1, PORTID=P1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-NPDIRECTCONNECTPORT.md`
