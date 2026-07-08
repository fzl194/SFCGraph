---
id: UNC@20.15.2@MMLCommand@SET NOTIFYRSDPARA
type: MMLCommand
name: SET NOTIFYRSDPARA（设置状态通知失败重传参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NOTIFYRSDPARA
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF通知失败重传开关
status: active
---

# SET NOTIFYRSDPARA（设置状态通知失败重传参数）

## 功能

**适用NF：NRF**

该命令配置了NRF状态通知失败时重传的参数。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NOTIFYRSDSW | NOTIFYRSDTIMER | NOTIFYRSDTIMES | NOTIFYRSDCODE | NOTIFYRSDCAP |
| --- | --- | --- | --- | --- |
| FUNC_ON | 1 | 3 | 429.500.503.504 | 1024 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOTIFYRSDSW | 失败通知重传开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示控制失败通知是否需要重传开关。开关打开后发送失败的通知按一定周期会尝试重新发送，直至发送成功；关闭则不重新发送。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NOTIFYRSDPARA查询当前参数配置值。<br>配置原则：无 |
| NOTIFYRSDTIMER | 失败通知重传周期时长(分钟) | 可选必选说明：可选参数<br>参数含义：该参数用于表示失败通知重传周期的时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10080，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NOTIFYRSDPARA查询当前参数配置值。<br>配置原则：无 |
| NOTIFYRSDTIMES | 失败通知重传最大次数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示失败通知重传最大次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~10080，单位是次。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NOTIFYRSDPARA查询当前参数配置值。<br>配置原则：无 |
| NOTIFYRSDCODE | 失败通知重传状态码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示需要失败通知重传的HTTP状态码，多个错误码用“.”分割。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NOTIFYRSDPARA查询当前参数配置值。<br>配置原则：无 |
| NOTIFYRSDCAP | 失败通知重传消息队列长度 | 可选必选说明：可选参数<br>参数含义：该参数用于表示需要失败通知重传的消息队列长度，当消息队列溢出之后可通过配置队列长度取消内部资源超限告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~10000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NOTIFYRSDPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NOTIFYRSDPARA]] · 状态通知失败重传参数（NOTIFYRSDPARA）

## 使用实例

设置状态通知失败重传参数，打开失败通知重传开关，失败通知重传周期时长设置为30分钟，失败通知重传消息队列长度设置为1024：

```
SET NOTIFYRSDPARA:NOTIFYRSDSW=FUNC_ON,NOTIFYRSDTIMER=30,NOTIFYRSDCAP=1024;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置状态通知失败重传参数（SET-NOTIFYRSDPARA）_25121212.md`
