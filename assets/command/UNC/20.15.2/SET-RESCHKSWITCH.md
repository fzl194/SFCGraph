---
id: UNC@20.15.2@MMLCommand@SET RESCHKSWITCH
type: MMLCommand
name: SET RESCHKSWITCH（设置RCF核查开关状态）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RESCHKSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- RCF管理
status: active
---

# SET RESCHKSWITCH（设置RCF核查开关状态）

## 功能

![](设置RCF核查开关状态（SET RESCHKSWITCH）_03794482.assets/notice_3.0-zh-cn_2.png)

关闭RCF核查开关，可能会导致服务间数据不一致。请务必在华为技术支持的指导下使用该命令。

该命令用于开启或关闭RCF核查功能。

## 注意事项

- 如果当前有核查任务正在执行，不会中断当前任务，下次任务再生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH |
| --- |
| ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | RCF核查开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制RCF核查开关状态。<br>数据来源：本端规划<br>取值范围：<br>- ON（打开）<br>- OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESCHKSWITCH]] · RCF核查开关状态（RESCHKSWITCH）

## 使用实例

关闭RCF核查功能。

```
SET RESCHKSWITCH: SWITCH=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-RESCHKSWITCH.md`
