---
id: UNC@20.15.2@MMLCommand@SET NRFNOTIFYPLY
type: MMLCommand
name: SET NRFNOTIFYPLY（设置NRF通知策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFNOTIFYPLY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF通知管理
status: active
---

# SET NRFNOTIFYPLY（设置NRF通知策略）

## 功能

![](设置NRF通知策略（SET NRFNOTIFYPLY）_07649546.assets/notice_3.0-zh-cn_2.png)

当NRF通知策略不为“NORMAL”时，相关NF的数据和状态变化不再通知给对应的订阅者，请谨慎操作。

**适用NF：NRF**

该命令用于设置NRF通知策略。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NOTIFYPLY | INNERNOTIFYPLY |
| --- | --- |
| NORMAL | DEFAULT |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOTIFYPLY | 通知策略 | 可选必选说明：必选参数<br>参数含义：该参数用于设置NRF通知策略。<br>数据来源：本端规划<br>取值范围：<br>- “NORMAL（正常通知）”：NRF正常处理所有通知消息。<br>- “ALLNOT（所有不通知）”：NRF不发送任何通知消息。<br>- “NFINSTANCEIDNOT（指定NF不通知）”： NRF不发送指定NF的变更引发的通知，其中指定NF由ADD NRFNOTNOTIFYNF命令进行配置。<br>默认值：无。<br>配置原则：无 |
| INNERNOTIFYPLY | 内部通知策略 | 可选必选说明：可选参数<br>参数含义：该参数用于设置NRF内部通知策略，仅在SCP和NRF联合部署场景下生效。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（默认策略）”：NRF处理内部通知消息受NOTIFYPLY参数控制。<br>- “NOT（不通知）”：NRF不发送任何内部通知消息。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFNOTIFYPLY查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [NRF通知策略（NRFNOTIFYPLY）](configobject/UNC/20.15.2/NRFNOTIFYPLY.md)

## 使用实例

运营商希望NRF不发送任何通知消息，执行下面命令。

```
SET NRFNOTIFYPLY: NOTIFYPLY=ALLNOT,  INNERNOTIFYPLY=DEFAULT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NRF通知策略（SET-NRFNOTIFYPLY）_07649546.md`
