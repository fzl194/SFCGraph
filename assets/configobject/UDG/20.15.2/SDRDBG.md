---
id: UDG@20.15.2@ConfigObject@SDRDBG
type: ConfigObject
name: SDRDBG（SDR调试信息）
nf: UDG
version: 20.15.2
object_name: SDRDBG
object_kind: query_target
status: active
---

# SDRDBG（SDR调试信息）

## 说明

该命令用于显示SDR信息。

> **说明**
> - 如果调试信息发送对象下没有SDR模块，但是又查询该模块下的调试信息，则返回无数据。
> - 当前版本不支持此命令SDR Module参数的BDRA、FCA、SDRA_C取值；不支持操作类型参数的SDR策略、SDR传输速率取值。操作类型选择SDR有界邮箱计数统计时SDR Module参数必须选择SDRA。
> - 本命令只用于查询SDR丢包数量、SDR计数统计和SDR有界邮箱计数统计，若要查询SDR策略，请使用[**DSP SDRSAPPTYPE**](../策略查询/显示SDRS中的APPTYPE信息（DSP SDRSAPPTYPE）_05545720.md)、[**DSP SDRSMASTERNODE**](../策略查询/显示HAF向SDRS推送的主节点信息（DSP SDRSMASTERNODE）_05225906.md)、[**DSP SDRSROUTE**](../策略查询/显示SDRS中的APPROUTEINFO信息（DSP SDRSROUTE）_43960913.md)、[**DSP SDRSTOKEN**](../策略查询/显示SDRS中的TOKEN信息（DSP SDRSTOKEN）_45749059.md)、[**DSP SDRSVPN**](../策略查询/显示SDRS中的VPN信息（DSP SDRSVPN）_10972324.md)命令。

## 操作本对象的命令

- [DSP SDRDBG](command/UDG/20.15.2/DSP-SDRDBG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示SDR调试信息（DSP-SDRDBG）_94730428.md`
