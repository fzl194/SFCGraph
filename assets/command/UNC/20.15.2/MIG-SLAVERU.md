---
id: UNC@20.15.2@MMLCommand@MIG SLAVERU
type: MMLCommand
name: MIG SLAVERU（迁移热备RU）
nf: UNC
version: 20.15.2
verb: MIG
object_keyword: SLAVERU
command_category: 调测类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# MIG SLAVERU（迁移热备RU）

## 功能

![](迁移热备RU（MIG SLAVERU）_00841197.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于将RU组热备迁移到目标RU。

## 注意事项

- 该命令执行后立即生效。
- 该操作会复位被迁移的RU，可能使得RU承载的业务受影响。
- 只有“1主1热备多冷备”仲裁模式的RU组支持迁移热备。
- 非强制迁移时，指定的迁移目的RU必须满足如下条件：（1）RU的CPU使用率<=75%（2）RU的内存使用率<=87% （3）角色为冷备。
- 请先使用非强制迁移的方式进行迁移，当所有的RU CPU使用率超过75%或者内存使用率超过87%的时候，再通过输入参数ISFORCEOPER=TRUE，进行强制迁移。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUGROUPNAME | RU组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定迁移的RU组，请使用DSP RUGROUP命令查询存在的RU组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| DESTRUNAME | 目的RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定迁移目的RU，请使用DSP RUGROUP命令查询RU组内存在的RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。目的RU必须属于指定的RU组。<br>默认值：无 |
| ISFORCEOPER | 强制操作标志 | 可选必选说明：可选参数<br>参数含义：该参数用于强制迁移到目标RU，当迁移的目的RU CPU占用超过50%或者内存占用超过80%时，使用默认迁移方式会失败，可以通过指定该参数为“TRUE”，执行强制迁移。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SLAVERU]] · 迁移热备RU（SLAVERU）

## 使用实例

将RU组热备迁移到目标RU，RU组名称为BG-IPCTRL，目的RU名称为VNRS_IPCTRL_RU_0800：

```
MIG SLAVERU:RUGROUPNAME="BG-IPCTRL",DESTRUNAME="VNRS_IPCTRL_RU_0800";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MIG-SLAVERU.md`
