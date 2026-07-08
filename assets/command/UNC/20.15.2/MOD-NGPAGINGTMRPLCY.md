---
id: UNC@20.15.2@MMLCommand@MOD NGPAGINGTMRPLCY
type: MMLCommand
name: MOD NGPAGINGTMRPLCY（修改5G寻呼定时器策略配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGPAGINGTMRPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG寻呼定时器策略管理
status: active
---

# MOD NGPAGINGTMRPLCY（修改5G寻呼定时器策略配置）

## 功能

**适用NF：AMF**

该命令用于修改NG寻呼定时器策略配置数据。

## 注意事项

- 该命令执行后立即生效。

- 不能为相同的DNN，FQI，ARP和PPI指定多个寻呼定时器策略。对于指定的TAList，该命令配置之后，使用SET NGMMPARA命令配置的T3513(秒)，N3513(次数)，重寻呼间隔递增值(s)将失效。
- 当用户所在TALIST的TAC在ADD NGTALISTPAGINGCFG配置的指定TAC区间范围内，则AMF不重发用户基于TALIST的寻呼，MOD NGPAGINGTMRPLCY命令配置的T3513(秒)，N3513(次数)将失效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLCYIDX | 策略索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在AMF中唯一标识一条寻呼定时器策略。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1999。<br>默认值：无<br>配置原则：无 |
| T3513 | T3513(s) | 可选必选说明：可选参数<br>参数含义：此定时器用于控制AMF发起寻呼与UE响应的时间间隔。此定时器在AMF发送Paging Request消息后启动，在收到Service Request消息后停止；超时后，AMF重发Paging Request消息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是3~12，单位是秒。<br>默认值：无<br>配置原则：无 |
| N3513 | N3513(times) | 可选必选说明：可选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到UE的响应消息，AMF重复发送Paging Request消息的最大次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~5，单位是次。<br>默认值：无<br>配置原则：无 |
| PAGINGDELTA | 重寻呼间隔递增值(s) | 可选必选说明：可选参数<br>参数含义：该参数用于指定在寻呼流程中，没有收到Service Request消息，AMF重复发送Paging Request消息的间隔递增时间值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~20，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGPAGINGTMRPLCY]] · 5G寻呼定时器策略配置（NGPAGINGTMRPLCY）

## 使用实例

修改一条策略索引为1的NG寻呼定时器策略配置，将T3513修改为3，执行如下命令：

```
MOD NGPAGINGTMRPLCY: PLCYIDX=1,T3513=3;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NGPAGINGTMRPLCY.md`
