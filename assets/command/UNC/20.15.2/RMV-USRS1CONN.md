---
id: UNC@20.15.2@MMLCommand@RMV USRS1CONN
type: MMLCommand
name: RMV USRS1CONN（删除S1接口用户连接）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRS1CONN
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1接口用户连接
status: active
---

# RMV USRS1CONN（删除S1接口用户连接）

## 功能

**适用网元：MME**

此命令用于删除处于连接态用户的S1口链接。

## 注意事项

- 此命令执行后立即生效。
- 仅当用户处于连接态时可以使用该命令。该命令会导致指定用户暂时中断业务，等用户再次请求业务后恢复。
- 如果用户处于非连接态时使用该命令，会导致命令执行失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVOPTION | 删除方式 | 可选必选说明：可选参数<br>参数含义：待删除用户的识别码类型。<br>取值范围：<br>- “BYIMSI(指定IMSI)”<br>- “BYMSISDN(指定MSISDN)”<br>- “BYGUTI(指定GUTI)”<br>默认值：<br>“BYIMSI(指定IMSI)”<br>说明：在多IMSI功能开启的情况下，不支持根据MSISDN来删除用户S1口链接。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：待删除用户的国际移动用户识别码。由MCC、MNC和MSIN组成，在PLMN中唯一标识用户。<br>前提条件：该参数在<br>“删除方式”<br>配置为<br>“BYIMSI(指定IMSI)”<br>时生效。<br>取值范围：1~15位数字<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>参数含义：待删除用户的国际移动用户电话号码。由CC、NDC和SN组成，用于从CloudEPSN呼叫移动用户。<br>前提条件：该参数在<br>“删除方式”<br>配置为<br>“BYMSISDN(指定MSISDN)”<br>时生效。<br>取值范围：1~15位数字<br>默认值：无 |
| GUTI | GUTI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GUTI号。<br>前提条件：该参数在<br>“删除方式”<br>配置为<br>“BYGUTI(指定GUTI)”<br>后生效。<br>取值范围：19~20位16进制码字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRS1CONN]] · S1接口用户连接（USRS1CONN）

## 使用实例

删除IMSI为123071104000955的用户的S1口连接：

RMV USRS1CONN: RMVOPTION= BYIMSI, IMSI="123071104000955";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-USRS1CONN.md`
