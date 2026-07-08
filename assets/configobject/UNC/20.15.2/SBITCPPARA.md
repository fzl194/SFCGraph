---
id: UNC@20.15.2@ConfigObject@SBITCPPARA
type: ConfigObject
name: SBITCPPARA（SBI接口TCP控制参数）
nf: UNC
version: 20.15.2
object_name: SBITCPPARA
object_kind: global_setting
status: active
---

# SBITCPPARA（SBI接口TCP控制参数）

## 说明

![](设置SBI接口TCP控制参数（SET SBITCPPARA）_83813644.assets/notice_3.0-zh-cn_2.png)

该参数需要进行全网规划，根据对端的连接能力进行设置，阈值设置过低可能会导致正常的SBI连接失败。

该命令用于设置TCP SYN包流控阈值以及单个IP的最大TCP连接数。TCP SYN报文数量过大，可能导致系统无法接收正常的TCP连接请求。通过该命令设置相关参数可以预防TCP SYN Flood攻击，保护系统正常运行。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SBITCPPARA]] · LST SBITCPPARA
- [[command/UNC/20.15.2/SET-SBITCPPARA]] · SET SBITCPPARA

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SBI接口TCP控制参数（LST-SBITCPPARA）_83972190.md`
- 原始手册：`evidence/UNC/20.15.2/设置SBI接口TCP控制参数（SET-SBITCPPARA）_83813644.md`
