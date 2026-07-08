---
id: UDG@20.15.2@ConfigObject@ADCPARA
type: ConfigObject
name: ADCPARA（ADC参数）
nf: UDG
version: 20.15.2
object_name: ADCPARA
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# ADCPARA（ADC参数）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置应用的流信息上报开关。流信息的上报功能是指对于需要进行检测上报的应用，在上报应用开始/结束上报时，同时上报当前业务的流信息，便于PCRF/PCF能够获取到应用与流的对应关系，从而可以下发更精确地策略对业务进行控制。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-ADCPARA]] · ADD ADCPARA
- [[command/UDG/20.15.2/LST-ADCPARA]] · LST ADCPARA
- [[command/UDG/20.15.2/MOD-ADCPARA]] · MOD ADCPARA
- [[command/UDG/20.15.2/RMV-ADCPARA]] · RMV ADCPARA

## 关联对象

- [[configobject/UDG/20.15.2/FLOWFILTER]] · FLOWFILTER

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改ADC参数（MOD-ADCPARA）_01905961.md`
- 原始手册：`evidence/UDG/20.15.2/删除ADC参数（RMV-ADCPARA）_01905962.md`
- 原始手册：`evidence/UDG/20.15.2/增加ADC参数（ADD-ADCPARA）_01905960.md`
- 原始手册：`evidence/UDG/20.15.2/查询ADC参数（LST-ADCPARA）_01905963.md`
