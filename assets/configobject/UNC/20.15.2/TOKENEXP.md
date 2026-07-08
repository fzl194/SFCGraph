---
id: UNC@20.15.2@ConfigObject@TOKENEXP
type: ConfigObject
name: TOKENEXP（Token有效期）
nf: UNC
version: 20.15.2
object_name: TOKENEXP
object_kind: entity
applicable_nf:
- NRF
status: active
---

# TOKENEXP（Token有效期）

## 说明

**适用NF：NRF**

该命令用于增加NF的Token有效期。当运营商希望新增对应NF类型/NF实例的Token有效期时长时可以使用此命令。

安全层面考虑，NF请求提供某种服务时需要获取授权，以预防和降低权限提升风险。5GC网络的NF间的服务化接口采用Oauth2.0动态Token授权以保证安全，Token可以理解为NF请求访问某服务使用的短期令牌，当且仅当手持令牌时，才能获取所需服务。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-TOKENEXP]] · ADD TOKENEXP
- [[command/UNC/20.15.2/LST-TOKENEXP]] · LST TOKENEXP
- [[command/UNC/20.15.2/MOD-TOKENEXP]] · MOD TOKENEXP
- [[command/UNC/20.15.2/RMV-TOKENEXP]] · RMV TOKENEXP

## 证据

- 原始手册：`evidence/UNC/20.15.2/TOKENEXP.md`
- 原始手册：`evidence/UNC/20.15.2/TOKENEXP.md`
- 原始手册：`evidence/UNC/20.15.2/TOKENEXP.md`
- 原始手册：`evidence/UNC/20.15.2/TOKENEXP.md`
