---
id: UNC@20.15.2@MMLCommand@CLR NFCACHE
type: MMLCommand
name: CLR NFCACHE（清除NF缓存）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NFCACHE
command_category: 动作类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF Cache管理
status: active
---

# CLR NFCACHE（清除NF缓存）

## 功能

![](清除NF缓存（CLR NFCACHE）_17555434.assets/notice_3.0-zh-cn_2.png)

本命令会清除本端从NRF中获得的远端NF信息缓存数据，可能会导致业务呼损。

**适用NF：AMF、SMF、NRF、NSSF、NCG、SMSF**

该命令用于清除本端从NRF中获得的远端NF信息缓存数据。如果缓存数据存在异常，或者希望在缓存老化时间到达之前清除缓存，可以执行该命令。

## 注意事项

- 该命令执行后立即生效。

- 清除缓存信息后，后续NF进行服务发现就需要发查询请求给NRF，可能会导致短时间内向NRF的服务发现请求增多。
- 该命令参数均为可选，若不提供任何输入参数，则会清除全部缓存，建议就实际情况选择输入参数。
- 当参数“仅缓存更新”开启时，不会直接删除缓存，而是按照一定的速率，向NRF主动服务发现来更新缓存。
- 如果在短时间内连续两次执行此命令且参数“仅缓存更新”都开启时，先执行的命令还没有将所有NF的缓存全部更新完成的场景下，后执行优先级更高的“CLR_CACHE_ALL”会打断前面“CLR_CACHE_NFTYPE”的命令。其它场景则会直接丢弃后执行的此命令。
- 如果“仅缓存更新”功能正在执行过程中，再次下发此命令且参数“仅缓存更新”关闭时，“仅缓存更新”功能会中止。
- 指定NF InstanceID清缓存时推荐对主备NF InstanceID同时执行清缓存，否则会导致无法按照配置的NF优先级选择目标NF。
- 如果“仅缓存更新”功能关闭，且软参DWORD205 BIT31开启，执行“CLR_CACHE_ALL”会清除所有订阅记录并触发去订阅流程。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLRCACHETYPE | 缓存清除策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定缓存清除的策略。<br>数据来源：本端规划<br>取值范围：<br>- “CLR_CACHE_ALL（CLR_CACHE_ALL）”：清除缓存中所有的NF信息。<br>- “CLR_CACHE_NFTYPE（CLR_CACHE_NFTYPE）”：根据NF类型清除缓存中的NF信息。<br>- “CLR_CACHE_NFID（CLR_CACHE_NFID）”：根据指定的NF实例标识清除缓存中的单个NF信息。<br>默认值：CLR_CACHE_ALL<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"CLRCACHETYPE"配置为"CLR_CACHE_NFTYPE"时为条件必选参数。<br>参数含义：该参数用于指定采用NF类型来清除缓存时，具体的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| NFID | NF实例标识 | 可选必选说明：该参数在"CLRCACHETYPE"配置为"CLR_CACHE_NFID"时为条件必选参数。<br>参数含义：该参数用于指定采用NF实例标识来清除缓存时，具体的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是36。<br>默认值：无<br>配置原则：<br>该参数为通过DSP NFCACHE命令指定对应的NF类型以及Cache Type为E_REMOTE_ONLY查询得到的NF实例标识。 |
| CACHEUPDATEONLY | 仅缓存更新 | 可选必选说明：该参数在"CLRCACHETYPE"配置为"CLR_CACHE_ALL"、"CLR_CACHE_NFTYPE"、"CLR_CACHE_NFID"时为条件可选参数。<br>参数含义：如果功能开启，不直接删除本地缓存，而是将缓存里指定的NF记录（记录的范围根据参数缓存清除策略来定），按照一定的速率，向NRF主动服务发现来更新缓存。如果功能关闭，支持删除本地缓存。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：ON<br>配置原则：无 |
| UPDATESPEED | 缓存更新速度(秒) | 可选必选说明：该参数在"CACHEUPDATEONLY"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于指定当次缓存更新的速度，即每隔N秒去NRF服务发现一个NF。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。当取值为0时，会按照默认值10秒每个的速率去NRF服务发现。<br>默认值：10<br>配置原则：无 |
| PODID | POD地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定POD的地址。如需按指定POD进行清除缓存，输入此参数即可。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。来源于DSP NFCACHE的输出报文的参数“Pod地址”或命令DSP POD的输出报文中的参数“Pod名称”。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFCACHE]] · NF缓存信息（NFCACHE）

## 使用实例

- 运营商A需要清除从NRF中获得的远端NF信息缓存数据：
  ```
  CLR NFCACHE:;
  ```
- 运营商A需要清除所有从NRF中获得的所有远端AMF信息缓存数据：
  ```
  CLR NFCACHE:CLRCACHETYPE=CLR_CACHE_NFTYPE,NFTYPE=NfAMF;
  ```
- 运营商A需要清除从NRF中获得的远端网元（NF实例标识为a6a61c6f-0d3a-4221-b1da-424eda3ccf67）信息缓存数据：
  ```
  CLR NFCACHE:CLRCACHETYPE=CLR_CACHE_NFID,NFID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67";
  ```
- 运营商A需要清除所有向NRF的订阅记录和从NRF中获得的远端网元缓存记录（需先通过LST COMMONSOFTPARAOFBIT确保软参DWORD205 BIT31开启）：
  ```
  CLR NFCACHE:CLRCACHETYPE=CLR_CACHE_ALL;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-NFCACHE.md`
