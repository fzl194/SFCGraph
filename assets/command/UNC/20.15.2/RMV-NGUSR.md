---
id: UNC@20.15.2@MMLCommand@RMV NGUSR
type: MMLCommand
name: RMV NGUSR（删除5G用户）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGUSR
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# RMV NGUSR（删除5G用户）

## 功能

**适用NF：AMF**

该命令用于删除用户的所有信息。需要主动删除用户时，使用此命令删除用户信息。

## 注意事项

- 该命令执行后立即生效。

- 用户处于稳态或暂态时，都可以执行该命令。
- 删除用户将导致用户正在进行的业务终止，导致用户从网络去注册，请慎重使用此命令。
- 通过该命令隐式去注册用户时，AMF上的用户签约数据将被清除；而如果是显式去注册，用户签约数据都不会被立即清除。另，在隐式去注册定时器超时触发的去注册场景下，用户签约数据也不会被立即清除。
- 通过该命令显式去注册用户时，如果用户为eDRX用户且不在寻呼窗口时，AMF执行隐式去注册流程。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVOPTION | 删除方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定被删除用户的识别码类型。<br>数据来源：全网规划<br>取值范围：<br>- “BYIMSI（指定IMSI）”：指定IMSI<br>- “BYMSISDN（指定MSISDN）”：指定MSISDN<br>- “BYIMEI（指定IMEI）”：指定IMEI<br>- “BYGUTI（指定GUTI）”：指定GUTI<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"RMVOPTION"配置为"BYIMSI"时为条件必选参数。<br>参数含义：该参数用于指定被删除5G用户的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数在“删除方式”设置为“BYIMSI(指定IMSI)”时有效。 |
| MSISDN | MSISDN | 可选必选说明：该参数在"RMVOPTION"配置为"BYMSISDN"时为条件必选参数。<br>参数含义：该参数用于指定被删除5G用户的MSISDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"RMVOPTION"配置为"BYIMEI"时为条件必选参数。<br>参数含义：该参数用于指定被删除5G用户的IMEI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GUTI | 5G-GUTI | 可选必选说明：该参数在"RMVOPTION"配置为"BYGUTI"时为条件必选参数。<br>参数含义：该参数用于指定被删除5G用户的5G-GUTI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是19~20。5G-GUTI的组成为[MCC] + [MNC] + [AMF Region ID] + [AMF Set ID] + [AMF Pointer] + [5G-TMSI]，其中MCC为3个十进制数字，MNC为2-3个十进制数字；AMF Region ID、AMF Set ID和AMF Pointer合成AMF Identifier，使用十六进制（0-9，a-f，A-F）表示，占6个字符；5G-TMSI是AMF内的唯一标识，使用十六进制表示，占8个字符。<br>默认值：无<br>配置原则：无 |
| DEREGMODE | 去注册模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定去注册模式。<br>数据来源：全网规划<br>取值范围：<br>- “EXPLICIT（显式去注册）”：显式去注册<br>- “IMPLICIT（隐式去注册）”：隐式去注册<br>默认值：IMPLICIT<br>配置原则：无 |
| DEREGTYPE | 去注册类型 | 可选必选说明：该参数在"DEREGMODE"配置为"EXPLICIT"时为条件必选参数。<br>参数含义：该参数用于指定去注册类型。<br>数据来源：全网规划<br>取值范围：<br>- “REREG_REQ（需要重新注册）”：用户需要重新注册。<br>- “REREG_NOTREQ（无需重新注册）”：用户无需重新注册。<br>默认值：REREG_NOTREQ<br>配置原则：无 |
| CAUSETYPE | 原因类型 | 可选必选说明：该参数在"DEREGTYPE"配置为"REREG_NOTREQ"时为条件必选参数。<br>参数含义：该参数用于指定去注册的原因值。<br>数据来源：全网规划<br>取值范围：<br>- “CUSTOMER_DEF（自定义原因）”：自定义原因<br>- “ILLEGAL_UE（非法的UE）”：非法的UE<br>- “ILLEGAL_ME（非法的ME）”：非法的ME<br>- “SRV_NOT_ALLOW（5G系统服务拒绝）”：5G系统服务拒绝<br>- “PLMN_NOT_ALLOW（PLMN拒绝）”：PLMN拒绝<br>- “AREA_NOT_ALLOW（TA区域拒绝）”：TA区域拒绝<br>- “ROAM_NOT_ALLOW（区域漫游拒绝）”：区域漫游拒绝<br>- “N1_NOT_ALLOW（N1模式拒绝）”：N1模式拒绝<br>- “PEI_NOT_ALLOW（PEI拒绝）”：PEI拒绝<br>- “UE_UN_DERIVED（无法获取UE标识）”：无法获取UE标识<br>- “IMPLICIT_DEREG（隐式去注册）”：隐式去注册<br>- “NO_CELL_IN_TA（TA内无可用小区）”：TA内无可用小区<br>- “NON_3GPP_NOT_ALLOW（禁止非3gpp接入）”：禁止非3gpp接入<br>默认值：SRV_NOT_ALLOW<br>配置原则：无 |
| CUSCAUSE | 自定义原因 | 可选必选说明：该参数在"CAUSETYPE"配置为"CUSTOMER_DEF"时为条件必选参数。<br>参数含义：该参数用于指定用户自定义的去注册原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是3~255。不建议使用已定义的原因值（如3、5、6、7、9、10、11、12、13、15、27、72）作为自定义原因值。建议顺序取值，便于维护。“自定义原因值”为3GPP协议未定义的原因值，运营商可自行规定这些值的意义。使用时，请运营商自行维护自定义原因值与其意义的对应表。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGUSR]] · 5G用户（NGUSR）

## 使用实例

显式地去注册IMSI为460071104000955的用户，执行如下命令：

```
RMV NGUSR: RMVOPTION=BYIMSI, IMSI="460071104000955", DEREGMODE=EXPLICIT, DEREGTYPE=REREG_REQ;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGUSR.md`
