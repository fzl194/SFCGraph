# 增加SBI接口链路属性配置（ADD SBILINKCFG）

- [命令功能](#ZH-CN_MMLREF_0000001183813628__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001183813628__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001183813628__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001183813628__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001183813628)

该命令用于增加服务化接口的静态链路及其属性，静态链路可以配置网元级和IP级链路。该命令也可以用于增加动态链路的属性。

## [注意事项](#ZH-CN_MMLREF_0000001183813628)

- 该命令执行后立即生效。

- 配置Callback、Location及其他URL消息的链路属性时，参数“NFINSTID”必须配置成对端的IP地址或FQDN（详细参见该参数的描述），参数“NETINFO”配置成“NULL”，参数“NFTYPE”建议配置成“INVALID”（如果需要配置成其他值，请联系华为工程师）。
- 本端设备NF类型为AMF/SMF，对端设备NF类型为UDM/AUSF/PCF/NRF时，同时未打开链路自动控制功能时，未添加本命令配置时系统默认按整系统控制链路数量。其他场景下，未打开链路自动控制功能且未添加本命令配置时系统默认按单进程控制链路数量；如果打开链路自动控制功能，且未添加本命令配置时系统按链路自动控制规则控制链路数量；如果配置了本命令时，按本命令配置规则控制链路数量。
- 整系统控制默认链路数4条，单进程控制默认链路数1条，upf单进程控制默认链路数8条。

- 最多可输入512条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001183813628)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001183813628)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务化接口链路的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~513。<br>默认值：无<br>配置原则：无 |
| LINKTYPE | 链路类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务化接口链路的类型，分为静态链路和动态链路两种。<br>数据来源：本端规划<br>取值范围：<br>- “Dynamic（Dynamic）”：动态学习<br>- “Static（Static）”：静态配置<br>默认值：无<br>配置原则：无 |
| SBIAPLEIDX | 服务化接口本端实体索引 | 可选必选说明：该参数在"LINKTYPE"配置为"Static"时为条件必选参数。该参数在"LINKTYPE"配置为"Dynamic"时为条件可选参数。<br>参数含义：该参数用于指定关联的服务化接口本端实体索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD SBIAPLE**](../服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)<br>命令配置生成。 |
| NFTYPE | 对端NF类型 | 可选必选说明：该参数在"LINKTYPE"配置为"Dynamic"时为条件可选参数。<br>参数含义：该参数用于指定对端NF的类型。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeMBSMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| NETINFO | 网络信息 | 可选必选说明：该参数在"LINKTYPE"配置为"Dynamic"时为条件可选参数。<br>参数含义：该参数用于指定本端NF和对端NF的网络位置信息，即网元间互联网络为本地网络还是外部网络。<br>数据来源：本端规划<br>取值范围：<br>- “NULL（NULL）”：对网络连接不做区分<br>- “Internal（内部网络）”：本地网络，如中国区本省范围内可认为本地网络。<br>- “External（外部网络）”：外部网络，如中国区跨省范围可认为是外部网络。<br>默认值：NULL<br>配置原则：无 |
| NFINSTID | 对端NF实例ID | 可选必选说明：该参数在"LINKTYPE"配置为"Static"时为条件必选参数。该参数在"NETINFO"配置为"NULL"时为条件可选参数。<br>参数含义：该参数用于指定对端NF的实例ID。当链路集类型为Callback或Location时，该参数可以填写为对端的IP地址或FQDN，即只匹配IP地址或者FQDN，也可以填写为对端IP地址或FQDN与端口号的组合，即IP地址或FQDN与端口号都匹配。而且，如果是IPv6地址，则IPv6地址必须放在中括号内。比如：10.1.1.1或10.1.1.1:80或[fc00:22::33]或[fc00:22::33]:80或example.com或example.com:80。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| NFSRVNAME | 对端NF服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF服务的名称。该参数可以通过<br>[**DSP SBILINKSTATUS**](../服务化接口链路管理/查询服务化接口链路状态（DSP SBILINKSTATUS）_29213281.md)<br>中PEERNFSRVNAME字段获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| NFSRVINSTID | 对端NF服务实例ID | 可选必选说明：该参数在"NETINFO"配置为"NULL"时为条件可选参数。<br>参数含义：该参数用于指定配置的对端NF服务实例ID。该参数不可独立配置，需要与NFINSTID共同配置方能生效。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| SCHEMA | 模式 | 可选必选说明：该参数在"LINKTYPE"配置为"Static"时为条件必选参数。该参数在"LINKTYPE"配置为"Dynamic"时为条件可选参数。<br>参数含义：该参数用于指定模式，分为HTTP和HTTPS两种。如果不输入该参数，则针对HTTP及HTTPS都生效。<br>数据来源：本端规划<br>取值范围：<br>- “HTTP（HTTP）”：明文传输HTTP协议传输的数据<br>- “HTTPS（HTTPS）”：密文传输HTTP协议传输的数据<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"LINKTYPE"配置为"Static"时为条件必选参数。<br>参数含义：该参数用于指定IP类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPTypeV4（IPv4地址）”：IPv4地址<br>- “IPTypeV6（IPv6地址）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| HTTPLEIDX | HTTP本端实体索引 | 可选必选说明：该参数在"LINKTYPE"配置为"Static"时为条件必选参数。<br>参数含义：该参数用于指定HTTP本端实体的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD HTTPLE**](../../HTTP管理/HTTP本端实体管理/增加HTTP本端实体（ADD HTTPLE）_84132094.md)<br>命令配置生成。 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERPORT | 对端端口 | 可选必选说明：该参数在"LINKTYPE"配置为"Static"时为条件必选参数。<br>参数含义：该参数用于指定对端端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |
| PROPIDX | SBI链路集策略索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SBI链路集策略的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD SBILINKSETPROP**](../服务化接口链路集策略管理/增加SBI链路集策略（ADD SBILINKSETPROP）_29053325.md)<br>命令配置生成。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于配置服务化接口链路的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001183813628)

若运营商想配置一条动态链路的属性，其索引为1、SBIAPLE索引为1、NF类型为NFTypeNRF、NFID为bf33a517-7789-4637-b675-b3591b0d706b、服务名称为nnssf-nsselection、NF服务实例ID为1，并指定SBI链路集策略索引为1，描述信息配置为"sbilink"，可以执行如下命令：

```
ADD SBILINKCFG:INDEX=1,LINKTYPE=Dynamic,SBIAPLEIDX=1,NFTYPE=NFTypeNRF,NETINFO=NULL,NFINSTID="bf33a517-7789-4637-b675-b3591b0d706b",NFSRVNAME="Nnssf_NSSelection",NFSRVINSTID="1",PROPIDX=1,DESC="sbilink";
```
