---
id: UNC@20.15.2@MMLCommand@LST PNFPROFILE
type: MMLCommand
name: LST PNFPROFILE（查询对端NF实例概述信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFPROFILE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- NRF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例概述信息管理
status: active
---

# LST PNFPROFILE（查询对端NF实例概述信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、NRF、SGW-C、PGW-C、GGSN**

该命令用于查询本地配置的对端NF实例的概述信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。NFINSTANCEID参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.不区分大小写。不支持配置单空格。<br>默认值：无<br>配置原则：<br>建议以UUID格式配置。如果不为UUID格式，该参数被发送到对端网元且被使用时，可能出现异常。 |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| NFSTATUS | NF状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF状态。<br>数据来源：全网规划<br>取值范围：<br>- “Invalid（Invalid）”：表示当前NF实例处于无效态，如果配置成该值，NF选择时不会选择此类NF。<br>- “Registered（Registered）”：表示当前NF实例处于注册态，如果配置成该值，NF选择时只会选择此类NF。<br>- “Suspend（Suspend）”：表示当前NF实例处于挂起态。当NF实例处于运维状态下，比如正在进行用户迁移等，不希望在NF发现流程中被选中时，可以置为此状态，迁移完毕后通过该命令对应的MOD命令修改为注册态即可。<br>- “DeRegistered（DeRegistered）”：表示当前NF实例处于去注册态，如果配置成该值，NF选择时不会选择此类NF。<br>- “UnDiscoverable（UnDiscoverable）”：表示当前NF实例处于不可被发现状态，如果配置成该值，NF选择时不会选择此类NF。<br>默认值：无<br>配置原则：<br>建议配置成Registered，如果配置成其它状态NF服务发现时不会被选中。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFPROFILE]] · 对端NF实例概述信息（PNFPROFILE）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFPROFILE.md`
