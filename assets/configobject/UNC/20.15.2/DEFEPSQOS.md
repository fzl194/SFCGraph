---
id: UNC@20.15.2@ConfigObject@DEFEPSQOS
type: ConfigObject
name: DEFEPSQOS（EPS缺省QoS参数）
nf: UNC
version: 20.15.2
object_name: DEFEPSQOS
object_kind: global_setting
applicable_nf:
- PGW-C
- SGW-C
status: active
---

# DEFEPSQOS（EPS缺省QoS参数）

## 说明

**适用NF：PGW-C、SGW-C**

该命令用来配置在SAE架构下的缺省QoS参数。当UNC收到GTPv2版本消息中携带的QoS字段不合法时，使用该配置作为缺省值。

PGW-C根据协议检查用户携带的QoS参数的合法性，如果参数非法，则根据该命令配置的缺省QoS参数进行替换。对于各业务类型的相关QoS参数，如果用户请求的QoS属性值为非法值，则QoS协商值等于系统配置值。如果用户请求的QoS属性值为合法值，则QoS协商值等于用户请求值。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DEFEPSQOS]] · LST DEFEPSQOS
- [[command/UNC/20.15.2/SET-DEFEPSQOS]] · SET DEFEPSQOS

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询EPS缺省QoS参数（LST-DEFEPSQOS）_09653169.md`
- 原始手册：`evidence/UNC/20.15.2/设置EPS缺省QoS参数（SET-DEFEPSQOS）_09653732.md`
