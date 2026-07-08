---
id: UNC@20.15.2@MMLCommand@ADD SMSCBLACKLIST
type: MMLCommand
name: ADD SMSCBLACKLIST（增加SMSC黑名单记录）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMSCBLACKLIST
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 16
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 短消息
- SMSC黑名单
status: active
---

# ADD SMSCBLACKLIST（增加SMSC黑名单记录）

## 功能

**适用网元：SGSN**

此命令用于增加SMSC黑名单记录。用于短消息通信中黑名单拒绝的功能，即如果手机短消息中携带的请求SMSC地址在黑名单中，将中止该短消息流程。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为16。
- 此命令增加的SMSC黑名单记录只对本地PLMN的用户生效，本地PLMN的配置请参考[**ADD HPLMN**](../../../网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)命令。
- 短消息通信的黑名单拒绝功能的优先级高于[**ADD HPLMN**](../../../网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)命令中实现的纠正短消息中心的功能。即当手机短消息中携带的请求SMSC地址位于黑名单中时，将直接中止短消息流程，而不会继续进行短消息中心纠正后，再次尝试继续进行未完成的短消息流程。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMSCADDR | SMSC地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定加入黑名单中的SMSC地址。如果手机短消息中携带的请求SMSC地址为该参数所配置的<br>“SMSC地址”<br>，将中止该短消息流程。<br>数据来源：整网规划<br>取值范围：1~16位十进制字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSCBLACKLIST]] · SMSC黑名单记录（SMSCBLACKLIST）

## 使用实例

增加一条SMSC黑名单记录：

ADD SMSCBLACKLIST: SMSCADDR="8613951701";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SMSCBLACKLIST.md`
