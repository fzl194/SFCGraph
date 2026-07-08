---
id: UNC@20.15.2@MMLCommand@MOD REALMBINDAPN
type: MMLCommand
name: MOD REALMBINDAPN（修改APN与Diameter Realm关联关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: REALMBINDAPN
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter Realm
- Realm绑定APN
status: active
---

# MOD REALMBINDAPN（修改APN与Diameter Realm关联关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改APN对应的Diameter域信息，或指定根据IMSI构造Diameter域信息。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要与Diameter域绑定的APN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN绑定Diameter域的Diameter应用类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- GY：Gy接口应用。<br>- GX：Gx接口应用。<br>- S6B：S6b接口应用。<br>默认值：无<br>配置原则：无 |
| CONSTBYIMSISW | 根据IMSI构造归属地Realm开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否使能根据IMSI构造Peer的归属地域名。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：当选择ENABLE时，将通过IMSI构造Diameter域，构造格式为“epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。 |
| REALMNAME | Realm名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONSTBYIMSISW”配置为“DISABLE”时为必选参数。<br>参数含义：该参数用于指定与APN关联的Diameter域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：<br>- 当根据IMSI构造归属地Realm开关设置为ENABLE时，该参数无效。<br>- 当根据IMSI构造归属地Realm开关设置为DISABLE时，必须手动指定Diameter域。 |
| SUPFTNEGOSW | Supported-Features动态协商开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“APPLICATION”配置为“GX”时为可选参数。<br>参数含义：该参数用于指定是否使能Gx应用的Supported-Features动态协商。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：该参数在3GPP-EPS接入场景下生效，3GPP-GPRS接入场景下不生效。 |
| FEATURELIST | Feature列表 | 可选必选说明：条件可选参数<br>前提条件：该参数在“APPLICATION”配置为“GX”时为可选参数。<br>参数含义：该参数用于指定要开启的Supported-Features动态协商参数。<br>数据来源：对端协商<br>取值范围：位域类型。<br>- RELEASE8：表示支持3GPP Rel-8 Gx功能。<br>- RELEASE9：表示支持3GPP Rel-9 Gx功能。<br>- RELEASE10：表示支持3GPP Rel-10 Gx功能。<br>- ADC：表示支持应用检测与控制功能。<br>- NETLOC：表示支持接入网信息上报功能。<br>- PROVAFSIGNALFL：表示支持IMS恢复功能。<br>- UMCH：表示支持Usage Monitoring拥塞处理功能。<br>- SGW_REST：表示支持SGW恢复功能。<br>- CNO_ULI：表示支持基于指定区域的策略控制功能。<br>- PENDINGTRANSACTION：表示支持事务等待功能。<br>- PCSCF_RESTORATION_ENHANCEMENT：PCSCF故障恢复增强功能。<br>- EXTENDED_BW_NR：扩展带宽特性。<br>默认值：无<br>配置原则：<br>- RELEASE8、RELEASE9和RELEASE10为必选参数，必须至少设置一个。<br>- ADC，NETLOC，PROVAFSIGNALFL，UMCH和SGW_REST为可选参数，可以根据实际应用场景配置0个或多个。<br>- 动态协商关闭时，UNC设置Feature列表默认值为RELEASE8和RELEASE9，并按照所设置的最高协议版本和PCRF进行交互。<br>- 动态协商使能时，如果不配置Feature列表，UNC按照缺省配置RELEASE8和RELEASE9和PCRF进行协商。<br>- 动态协商使能时，如果配置Feature列表，则UNC使用实际配置的Feature和PCRF进行协商。<br>- UNC会对协商结果进行缓存，按照实际的协商结果与PCRF进行该会话的后续交互，并使用缓存的协商结果发起后续会话与该PCRF的动态协商，以提高协商成功率。 |
| CARRYSUPFEASW | Supported-Feature AVP携带开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SUPFTNEGOSW”配置为“DISABLE”时为可选参数。<br>参数含义：该参数用于配置是否在CCR-I消息中携带Supported-Feature AVP。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN与Diameter Realm关联关系（REALMBINDAPN）](configobject/UNC/20.15.2/REALMBINDAPN.md)

## 使用实例

因为网络布局改变，之前指定的Diameter域已经不存在，新策略是根据IMSI来作为Diameter域，因此修改APN isp下的Gx应用根据IMSI构造归属地Diameter域名：

```
MOD REALMBINDAPN: APN="isp", APPLICATION=GX, CONSTBYIMSISW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN与Diameter-Realm关联关系（MOD-REALMBINDAPN）_09897286.md`
