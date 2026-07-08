---
id: UNC@20.15.2@ConfigObject@NRFIPWHITELST
type: ConfigObject
name: NRFIPWHITELST（NF IP白名单）
nf: UNC
version: 20.15.2
object_name: NRFIPWHITELST
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFIPWHITELST（NF IP白名单）

## 说明

![](增加NF IP白名单（ADD NRFIPWHITELST）_29869620.assets/notice_3.0-zh-cn_2.png)

该命令与NF IP白名单开关SET NRFIPWHITELSTSW配合使用，在IP白名单未设置完成时请勿打开NF IP白名单开关，否则影响未加入到IP白名单中NF的正常注册、去注册、更新及心跳功能。

**适用NF：NRF**

该命令用于向NF IP白名单列表里边增加IP地址段。客户端IP在配置的IP地址段内的NF才允许正常注册、去注册、更新及维持到NRF的心跳。客户端IP不在配置的IP地址段内的NF将无法正常进行上述业务。

该命令与NF IP白名单开关SET NRFIPWHITELSTSW配合使用，在IP白名单未设置完成时请勿打开NF IP白名单开关，否则影响未加入到IP白名单中NF的正常注册、去注册、更新及心跳功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFIPWHITELST]] · ADD NRFIPWHITELST
- [[command/UNC/20.15.2/LST-NRFIPWHITELST]] · LST NRFIPWHITELST
- [[command/UNC/20.15.2/RMV-NRFIPWHITELST]] · RMV NRFIPWHITELST

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF-IP白名单（RMV-NRFIPWHITELST）_75909313.md`
- 原始手册：`evidence/UNC/20.15.2/增加NF-IP白名单（ADD-NRFIPWHITELST）_29869620.md`
- 原始手册：`evidence/UNC/20.15.2/查询NF-IP白名单（LST-NRFIPWHITELST）_29709830.md`
