---
id: UNC@20.15.2@MMLCommand@MOD SMSCCONVERT
type: MMLCommand
name: MOD SMSCCONVERT（修改SMSC转换配置记录）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SMSCCONVERT
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
- SMSC转换
status: active
---

# MOD SMSCCONVERT（修改SMSC转换配置记录）

## 功能

**适用网元：SGSN**

此命令用于修改一条SMSC转换记录。用于短消息通信中纠正短消息中心的功能。

## 注意事项

- 此命令执行后立即生效。
- 此命令只能修改“转换SMSC地址”和“描述”。
- 此命令增加的SMSC转换记录只对本地PLMN的用户生效，本地PLMN的配置请参考[**ADD HPLMN**](../../../网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)命令。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REQADDR | 请求SMSC地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定请求SMSC地址。<br>“请求SMSC地址”<br>是手机短消息中携带的请求SMSC地址。<br>数据来源：整网规划<br>取值范围：1～16位十进制字符串<br>默认值：无 |
| CORRADDR | 转换SMSC地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定转换SMSC地址。<br>“转换SMSC地址”<br>将手机短消息中的SMSC地址转化为该参数设置的值。<br>数据来源：整网规划<br>取值范围：1～16位十进制字符串<br>默认值：无<br>说明：“转换SMSC地址”<br>的优先级高于<br>[**ADD HPLMN**](../../../网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)<br>命令中的<br>“纠正后的短消息中心”<br>的优先级。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMSC转换配置记录名称。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCCONVERT]] · SMSC转换配置记录（SMSCCONVERT）

## 使用实例

修改一条SMSC转换配置记录：

MOD SMSCCONVERT: REQADDR="8613951701", CORRADDR="8613951996", DESC="FOR MSC2";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SMSC转换配置记录(MOD-SMSCCONVERT)_72345325.md`
