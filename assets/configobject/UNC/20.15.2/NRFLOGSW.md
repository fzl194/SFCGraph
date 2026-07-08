---
id: UNC@20.15.2@ConfigObject@NRFLOGSW
type: ConfigObject
name: NRFLOGSW（NRF维护日志打印开关）
nf: UNC
version: 20.15.2
object_name: NRFLOGSW
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFLOGSW（NRF维护日志打印开关）

## 说明

![](设置NRF维护日志打印开关（SET NRFLOGSW）_96243172.assets/notice_3.0-zh-cn_2.png)

DISCLOGSW开启且MAXRATE设置过大，将会导致日志打印频繁，引起CPU升高。

**适用NF：NRF**

该命令用于控制NRF中各类维护日志打印。维护日志的内容包括接收请求的时间，请求的参数，响应内容的统计等。维护人员可以根据需求来决定是否打印维护日志。

## 操作本对象的命令

- [LST NRFLOGSW](command/UNC/20.15.2/LST-NRFLOGSW.md)
- [SET NRFLOGSW](command/UNC/20.15.2/SET-NRFLOGSW.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF维护日志打印开关（LST-NRFLOGSW）_96242312.md`
- 原始手册：`evidence/UNC/20.15.2/设置NRF维护日志打印开关（SET-NRFLOGSW）_96243172.md`
