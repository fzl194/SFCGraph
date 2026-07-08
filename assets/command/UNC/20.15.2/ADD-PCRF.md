---
id: UNC@20.15.2@MMLCommand@ADD PCRF
type: MMLCommand
name: ADD PCRF（增加PCRF）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PCRF
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF
status: active
---

# ADD PCRF（增加PCRF）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于增加PCRF的基本信息，配置PCRF主机名、域名、VPN实例、PCRF动态协商参数。

此命令为PCC策略控制的核心配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | PCRF主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：该参数不支持与DRA主机名重名。需要与对端PCRF设备配置保持一致。该参数错误，会导致PCRF连接不能建立，PCRF状态异常，PCC策略控制特性无法使用。 |
| REALMNAME | PCRF域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF所在的vpn-instance的实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD VPNINST命令配置生成。 |
| SUPFEANEGOSW | Supported-Features动态协商开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使能Supported-Features动态协商。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：动态协商开关不依赖于是否配置FeatureList。动态协商功能需谨慎开启，如果开启，当PCRF不下或者下发错误FeatureList值时，可能会导致用户激活失败或者相关Feature功能不可用。 |
| CARRYSUPFEASW | Supported-Feature AVP携带开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SUPFEANEGOSW”配置为“DISABLE”时为可选参数。<br>参数含义：该参数用于配置是否在CCR-I消息中携带Supported-Feature AVP。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：ENABLE<br>配置原则：无 |
| FEATURELIST | Feature列表 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要开启的Supported-Features动态协商参数。<br>数据来源：对端协商<br>取值范围：位域类型。<br>- RELEASE8：表示支持3GPP Rel-8 Gx功能。<br>- RELEASE9：表示支持3GPP Rel-9 Gx功能。<br>- RELEASE10：表示支持3GPP Rel-10 Gx功能。<br>- ADC：表示支持应用检测与控制功能。<br>- NETLOC：表示支持接入网信息上报功能。<br>- PROVAFSIGNALFL：表示支持IMS恢复功能。<br>- UMCH：表示支持Usage Monitoring拥塞处理功能。<br>- SGW_REST：表示支持SGW恢复功能。<br>- CNO_ULI：表示支持基于指定区域的策略控制功能。<br>- PENDINGTRANSACTION：表示支持事务等待功能。<br>- PCSCF_RESTORATION_ENHANCEMENT：PCSCF故障恢复增强功能。<br>- EXTENDED_BW_NR：扩展带宽特性。<br>默认值：无<br>配置原则：<br>- RELEASE8、RELEASE9和RELEASE10为必选参数，必须至少设置一个。<br>- ADC，NETLOC，PROVAFSIGNALFL，UMCH，SGW_REST和CNO_ULI为可选参数，可以根据实际应用场景配置0个或多个。<br>- 动态协商关闭时，如果配置Feature列表，则按照实际的配置与PCRF进行该会话的后续交互。<br>- 动态协商关闭时，UNC设置Feature列表默认值为RELEASE8和RELEASE9，并按照所设置的最高协议版本和PCRF进行交互。<br>- 动态协商使能时，如果不配置Feature列表，UNC按照缺省配置RELEASE8、RELEASE9和PCRF进行协商。<br>- 动态协商使能时，如果配置Feature列表，则UNC使用实际配置的Feature和PCRF进行协商。<br>- UNC会对协商结果进行缓存，按照实际的协商结果与PCRF进行该会话的后续交互，并使用缓存的协商结果发起后续会话与该PCRF的动态协商，以提高协商成功率。 |
| DSCPV | DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCC信令报文的DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～63，255。<br>默认值：255<br>配置原则：该参数配置为255时，表示继承SET LOGIFDSCP设置的全局PCC信令DSCP值。 |
| WALVALUE | wal值 | 可选必选说明：可选参数<br>参数含义：该参数表示UNC每秒发送给该PCRF的最大CCR消息数，超过之后的CCR消息，会被流控处理，但CCR-T消息的发送不受发送窗口限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：0<br>配置原则：该参数配置为0时，表示不控制发送给该PCRF的CCR消息数。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCRF]] · PCRF（PCRF）

## 使用实例

根据网络规划，需要新增一个PCRF在域www.huawei.com上激活动态PCC用户，在UNC上规划PCRF的vpn实例vpn1，希望支持和对端进行动态协商，支持协商版本为RELEASE8：

```
ADD PCRF:HOSTNAME="pcrf1",REALMNAME="www.huawei.com",VPNINSTANCE="vpn1",SUPFEANEGOSW=ENABLE,FEATURELIST=RELEASE8-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PCRF.md`
