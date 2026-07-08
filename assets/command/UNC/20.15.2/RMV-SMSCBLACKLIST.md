---
id: UNC@20.15.2@MMLCommand@RMV SMSCBLACKLIST
type: MMLCommand
name: RMV SMSCBLACKLIST（删除SMSC黑名单记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMSCBLACKLIST
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 短消息
- SMSC黑名单
status: active
---

# RMV SMSCBLACKLIST（删除SMSC黑名单记录）

## 功能

**适用网元：SGSN**

该命令用于删除SMSC黑名单中的一条或多条记录。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令时，当参数“SMSC地址”有输入值，表示将删除一条指定的SMSC黑名单记录；当参数“SMSC地址”没有输入值，表示将删除所有SMSC黑名单记录。
- 短消息通信的黑名单拒绝功能的优先级高于[**ADD SMSCCONVERT**](../SMSC转换/增加SMSC转换配置记录(ADD SMSCCONVERT)_72225407.md)命令中实现的纠正短消息中心的功能。即当手机短消息中携带的请求SMSC地址位于黑名单中时，将直接中止短消息流程，而不会继续进行短消息中心纠正后，再次尝试继续进行未完成的短消息流程。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMSCADDR | SMSC地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待删除的位于SMSC黑名单中的SMSC地址。如果手机短消息中携带的请求SMSC地址位于SMSC黑名单中，将中止该短消息流程。<br>取值范围：1~16位十进制字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCBLACKLIST]] · SMSC黑名单记录（SMSCBLACKLIST）

## 使用实例

删除一条SMSC黑名单记录：

RMV SMSCBLACKLIST: SMSCADDR="8613951701";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SMSC黑名单记录(RMV-SMSCBLACKLIST)_26305536.md`
