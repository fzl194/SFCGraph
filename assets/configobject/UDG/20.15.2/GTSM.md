---
id: UDG@20.15.2@ConfigObject@GTSM
type: ConfigObject
name: GTSM（GTSM全局配置属性）
nf: UDG
version: 20.15.2
object_name: GTSM
object_kind: global_setting
status: active
---

# GTSM（GTSM全局配置属性）

## 说明

该命令用于设置GTSM全局属性。

GTSM（Generalized TTL Security Mechanism），即通用TTL安全保护机制。GTSM通过检查IP报文头中的TTL值是否在一个预先定义好的范围内，对IP层以上业务进行保护。在实际应用中，用于保护建立在TCP/IP基础上的控制层面（路由协议等）免受CPU利用（CPU-utilization）类型的攻击，如CPU过载（CPU overload）。

## 操作本对象的命令

- [LST GTSM](command/UDG/20.15.2/LST-GTSM.md)
- [SET GTSM](command/UDG/20.15.2/SET-GTSM.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询GTSM全局配置属性（LST-GTSM）_00601001.md`
- 原始手册：`evidence/UDG/20.15.2/设置GTSM全局配置属性（SET-GTSM）_00866477.md`
