---
id: UNC@20.15.2@ConfigObject@RCLICIGNSW
type: ConfigObject
name: RCLICIGNSW（注册中心用户数license忽略开关）
nf: UNC
version: 20.15.2
object_name: RCLICIGNSW
object_kind: global_setting
applicable_nf:
- SMSF
status: active
---

# RCLICIGNSW（注册中心用户数license忽略开关）

## 说明

**适用NF：SMSF**

该命令用于设置SMSF/VLR到注册中心进行用户注册时是否忽略注册中心用户数license控制结果。开关打开时SMSF/VLR只根据“融合短信注册用户数”License项控制用户注册，当此license项未超限但注册中心用户数license超限时。

SMSF/VLR仍然向AMF/MME响应注册成功。

## 操作本对象的命令

- [LST RCLICIGNSW](command/UNC/20.15.2/LST-RCLICIGNSW.md)
- [SET RCLICIGNSW](command/UNC/20.15.2/SET-RCLICIGNSW.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询注册中心用户数license忽略开关（LST-RCLICIGNSW）_54815038.md`
- 原始手册：`evidence/UNC/20.15.2/设置注册中心用户数license忽略开关（SET-RCLICIGNSW）_54974858.md`
