---
id: UNC@20.15.2@MMLCommand@DSP GRPPFCPSESSINFO
type: MMLCommand
name: DSP GRPPFCPSESSINFO（显示PFCP的组会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GRPPFCPSESSINFO
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 查询5G LAN组PFCP会话信息
status: active
---

# DSP GRPPFCPSESSINFO（显示PFCP的组会话信息）

## 功能

**适用NF：SMF**

该命令用于显示PFCP的组会话信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSPINFOTYPE | 信息呈现方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信息呈现方式，“简约信息呈现”显示指定5G Lan组里的会话标识，“详细信息呈现”显示全部或指定规则、隧道、会话等相关信息。<br>数据来源：本端规划<br>取值范围：<br>- SIMPLE（简约信息呈现）<br>- DETAILED（详细信息呈现）<br>默认值：无<br>配置原则：无 |
| QUERYTYPE | 查询方式 | 可选必选说明：该参数在"DSPINFOTYPE"配置为"SIMPLE"时为条件必选参数。<br>参数含义：该参数用于指定查询方式，通常以指定5G Lan组ID的方式查询会话标识。<br>数据来源：本端规划<br>取值范围：<br>- NGLANGROUPID（5G LAN组ID）<br>默认值：无<br>配置原则：无 |
| NGLANGROUPID | 5G LAN组的ID | 可选必选说明：该参数在"QUERYTYPE"配置为"NGLANGROUPID"时为条件必选参数。<br>参数含义：该参数用于指定5G LAN组的ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是18~37。<br>默认值：无<br>配置原则：<br>NGLANGROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |
| DETAILTYPE | 详单类型 | 可选必选说明：该参数在"DSPINFOTYPE"配置为"DETAILED"时为条件必选参数。<br>参数含义：该参数用于指定显示的详单类型，通常查询全部或指定的PFCP会话的相关信息，也可查询全部或指定的规则、隧道相关信息。<br>数据来源：本端规划<br>取值范围：<br>- PDR（包探测规则）<br>- FAR（包转发规则）<br>- VNGMURR（VNGM创建的使用上报规则）<br>- TUNNEL（传输业务流量的通道）<br>- PFCPSESSION（PFCP会话）<br>默认值：无<br>配置原则：无 |
| CPSEID | C面的会话端点标识 | 可选必选说明：该参数在"DSPINFOTYPE"配置为"DETAILED"时为条件必选参数。<br>参数含义：该参数用于指定C面分配的单一会话标识，可通过SIMPLE方式查询指定5G Lan组ID获得。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~9223372036854775807。<br>默认值：无<br>配置原则：无 |
| PDRID | PDR标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"时为条件可选参数。<br>参数含义：该参数用于指定某一个PDR规则，可通过DETAILED方式查询PDR详单类型获得。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| FARID | FAR标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"FAR"时为条件可选参数。<br>参数含义：该参数用于指定某一个FAR规则，可通过DETAILED方式查询FAR详单类型获得。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| URRID | URR标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"VNGMURR"时为条件可选参数。<br>参数含义：该参数用于指定某一个URR规则，可通过DETAILED方式查询VNGMURR详单类型获得。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GRPPFCPSESSINFO]] · PFCP的组会话信息（GRPPFCPSESSINFO）

## 使用实例

- 查询指定GroupID的组会话上的PFCP会话信息，执行具体如下：
  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=SIMPLE, QUERYTYPE=NGLANGROUPID, NGLANGROUPID="a0000001-460-03-01";%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
         5G LAN组ID  =  a0000001-460-03-01
       UP的实例标识  =  upf_instance_1
  C面的会话端点标识  =  140752789241857
   对端网元的IP地址  =  192.168.0.1
  (结果个数 = 1)

  ---    END
  ```
- 查询指定CPSEID的PFCP会话信息，执行具体如下：
  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=PFCPSESSION, CPSEID=140752789241857;%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
  	   5G LAN组ID  =  a0000001-460-03-01
  	 UP的实例标识  =  upf_instance_1
      C面的会话端点标识  =  140752789241857
      U面的会话端点标识  =  2
                PDR列表  =  4097 8194 16387
                FAR列表  =  1075838977 1074790402 1077936131
                URR列表  =  NULL
                POD名称  =  uncpod-0
       对端网元的IP地址  =  192.168.0.1
  (结果个数 = 1)

  ---    END
  ```
- 查询指定CPSEID的PFCP会话的隧道信息（当前仅有N19的隧道信息），执行具体如下：
  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=TUNNEL, CPSEID=140752789241857;%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
             隧道类型  =  TunnelTypeN19
             隧道TEID  =  10
             IPv4地址  =  10.0.0.1
             IPv6地址  =  ::
  (结果个数 = 1)

  ---    END
  ```
- 查询指定CPSEID的PFCP会话的PDR信息（可指定PDR ID），执行具体如下：
  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=PDR, CPSEID=140752789241857;%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
  PDR标识    PDR类型        PDR优先级      PDR方向		    关联的URR列表   关联的FAR标识    本端接口类型  

  4097       PdrTypeN6Dl    4294967295     Unidirectional Downlink    1075838977      NULL             UpItfTypeN6           
  8194       PdrTypeN6Ul    4294967295     Unidirectional Uplink      1074790402      NULL             UpItfTypeInvalid      
  16387      PdrTypeN19Dl   4294967295     Unidirectional Downlink    1077936131      NULL             UpItfTypeN19          
  (结果个数 = 3)

  ---    END
  ```
- 查询指定CPSEID的PFCP会话的FAR信息（可指定FAR ID），执行具体如下：
  ```
  %%DSP GRPPFCPSESSINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=FAR, CPSEID=140752789241857;%%
  RETCODE = 0  操作成功

  NgLanGroup PfcpSession Info
  ---------------------------
  FAR标识        FAR类型         对端接口类型         FAR应用动作  

  1075838977     FarTypeN6Dl     UpItfTypeInvalid     Forw              
  1074790402     FarTypeN6Ul     UpItfTypeN6          Forw              
  1077936131     FarTypeN19Dl    UpItfTypeInvalid     Forw              
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GRPPFCPSESSINFO.md`
