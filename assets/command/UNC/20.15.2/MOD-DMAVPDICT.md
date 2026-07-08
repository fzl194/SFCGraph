---
id: UNC@20.15.2@MMLCommand@MOD DMAVPDICT
type: MMLCommand
name: MOD DMAVPDICT（修改Diameter数据字典中的AVP参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DMAVPDICT
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 业务调测
- Diameter AVP表
status: active
---

# MOD DMAVPDICT（修改Diameter数据字典中的AVP参数）

## 功能

**适用网元：SGSN、MME**

该命令用于修改Diameter数据字典中的AVP参数。

当MME与HSS之间的协议版本不一致导致的对接失败时，可以执行此命令来修改Diameter数据字典中的AVP参数以解决HSS无法识别 UNC 发送的ULR消息的RAT-Type的信元问题。

## 注意事项

该命令执行后立即生效。

该命令只适用于“S6a/S6d”接口的AVP。

该命令修改涉及参数AVPNAME、AVPCODE、VENDORID时，如果与现有记录不一样会插入新记录，记录最大规格为128条。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DICTNAME | 字典名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter数据字典名称。<br>数据来源：整网规划<br>取值范围：0~65535<br>默认值：无<br>说明：“S6a/S6d”接口对应的字典名称固定取值为6。 |
| AVPNAME | 信元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信元名称。<br>数据来源：整网规划<br>取值范围：0~65535<br>默认值：无 |
| AVPCODE | 信元编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信元编码。<br>数据来源：整网规划<br>取值范围：0~4294967294<br>默认值：无<br>说明：AVP代码连同Vendor-ID字段一起来唯一地标识属性。代码1~255保留，用于保证和RADIUS向后兼容。255以上的代码为Diameter所用，由IANA分配。 |
| VENDORID | Vendor标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定厂商ID字段。<br>数据来源：整网规划<br>取值范围：0~4294967294<br>默认值：无<br>说明：厂商ID字段为可选字段，当“V”比特设置为1时才出现。 |
| AVPTYPE | 信元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信元类型。<br>数据来源：整网规划<br>取值范围：<br>- “DIAM_AVP_TYPE_UINT32(DIAM_AVP_TYPE_UINT32)”<br>- “DIAM_AVP_TYPE_UINT64(DIAM_AVP_TYPE_UINT64)”<br>- “DIAM_AVP_TYPE_INT32(DIAM_AVP_TYPE_INT32)”<br>- “DIAM_AVP_TYPE_INT64(DIAM_AVP_TYPE_INT64)”<br>- “DIAM_AVP_TYPE_OCTETSTR(DIAM_AVP_TYPE_OCTETSTR)”<br>- “DIAM_AVP_TYPE_ENUM(DIAM_AVP_TYPE_ENUM)”<br>- “DIAM_AVP_TYPE_DIAMIDENT(DIAM_AVP_TYPE_DIAMIDENT)”<br>- “DIAM_AVP_TYPE_DIAMURI(DIAM_AVP_TYPE_DIAMURI)”<br>- “DIAM_AVP_TYPE_GROUP(DIAM_AVP_TYPE_GROUP)”<br>- “DIAM_AVP_TYPE_TIME(DIAM_AVP_TYPE_TIME)”<br>- “DIAM_AVP_TYPE_ADDRESS(DIAM_AVP_TYPE_ADDRESS)”<br>- “DIAM_AVP_TYPE_UTF8STR(DIAM_AVP_TYPE_UTF8STR)”<br>- “DIAM_AVP_TYPE_IPFILTERRULE(DIAM_AVP_TYPE_IPFILTERRULE)”<br>- “DIAM_AVP_TYPE_QOSFILTERRULE(DIAM_AVP_TYPE_QOSFILTERRULE)”<br>- “DIAM_AVP_TYPE_OLD_IPV4(DIAM_AVP_TYPE_OLD_IPV4)”<br>- “DIAM_AVP_TYPE_FLOAT32(DIAM_AVP_TYPE_FLOAT32)”<br>- “DIAM_AVP_TYPE_FLOAT64(DIAM_AVP_TYPE_FLOAT64)”<br>- “DIAM_AVP_TYPE_LAST(DIAM_AVP_TYPE_LAST)”<br>默认值：无 |
| AVPFLAG | 信元标记 | 可选必选说明：必选参数<br>参数含义：该参数用于指定AVP标志。<br>数据来源：整网规划<br>取值范围：<br>- “DIAM_AVP_FLAG_MAY_M_PRESENT(DIAM_AVP_FLAG_MAY_M_PRESENT)”<br>- “DIAM_AVP_FLAG_P_PRESENT(DIAM_AVP_FLAG_P_PRESENT)”<br>- “DIAM_AVP_FLAG_M_PRESENT(DIAM_AVP_FLAG_M_PRESENT)”<br>- “DIAM_AVP_FLAG_V_PRESENT(DIAM_AVP_FLAG_V_PRESENT)”<br>默认值：无<br>说明：- DIAM_AVP_FLAG_V_PRESENT：表明了AVP头部是否包括可选字段Vendor-ID。设为1时，表示AVP编码属于厂商专用的地址空间。<br>- DIAM_AVP_FLAG_M_PRESENT：表示了是否需要支持该AVP。如果Diameter节点接收到的消息的AVP“M”比特设置为1又无法被识别，该消息将被拒绝。Diameter中继代理和重定向代理不能拒绝带有无法识别的“M”位的AVP。<br>- DIAM_AVP_FLAG_P_PRESENT：设为1时，表示需要端到端的安全加密。<br>- DIAM_AVP_FLAG_MAY_M_PRESENT：表示发送消息时AVP Header中的M bit不置位，接收消息时不检查AVP Header中的M bit。 |

## 操作的配置对象

- [Diameter数据字典中的AVP参数（DMAVPDICT）](configobject/UNC/20.15.2/DMAVPDICT.md)

## 使用实例

修改Diameter数据字典:

MOD DMAVPDICT: AVPNAME=129, AVPCODE=1032, VENDORID=10415, AVPTYPE=DIAM_AVP_TYPE_ADDRESS, AVPFLAG=DIAM_AVP_FLAG_MAY_M_PRESENT-0&DIAM_AVP_FLAG_M_PRESENT-0&DIAM_AVP_FLAG_P_PRESENT-0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter数据字典中的AVP参数(MOD-DMAVPDICT)_26305668.md`
