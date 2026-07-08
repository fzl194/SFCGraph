---
id: UNC@20.15.2@MMLCommand@MOD VLR
type: MMLCommand
name: MOD VLR（修改VLR配置信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: VLR
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
- 电路域联合业务
- VLR管理
status: active
---

# MOD VLR（修改VLR配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于修改一个与本局 UNC 相连的VLR的VLR名称。

## 注意事项

- 该命令执行后立即生效。
- 可使用[**DSP VLR**](显示VLR迁移进度(DSP VLR)_26305256.md)查询VLR是否处于迁移状态，当MSC POOL中有VLR处于迁移状态时，不允许修改此MSC POOL中的VLR配置。
- 修改V值，会影响MSC POOL组网下各个MSC的用户接入比例。
- 若修改MSC POOL name，会使该VLR进入新的MSC POOL中。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VN | VLR号 | 可选必选说明：必选参数<br>参数说明：该参数用于指定VLR在移动网络中的设备号。<br>数据来源：整网规划<br>取值范围： 1～15位十进制数字<br>默认值：无 |
| VNM | VLR名称 | 可选必选说明：可选参数<br>参数说明：待修改的VLR名称。<br>数据来源：整网规划<br>取值范围：1~255位字符串<br>默认值：无 |
| SVSGS | Sv/SGs合一 | 可选必选说明：可选参数<br>参数说明：该参数用于设置SRVCC流程中选择的Sv接口的MSC/VLR与用户在CS域注册的MSC/VLR是否为同一个。其中用户在CS域注册的MSC/VLR是通过SGs接口与MME通信的。<br>数据来源：对端协商<br>取值范围：<br>- “INCONSISTENCY（不合一）”：表示SRVCC流程中使用RAI FQDN或LAI FQDN来解析MSC。<br>- “CONSISTENT_SELECTION（CSFB触发合一）”：表示SRVCC流程中使用“MSC主机名”来查找MSC，使选择的Sv接口的MSC与用户在CS域注册的MSC/VLR为同一个。<br>默认值：无<br>说明：当CSFB触发SRVCC，如果是MSC POOL场景，该参数需要设置为“CSFB触发合一”。CSFB触发SRVCC：UE在E-UTRAN网络下同时在PS域和CS域进行注册，并且也在IMS域进行注册。用户的语音业务优选IMS VoPS方式进行，LCS、USSD等业务仍然通过CS域进行。如果在通话过程中，用户需要回落到GERAN/UTRAN网络进行LCS、USSD等业务，语音通话会以SRVCC方式切换到MSC/VLR。SRVCC过程中Sv接口选择的MSC/VLR与用户在CS域注册的MSC/VLR需要保持一致，来保证回落到GERAN/UTRAN网络后，LCS、USSD等业务和语音通话都能正常进行。 |
| MSCHOSTNAME | MSC主机名 | 可选必选说明：条件必选参数<br>参数含义：该参数用于配置主机名。<br>数据来源：整网规划<br>取值范围：1~255位字符串<br>默认值：无<br>配置原则：该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成。<br>说明：当<br>“Sv/SGs合一”<br>取值为<br>“CONSISTENT_SELECTION（CSFB触发合一）”<br>时，该参数有效。<br>配置的MSC主机名需要与<br>[**ADD IPV4DNSH**](../../GTP-C接口管理/DNS/DNS Hostfile管理/增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)<br>或DNS Server中已配置的对应MSC主机名保持一致。 |
| POOLNM | MSC POOL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MSC POOL名称。<br>数据来源：整网规划<br>取值范围：1~19位字符串<br>默认值：无<br>说明：- POOLNM唯一标识一个MSC POOL。当此参数没有输入任何值的时候表示新增加的VLR不属于任何MSC POOL。<br>- 此参数大小写敏感，不支持含有中文字符，不支持包含非法字符，如逗号、分号、冒号、等号、加号、减号、单引号、双引号、百分号。<br>- POOLNM的值不能设置为NULL（这里字符N，U和L不区分大小写）。<br>- 如果需要将该VLR撤出POOL，使用空格键将POOLNM的值修改为NULL。 |
| MINV | 最小V值 | 可选必选说明：可选参数<br>参数说明：该参数用于指定最小的V值，与最大V值组合，形成V值区间。<br>UNC<br>系统采用一种算法从IMSI得到一个V值后，再根据本表配置的V值区间，选择一个VLR。从IMSI计算V值的算法参见协议3GPP TS 23.236。<br>数据来源：整网规划<br>取值范围：0~999<br>默认值：无<br>说明：在MSC POOL中，推荐把0~999的V值分配到所有的VLR上，在正常情况下，不使用<br>[**ADD LAIVLR**](../LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md)<br>命令配置缺省VLR。 |
| MAXV | 最大V值 | 可选必选说明：可选参数<br>参数说明：该参数用于指定最大的V值，与最小V值组合，形成V值区间。<br>UNC<br>系统采用一种算法从IMSI得到一个V值后，再根据本表配置的V值区间，选择一个VLR。从IMSI计算V值的算法参见协议3GPP TS 23.236。<br>数据来源：整网规划<br>取值范围：0~999<br>默认值：无<br>说明：在MSC POOL中，推荐把0~999的V值分配到所有的VLR上，在正常情况下，不使用<br>[**ADD LAIVLR**](../LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md)<br>命令配置缺省VLR。 |
| MOSR | SGs主叫通知功能 | 可选必选说明：可选参数<br>参数说明：该参数用于在CSFB流程中，控制MME在收到主叫Extended Service Request时是否向MSC发送SGsAP-SERVICE-REQUEST消息。<br>数据来源：整网规划<br>取值范围：<br>- “SUPPORT（支持）”：表示该主叫场景下，MME支持向MSC发送SGsAP-SERVICE-REQUEST消息。<br>- “NOT_SUPPORT（不支持）”：表示该主叫场景下，MME不支持向MSC发送SGsAP-SERVICE-REQUEST消息。<br>默认值：无<br>说明：该SGsAP-SERVICE-REQUEST消息中携带定制信元用于通知MSC已触发CSFB主叫流程，这样MSC可以统计此流程成功率。 |
| CSFBRESTORE | CSFB被叫恢复功能 | 可选必选说明：可选参数<br>参数含义：该参数用于控制MME故障场景下，MSC向新MME发送SGsAP-PAGING-REQUEST时，新MME是否寻呼用户。<br>数据来源：整网规划<br>取值范围：<br>- “SUPPORT（支持）”：表示该被叫场景下，新MME支持寻呼用户。<br>- “NOT_SUPPORT（不支持）”：表示该被叫场景下，新MME不支持寻呼用户，向MSC回复SGsAP-PAGING-REJECT消息。<br>默认值：“SUPPORT（支持）”<br>配置原则：当ADD TAILAI命令中一个LAI对应的TAI过多时，建议配置成NOT_SUPPORT（不支持）避免出现大范围寻呼用户，导致MME过载的场景。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VLR]] · VLR配置信息（VLR）

## 使用实例

修改VLR的名称，VLR号为86139027，VLR名称为test1：

```
MOD VLR: VN="86139027", VNM="test1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-VLR.md`
