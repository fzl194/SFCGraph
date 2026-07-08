---
id: UNC@20.15.2@ConfigObject@TOKENALG
type: ConfigObject
name: TOKENALG（Token签名算法）
nf: UNC
version: 20.15.2
object_name: TOKENALG
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# TOKENALG（Token签名算法）

## 说明

**适用NF：NRF**

NF服务消费者获取到Token后，携带Token访问NF服务提供方的服务。NF服务提供方会对NF服务消费者进行认证，校验Token是否正确，校验过程中NF会使用到公钥和NRF侧配置的Token签名算法。

此命令用于设置NRF上Token的签名算法。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-TOKENALG]] · LST TOKENALG
- [[command/UNC/20.15.2/SET-TOKENALG]] · SET TOKENALG

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Token签名算法（LST-TOKENALG）_09652335.md`
- 原始手册：`evidence/UNC/20.15.2/设置Token签名算法（SET-TOKENALG）_09653632.md`
