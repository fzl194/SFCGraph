---
id: UNC@20.15.2@MMLCommand@ADD NRFPLMNVISITPLY
type: MMLCommand
name: ADD NRFPLMNVISITPLY（增加指定归属地PLMN的拜访地策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFPLMNVISITPLY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# ADD NRFPLMNVISITPLY（增加指定归属地PLMN的拜访地策略）

## 功能

**适用NF：NRF**

该命令用于增加NRF作为拜访地NRF时对指定归属地PLMN的跨PLMN交互处理策略。

## 注意事项

- 该命令执行后立即生效。

- 若对某归属地PLMN没有配置本命令中的策略，以SET NRFVISITPLY配置的默认策略为准。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定归属地PLMN的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定归属地PLMN的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| INTERSUBSW | 是否支持跨PLMN订阅 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF作为拜访地NRF时，是否处理NF发起的对指定归属地PLMN的跨PLMN订阅以及订阅更新请求。开关为FUNC_ON表示处理，开关为FUNC_OFF表示不处理，并返回403错误码。<br>数据来源：全网规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：FUNC_ON<br>配置原则：无 |
| SUBLOCMODSW | 订阅是否进行Location改造 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF作为拜访地NRF收到指定归属地PLMN的跨PLMN的订阅响应时是否对响应头中Location进行改造。<br>该参数设置为“FUNC_ON”表示进行Location改造，NRF会把跨PLMN的订阅响应头中的Location的apiRoot部分替换为本NRF的，订阅ID部分增加归属地PLMN ID前缀，然后再转发给前一跳。该参数设置为“FUNC_OFF”表示不进行Location改造，NRF保持Location不变透传给前一跳，后续NF的订阅更新和去订阅请求会直接发给归属地NRF，不再经过拜访地NRF转发。<br>数据来源：全网规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：FUNC_OFF<br>配置原则：无 |
| SUBDELPLMNSW | 订阅转发是否删除PLMN | 可选必选说明：可选参数<br>参数含义：该参数不生效。该参数用于表示本NRF作为拜访地NRF对于指定归属地PLMN转发跨PLMN订阅更新、去订阅时是否删除URI中订阅ID包含的归属地PLMN ID后再进行转发。<br>数据来源：全网规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：FUNC_OFF<br>配置原则：<br>非国际漫游关口局NRF需要配置为FUNC_ON，国际漫游关口局NRF需要配置为FUNC_OFF。 |
| HPLMNCUTSW | 跨PLMN转发是否剥离目的PLMN | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF作为拜访地NRF时，对于跨PLMN的服务发现和订阅请求是否删除目标PLMN参数后转发。<br>开关打开表示删除目标PLMN参数后转发。开关关闭表示不删除转发。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：FUNC_OFF<br>配置原则：<br>非国际漫游关口局NRF需要配置为FUNC_OFF，国际漫游关口局NRF按需打开。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFPLMNVISITPLY]] · 指定归属地PLMN的拜访地策略（NRFPLMNVISITPLY）

## 使用实例

新增一条指定归属地PLMN的拜访地策略，移动国家码为460，移动网号为03，支持跨PLMN订阅。

```
ADD NRFPLMNVISITPLY: MCC="460", MNC="03", INTERSUBSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NRFPLMNVISITPLY.md`
