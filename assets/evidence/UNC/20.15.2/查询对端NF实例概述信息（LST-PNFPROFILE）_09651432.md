# 查询对端NF实例概述信息（LST PNFPROFILE）

- [命令功能](#ZH-CN_MMLREF_0209651432__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651432__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651432__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651432__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209651432__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209651432)

**适用NF：AMF、SMF、NSSF、SMSF、NCG、NRF、SGW-C、PGW-C、GGSN**

该命令用于查询本地配置的对端NF实例的概述信息。

## [注意事项](#ZH-CN_MMLREF_0209651432)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209651432)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651432)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。NFINSTANCEID参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.不区分大小写。不支持配置单空格。<br>默认值：无<br>配置原则：<br>建议以UUID格式配置。如果不为UUID格式，该参数被发送到对端网元且被使用时，可能出现异常。 |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| NFSTATUS | NF状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF状态。<br>数据来源：全网规划<br>取值范围：<br>- “Invalid（Invalid）”：表示当前NF实例处于无效态，如果配置成该值，NF选择时不会选择此类NF。<br>- “Registered（Registered）”：表示当前NF实例处于注册态，如果配置成该值，NF选择时只会选择此类NF。<br>- “Suspend（Suspend）”：表示当前NF实例处于挂起态。当NF实例处于运维状态下，比如正在进行用户迁移等，不希望在NF发现流程中被选中时，可以置为此状态，迁移完毕后通过该命令对应的MOD命令修改为注册态即可。<br>- “DeRegistered（DeRegistered）”：表示当前NF实例处于去注册态，如果配置成该值，NF选择时不会选择此类NF。<br>- “UnDiscoverable（UnDiscoverable）”：表示当前NF实例处于不可被发现状态，如果配置成该值，NF选择时不会选择此类NF。<br>默认值：无<br>配置原则：<br>建议配置成Registered，如果配置成其它状态NF服务发现时不会被选中。 |

## [使用实例](#ZH-CN_MMLREF_0209651432)

查询对端SMF实例的概述信息，NF实例标识为SMF_Instance_0，NF类型为NfSMF。

```
%%LST PNFPROFILE: ;%%
RETCODE = 0  操作成功

结果如下
---------
NF实例标识  =  smf_instance_0
    NF类型  =  NfSMF
    NF状态  =  Registered
      域名  =  NULL
PLMN间域名  =  NULL
IP地址类型  =  IPTypeV4
 IPv4地址1  =  10.240.240.240
 IPv4地址2  =  10.240.240.240
 IPv4地址3  =  10.240.240.240
 IPv4地址4  =  10.240.240.240
 IPv6地址1  =  ::
 IPv6地址2  =  ::
 IPv6地址3  =  ::
 IPv6地址4  =  ::
    端口号  =  8080
      容量  =  100
    优先级  =  0
      负载  =  0
  位置信息  =  NULL
 NF描述名称 =  NULL
  协议模式  =  NULL
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209651432)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF实例标识 | 该参数用于指定NF实例标识。 |
| NF类型 | 该参数用于指定NF类型。 |
| NF状态 | 该参数用于指定NF状态。 |
| 域名 | 该参数用于指定NF的域名。本参数指定的域名中可以不包含PLMN信息，主要用于本网内的域名查询场景。 |
| PLMN间域名 | 该参数用于指定PLMN间域名。当NF涉及跨PLMN网络间的NF发现时，需要为NF配置“PLMN间域名”。 |
| IP地址类型 | 该参数用于指定NF的IP地址类型。 |
| IPV4地址1 | 该参数用于指定NF的IPV4类型地址1。 |
| IPV4地址2 | 该参数用于指定NF的IPV4类型地址2。 |
| IPV4地址3 | 该参数用于指定NF的IPV4类型地址3。 |
| IPV4地址4 | 该参数用于指定NF的IPV4类型地址4。 |
| IPV6地址1 | 该参数用于指定NF的IPV6类型地址1。 |
| IPV6地址2 | 该参数用于指定NF的IPV6类型地址2。 |
| IPV6地址3 | 该参数用于指定NF的IPV6类型地址3。 |
| IPV6地址4 | 该参数用于指定NF的IPV6类型地址4。 |
| 端口号 | 该参数用于指定NF的端口号。 |
| 容量 | 本参数用于指定NF的相对权重（与其他同类型NF实例相比）。特别地，如果NF容量的绝对值不超过本参数的取值范围，那么本参数可以直接取用容量绝对值。例如AMF可接入的用户数是50000，那么该AMF的容量就可以用50000表示。 |
| 优先级 | 本参数用于指定NF的优先级（与其他同类型NF实例相比）。在NF选择过程中，NF会选择高优先级的NF，如果两个或多个NF的优先级一样，NF则会根据“容量”做进一步的判断。 |
| 负载 | 本参数用于指定NF的负载。系统可能会将此参数作为NF选择的依据。 |
| 位置信息 | 本参数用于指定NF的位置描述信息，比如NF所在的地域信息描述等。 |
| NF描述名称 | 该参数用于表示NF实例的描述信息。 |
| 协议模式 | 该参数用于指定协议模式。NFTYPE选择为SCP与SEPP时需要指定该参数。 |
