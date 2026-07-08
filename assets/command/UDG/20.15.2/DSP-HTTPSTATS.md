---
id: UDG@20.15.2@MMLCommand@DSP HTTPSTATS
type: MMLCommand
name: DSP HTTPSTATS（显示HTTP统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: HTTPSTATS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP统计管理
status: active
---

# DSP HTTPSTATS（显示HTTP统计信息）

## 功能

该命令用于显示HTTP相关的统计信息。HTTP相关模块包括了SBILINK、HTTPLINK。

> **说明**
> - 该命令中起始索引和终止索引用于命令后续扩展，使用需要注意起始索引必须小于等于终止索引，当起始索引等于终止索引时，即指定单个索引的统计结果输出。
> - 该命令中附加过滤条件为预留参数，便于后续输出过滤条件扩展使用。
> - 查询模块类型为HTTPLINK、子模块类型为HTTP并添加过滤条件时，MML的回显计数为0，将统计结果写入运行日志中。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MT | 模块类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的HTTP统计信息的模块。<br>数据来源：本端规划<br>取值范围：<br>- “HTTPLINK（HTTPLINK）”：服务化接口报文转发处理<br>- “SBILINK（SBILINK）”：服务化接口链路管理控制<br>默认值：无<br>配置原则：无 |
| HTTPSUBMT | HTTPLINK子模块 | 可选必选说明：该参数在"MT"配置为"HTTPLINK"时为条件必选参数。<br>参数含义：该参数用于指定查询的统计信息的子模块。HTTP为HTTP协议栈模块，ADP为HTTP协议栈的适配处理模块。<br>数据来源：本端规划<br>取值范围：<br>- “ADP（ADP）”：适配模块<br>- “HTTP（HTTP）”：HTTP模块<br>- “OAUTH（OAUTH）”：OAUTH模块<br>默认值：无<br>配置原则：无 |
| SBISUBMT | SBILINK子模块 | 可选必选说明：该参数在"MT"配置为"SBILINK"时为条件必选参数。<br>参数含义：该参数用于指定查询的统计信息的子模块。LINK为链路模块，RES为资源模块。<br>数据来源：本端规划<br>取值范围：<br>- “RES（资源）”：资源信息查询<br>- “LINK（链路）”：SBI链路查询<br>默认值：无<br>配置原则：无 |
| HTTPMD | HTTP模式 | 可选必选说明：该参数在"MT"配置为"HTTPLINK"时为条件必选参数。<br>参数含义：该参数用于指定查询的HTTP模式，HTTP模式指客户端模式或服务端模式的区分。<br>数据来源：本端规划<br>取值范围：<br>- “Client（客户端）”：客户端模式<br>- “Server（服务端）”：服务端模式<br>- “Both（Both）”：既可以作为客户端也可以作为服务端<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"HTTPSUBMT"配置为"ADP"时为条件可选参数。<br>参数含义：该参数用于指定附加的网元类型过滤条件。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF<br>- “NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF<br>- “NFTypeDRA（NFTypeDRA）”：NF类型为DRA<br>- “NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| STARIDX | 起始索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的起始索引，该索引为预留参数，便于后续命令扩展使用。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| ENDIDX | 终止索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的终止索引，该参数为预留参数，便于后续命令扩展使用。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| APP1 | 附加过滤条件1 | 可选必选说明：可选参数<br>参数含义：该参数用于指定附加的过滤条件，用于显示发送给特定Topic的统计信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| APP2 | 附加过滤条件2 | 可选必选说明：可选参数<br>参数含义：该参数用于指定附加的过滤条件2，便于后续命令扩展使用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| APP3 | 附加过滤条件3 | 可选必选说明：可选参数<br>参数含义：该参数用于指定附加的过滤条件3，便于后续命令扩展使用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| APP4 | 附加过滤条件4 | 可选必选说明：可选参数<br>参数含义：该参数用于指定附加的过滤条件4，便于后续命令扩展使用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPSTATS]] · HTTP统计信息（HTTPSTATS）

## 使用实例

- 若运营商想要查询HTTP的相关统计信息，并显示服务化接口报文转发处理的Client端消息统计，模块类型为HTTPLINK，子模块类型ADP，HTTP模式为Client端，可使用如下命令：
  ```
  %%DSP HTTPSTATS: MT=HTTPLINK, HTTPSUBMT=ADP, HTTPMD=Client;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  统计项                           统计值  

  客户端接收请求消息次数:           3699566  
  客户端成功处理请求消息次数:       3699534  
  客户端接收相应消息次数：          3702162    
  客户端成功处理消息次数:           3699566          
  (结果个数 = 4)

  ---    END
  ```
- 若运营商想要查询HTTP的相关统计信息，并显示服务化接口报文转发处理的特定Topic的消息统计，模块类型为HTTPLINK，子模块类型ADP，HTTP模式为Both，APP1过滤条件为397329，可使用如下命令：
  ```
  %%DSP HTTPSTATS: MT=HTTPLINK, HTTPSUBMT=ADP, HTTPMD=Both, APP1="3699566";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  统计项                                  统计值 

  服务端成功处理3699566的请求消息次数 :   2419193   
  客户端成功处理3699566的请求消息次数 :   3699566     
  (结果个数 = 2)

  ---    END
  ```
- 若运营商想要查询HTTP的相关统计信息，并显示服务化接口报文转发处理的特定NF的消息统计，模块类型为HTTPLINK，子模块类型ADP，HTTP模式为Both，NF类型为Nnrf，可使用如下命令：
  ```
  %%DSP HTTPSTATS: MT=HTTPLINK, HTTPSUBMT=ADP, HTTPMD=Both, NFTYPE=NFTypeNRF;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  统计项                             统计值 

  客户端成功接收请求消息次数 :            2    
  客户端成功发送请求消息次数 :            2  
  客户端接收响应消息次数 :                10
  ...
  (结果个数 = 14)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示HTTP统计信息（DSP-HTTPSTATS）_83972184.md`
