---
id: UNC@20.15.2@MMLCommand@MOD PCRF
type: MMLCommand
name: MOD PCRF（修改PCRF）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PCRF
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF
status: active
---

# MOD PCRF（修改PCRF）

## 功能

**适用NF：PGW-C、GGSN**

![](修改PCRF（MOD PCRF）_09897102.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改对端信息可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。

此命令用于修改PCRF的基本信息，修改特定的PCRF。

此命令为PCC策略控制的核心配置。

## 注意事项

- 该命令执行后立即生效。
- 修改特定的PCRF时，一定要输入指定PCRF主机名称。
- 可能导致PCRF链路闪断，影响PCC策略控制。
- PCRF绑定到PCRFGroup时，修改该PCRF的动态协商参数会同时修改该PCRFGROUP下所有其他PCRF的协商参数，如果该PCRFGROUP下的某个PCRF同时被其他PCRFGROUP绑定，那么该PCRFGROUP下的PCRF的协商参数也会被刷新。
- 如果PCRF被绑定到DiamConnGrp下，则无法修改其VPNINSTANCE信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | PCRF主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF所在的vpn-instance的实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD VPNINST命令配置生成。 |
| SUPFEANEGOSW | Supported-Features动态协商开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使能Supported-Features动态协商。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：动态协商开关不依赖于是否配置Feature-List。动态协商功能需谨慎开启，如果开启，当PCRF不下或者下发错误Feature-List值时，可能会导致用户激活失败或者相关Feature功能不可用。 |
| CARRYSUPFEASW | Supported-Feature AVP携带开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SUPFEANEGOSW”配置为“DISABLE”时为可选参数。<br>参数含义：该参数用于配置是否在CCR-I消息中携带Supported-Feature AVP。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| FEATURELIST | Feature列表 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要开启的Supported-Features动态协商参数。<br>数据来源：对端协商<br>取值范围：位域类型。<br>- RELEASE8：表示支持3GPP Rel-8 Gx功能。<br>- RELEASE9：表示支持3GPP Rel-9 Gx功能。<br>- RELEASE10：表示支持3GPP Rel-10 Gx功能。<br>- ADC：表示支持应用检测与控制功能。<br>- NETLOC：表示支持接入网信息上报功能。<br>- PROVAFSIGNALFL：表示支持IMS恢复功能。<br>- UMCH：表示支持Usage Monitoring拥塞处理功能。<br>- SGW_REST：表示支持SGW恢复功能。<br>- CNO_ULI：表示支持基于指定区域的策略控制功能。<br>- PENDINGTRANSACTION：表示支持事务等待功能。<br>- PCSCF_RESTORATION_ENHANCEMENT：PCSCF故障恢复增强功能。<br>- EXTENDED_BW_NR：扩展带宽特性。<br>默认值：无<br>配置原则：<br>- 修改完成后，RELEASE8、RELEASE9和RELEASE10必须至少保留一个。<br>- ADC，NETLOC，PROVAFSIGNALFL，UMCH，SGW_REST和CNO_ULI为可选参数，可以根据实际应用场景配置0个或多个。<br>- 动态协商关闭时，如果配置Feature列表，则按照实际的配置与PCRF进行该会话的后续交互。<br>- 动态协商关闭时，UNC设置Feature列表默认值为RELEASE8和RELEASE9，并按照所设置的最高协议版本和PCRF进行交互。<br>- 动态协商使能时，如果不配置Feature列表，UNC按照缺省配置RELEASE8和RELEASE9和PCRF进行协商。<br>- 动态协商使能时，如果配置Feature列表，则UNC使用实际配置的Feature和PCRF进行协商。<br>- UNC会对协商结果进行缓存，按照实际的协商结果与PCRF进行该会话的后续交互，并使用缓存的协商结果发起后续会话与该PCRF的动态协商，以提高协商成功率。 |
| DSCPV | DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCC信令报文的DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～63，255。<br>默认值：无<br>配置原则：该参数配置为255时，表示继承SET LOGIFDSCP设置的全局PCC信令DSCP值。 |
| WALVALUE | wal值 | 可选必选说明：可选参数<br>参数含义：该参数表示UNC每秒发送给该PCRF的最大CCR消息数，超过之后的CCR消息，会被流控处理，但CCR-T消息的发送不受发送窗口限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：该参数配置为0时，表示不控制发送给该PCRF的CCR消息数。 |

## 操作的配置对象

- [PCRF（PCRF）](configobject/UNC/20.15.2/PCRF.md)

## 使用实例

根据网络规划，需要修改PCRF在UNC上规划PCRF的vpn实例vpn2，希望支持和对端进行动态协商，支持协商版本为RELEASE9：

```
MOD PCRF:HOSTNAME="pcrf1",VPNINSTANCE="vpn2",SUPFEANEGOSW=ENABLE,FEATURELIST=RELEASE9-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PCRF（MOD-PCRF）_09897102.md`
