---
id: UNC@20.15.2@ConfigObject@RDSAUTHRSPATTR
type: ConfigObject
name: RDSAUTHRSPATTR（支持的Radius鉴权响应消息私有属性）
nf: UNC
version: 20.15.2
object_name: RDSAUTHRSPATTR
object_kind: global_setting
applicable_nf:
- PGW-C
- GGSN
- SMF
status: active
---

# RDSAUTHRSPATTR（支持的Radius鉴权响应消息私有属性）

## 说明

**适用NF：PGW-C、GGSN、SMF**

该命令用于配置是否支持解析RADIUS鉴权服务器组返回的运营商私有信元。对于RADIUS鉴权服务器返回的鉴权响应消息中携带的运营商私有信元，通过该命令配置是否对其进行解析处理。

## 操作本对象的命令

- [LST RDSAUTHRSPATTR](command/UNC/20.15.2/LST-RDSAUTHRSPATTR.md)
- [SET RDSAUTHRSPATTR](command/UNC/20.15.2/SET-RDSAUTHRSPATTR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询支持的Radius鉴权响应消息私有属性（LST-RDSAUTHRSPATTR）_28567654.md`
- 原始手册：`evidence/UNC/20.15.2/设置支持的Radius鉴权响应消息私有属性（SET-RDSAUTHRSPATTR）_28567663.md`
