---
id: UDG@20.15.2@MMLCommand@STR PAEFABDETECT
type: MMLCommand
name: STR PAEFABDETECT（启动Fabric链路探测任务）
nf: UDG
version: 20.15.2
verb: STR
object_keyword: PAEFABDETECT
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 链路探测
status: active
---

# STR PAEFABDETECT（启动Fabric链路探测任务）

## 功能

该命令用于触发Fabric平面链路状态探测。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令会增加fabric平面链路报文转发开销，请谨慎执行。
> - SRCPODNAME、DSTPODNAME任一不存在时，开启命令执行成功，但开启任务不生效。
> - 下发命令前请确保两个端口之间存在链路（处在同一fabric平面），可使用命令[**DSP FABRICOAMPORT**](../Fabric/显示PAE各链路OAM报文统计结果（DSP FABRICOAMPORT）_92520009.md)或[**DSP PAEFABRICLINK**](../Fabric/显示PAE链路信息（DSP PAEFABRICLINK）_92520014.md)查询链路信息。
> - 正在探测时重复开启同一任务，原任务将被重置。
> - 并行限制：一个pod不支持作为源端同时参与两个探测任务，其他场景支持并行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCPODNAME | 源Pod名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| DSTPODNAME | 目的Pod名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定远端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| SRCPORTNAME | 源端口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |
| DSTPORTNAME | 目的端口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定远端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |
| DURATION | 探测时长 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Fabric链路探测任务的持续时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是300~86400，单位是秒。<br>默认值：300<br>配置原则：无 |
| PKTLENGTH | 探测包长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送的探测报文负载字节数。<br>数据来源：本端规划<br>取值范围：<br>- “PKTLENGTH_256（报文长度256字节）”：报文长度256字节<br>- “PKTLENGTH_512（报文长度512字节）”：报文长度512字节<br>- “PKTLENGTH_1024（报文长度1024字节）”：报文长度1024字节<br>- “PKTLENGTH_1500（报文长度1500字节）”：报文长度1500字节<br>默认值：PKTLENGTH_512<br>配置原则：无 |
| INTERVAL | 间隔 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送探测报文的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~1000，单位是毫秒。<br>默认值：200<br>配置原则：无 |
| DYEFLAG | 染色标记位 | 可选必选说明：可选参数<br>参数含义：指定发送探测报文的染色标记类型。<br>数据来源：本端规划<br>取值范围：<br>- ETHTYPE（以太类型）<br>- OAMTYPE（OAM类型）<br>默认值：ETHTYPE<br>配置原则：<br>如果交换机支持以太类型过滤规则，选择ETHTYPE。如果交换机不支持以太类型过滤规则，选择OAMTYPE。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PAEFABDETECT]] · Fabric链路探测任务（PAEFABDETECT）

## 使用实例

开启Fabric链路探测任务：

```
+++    UNC/*MEID:0 MENAME:UNC_X86_20250307_107*/        2025-03-07 15:40:54
O&M    #52
%%STR PAEFABDETECT: SRCPODNAME="vup-pod-1", DSTPODNAME="vusn-pod-0", SRCPORTNAME="uio0", DSTPORTNAME="uio0", PKTLENGTH=PKTLENGTH_512, DYEFLAG=ETHTYPE;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/STR-PAEFABDETECT.md`
