---
id: UDG@20.15.2@MMLCommand@SET URRFAILACTION
type: MMLCommand
name: SET URRFAILACTION（设置URR上报失败后的动作处理参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: URRFAILACTION
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 计费URR上报失败时的处理动作
status: active
---

# SET URRFAILACTION（设置URR上报失败后的动作处理参数）

## 功能

**适用NF：UPF**

![](设置URR上报失败后的动作处理参数（SET URRFAILACTION）_42746595.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令可能会导致漏计费风险，执行前请参考命令行帮助文档知悉风险，并确认已获得授权。

本条命令用于设置计费URR上报失败的动作。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 当业务部署调整导致UPF上的ADD URR在SMF上不存在时(比如，先添加UPF上ADD URR，后添加SMF上ADD URR)，会导致SMF无法处理UPF的计费用量上报。为减小该场景下对用户业务的影响，可通过该命令设置UPF向SMF进行的计费用量上报失败时的处理动作。在业务部署调整完成后，UPF可以通过尝试，及时恢复业务。当失败动作设置为“CONTINUE”时，URR对应的业务将不计费。在UPF向SMF进行用量上报恢复后，将恢复对该URR的计费。该命令在离线计费新业务场景和在线计费需要申请配额的场景下生效。
- 建议设置的重发间隔（RETRYINTERVAL）乘以重发次数（RETRYTIMES）大于SMF向CHF/OCS申请配额的最大超时时长。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RETRYINTERVAL | RETRYTIMES | RETRYFAILACT | HOLDINGTIME |
| --- | --- | --- | --- | --- |
| 初始值 | 60 | 2 | BLOCK | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RETRYINTERVAL | 重发间隔 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF向SMF上报用量后等待SMF更新URR的超时时长。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为10～120，单位是秒。<br>默认值：无<br>配置原则：无 |
| RETRYTIMES | 重发次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF向SMF上报用量后等待SMF更新URR超时后的重发次数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～10。<br>默认值：无<br>配置原则：无 |
| RETRYFAILACT | 重发失败后的动作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF向SMF上报用量后等待SMF更新URR超时重发失败后的处理动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CONTINUE：系统业务放通。<br>- BLOCK：系统业务阻塞。<br>- TERMINATE：系统业务终止。<br>默认值：无<br>配置原则：无 |
| HOLDINGTIME | 保持时长 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RETRYFAILACT”配置为“BLOCK” 或 “CONTINUE”时为可选参数。<br>参数含义：该参数用于指定UPF向SMF重发用量上报超时后动作为阻塞或放通业务时的保持时长。保持时长超时后，重新触发START Trigger上报。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～60，单位是分钟。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/URRFAILACTION]] · 计费URR上报失败动作参数（URRFAILACTION）

## 关联任务

- [[UDG@20.15.2@Task@0-00018]]

## 使用实例

若要配置重试间隔为10s，重试次数为10次，重试失败动作为阻塞，保持时长为10分钟：

```
SET URRFAILACTION: RETRYINTERVAL=10, RETRYTIMES=10, RETRYFAILACT=BLOCK, HOLDINGTIME=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-URRFAILACTION.md`
