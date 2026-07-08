---
id: UNC@20.15.2@MMLCommand@SET SMAMEVTEXPPLY
type: MMLCommand
name: SET SMAMEVTEXPPLY（设置SMF向AMF下发事件订阅时的老化策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMAMEVTEXPPLY
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置上报管理
- 老化时间管理
status: active
---

# SET SMAMEVTEXPPLY（设置SMF向AMF下发事件订阅时的老化策略）

## 功能

**适用NF：SMF**

该命令用于设置，当SMF向AMF下发事件订阅时，是否携带老化时间，以及老化时间的时长。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| EXPIRYSW | EXPIRYPERIOD |
| --- | --- |
| DISABLE | 1440 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXPIRYSW | 下发老化时间开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SMF向AMF下发事件订阅时，请求消息是否携带老化时间。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：无 |
| EXPIRYPERIOD | 老化时间时长（min） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF向AMF下发事件订阅时携带老化时间的时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~12000，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMAMEVTEXPPLY查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [SMF向AMF下发事件订阅时的老化策略（SMAMEVTEXPPLY）](configobject/UNC/20.15.2/SMAMEVTEXPPLY.md)

## 使用实例

设置SMF向AMF下发事件订阅时，携带老化时间，并且时长设置为1440分钟：

```
SET SMAMEVTEXPPLY: EXPIRYSW=ENABLE, EXPIRYPERIOD=1440;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMF向AMF下发事件订阅时的老化策略（SET-SMAMEVTEXPPLY）_14059377.md`
