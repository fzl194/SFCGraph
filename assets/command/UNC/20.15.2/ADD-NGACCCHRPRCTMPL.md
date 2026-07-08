---
id: UNC@20.15.2@MMLCommand@ADD NGACCCHRPRCTMPL
type: MMLCommand
name: ADD NGACCCHRPRCTMPL（增加NG接入CHR流程控制模板）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGACCCHRPRCTMPL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- CHR管理
- NG接入CHR流程控制模板
status: active
---

# ADD NGACCCHRPRCTMPL（增加NG接入CHR流程控制模板）

## 功能

**适用NF：AMF**

该命令用于增加NG接入CHR流程控制模板，用以控制CHR的采集流程。

## 注意事项

- 该命令执行后立即生效。

- 系统初始运行，会默认创建索引为0和1的NGACCCHRPRCTMPL配置，分别用于高性能CHR服务器和低性能CHR服务器的采集流控控制。这两条默认配置无法被删除，只能修改。

- 最多可输入128条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TMPLIDX | NGAPCHRFAILPRC |
| --- | --- |
| 0 | OTHER-1&INITREG-1&MOBILREG-1&DEREG-1&SYSCHANGE-1&SRVREQ-1&PAGING-1&ANREL-1&N2HO-1&XNHO-1&PDUSESSNEST-1&PDUSESSNMOD-1&PDUSESSNREL-1&UECONUPD-1&LOCATIONREPORT-1&RESERVED2-1&RESERVED3-1&RESERVED4-1&RESERVED5-1&RESERVED6-1 |
| 1 | OTHER-1&INITREG-1&MOBILREG-1&DEREG-1&SYSCHANGE-1&SRVREQ-1&PAGING-1&ANREL-1&N2HO-1&XNHO-1&PDUSESSNEST-1&PDUSESSNMOD-1&PDUSESSNREL-1&UECONUPD-1&LOCATIONREPORT-1&RESERVED2-1&RESERVED3-1&RESERVED4-1&RESERVED5-1&RESERVED6-1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMPLIDX | 流程控制模板索引 | 可选必选说明：必选参数<br>参数含义：流程控制模板索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>该参数值非0和1，需要使用SET NGACCCHRCFG命令设置NG接入CHR上报策略。 |
| NGAPCHRSUCCPRC | NG接入CHR成功流程上报选项 | 可选必选说明：可选参数<br>参数含义：NG接入CHR成功流程上报选项。<br>数据来源：本端规划<br>取值范围：<br>- “OTHER（OTHER(Other Procedure)）”：表示其他流程需要上报CHR单据。<br>- “INITREG（Initial Registration）”：表示初始注册流程需要上报CHR单据。<br>- “MOBILREG（Mobility Registration）”：表示移动性注册流程需要上报CHR单据。<br>- “DEREG（Deregistration）”：表示去注册流程需要上报CHR单据。<br>- “SYSCHANGE（Inter System Change）”：表示4、5G互操作流程需要上报CHR单据。<br>- “SRVREQ（Service Request）”：表示Service Request流程需要上报CHR单据。<br>- “PAGING（Paging）”：表示寻呼流程需要上报CHR单据。<br>- “ANREL（AN Release）”：表示AN Release流程需要上报CHR单据。<br>- “N2HO（N2 Handover）”：表示N2 Handover流程需要上报CHR单据。<br>- “XNHO（Xn Handover）”：表示Xn Handover流程需要上报CHR单据。<br>- “PDUSESSNEST（Pdu Session Establishment）”：表示Pdu Session Establishment流程需要上报CHR单据。<br>- “PDUSESSNMOD（Pdu Session Modification）”：表示Pdu Session Modification流程需要上报CHR单据。<br>- “PDUSESSNREL（Pdu Session Release）”：表示Pdu Session Release流程需要上报CHR单据。<br>- “UECONUPD（Ue Configuration Update）”：表示Ue Configuration Update流程需要上报CHR单据。<br>- “LOCATIONREPORT（Location Report）”：表示Location Report流程需要上报CHR单据。<br>- “RESERVED2（RESERVED2）”：RESERVED2<br>- “RESERVED3（RESERVED3）”：RESERVED3<br>- “RESERVED4（RESERVED4）”：RESERVED4<br>- “RESERVED5（RESERVED5）”：RESERVED5<br>- “RESERVED6（RESERVED6）”：RESERVED6<br>默认值：无<br>配置原则：无 |
| NGAPCHRFAILPRC | NG接入CHR失败流程上报选项 | 可选必选说明：可选参数<br>参数含义：NG接入CHR失败流程上报选项。<br>数据来源：本端规划<br>取值范围：<br>- “OTHER（OTHER(Other Procedure)）”：表示其他流程需要上报CHR单据。<br>- “INITREG（Initial Registration）”：表示初始注册流程需要上报CHR单据。<br>- “MOBILREG（Mobility Registration）”：表示移动性注册流程需要上报CHR单据。<br>- “DEREG（Deregistration）”：表示去注册流程需要上报CHR单据。<br>- “SYSCHANGE（Inter System Change）”：表示4、5G互操作流程需要上报CHR单据。<br>- “SRVREQ（Service Request）”：表示Service Request流程需要上报CHR单据。<br>- “PAGING（Paging）”：表示寻呼流程需要上报CHR单据。<br>- “ANREL（AN Release）”：表示AN Release流程需要上报CHR单据。<br>- “N2HO（N2 Handover）”：表示N2 Handover流程需要上报CHR单据。<br>- “XNHO（Xn Handover）”：表示Xn Handover流程需要上报CHR单据。<br>- “PDUSESSNEST（Pdu Session Establishment）”：表示Pdu Session Establishment流程需要上报CHR单据。<br>- “PDUSESSNMOD（Pdu Session Modification）”：表示Pdu Session Modification流程需要上报CHR单据。<br>- “PDUSESSNREL（Pdu Session Release）”：表示Pdu Session Release流程需要上报CHR单据。<br>- “UECONUPD（Ue Configuration Update）”：表示Ue Configuration Update流程需要上报CHR单据。<br>- “LOCATIONREPORT（Location Report）”：表示Location Report流程需要上报CHR单据。<br>- “RESERVED2（RESERVED2）”：RESERVED2<br>- “RESERVED3（RESERVED3）”：RESERVED3<br>- “RESERVED4（RESERVED4）”：RESERVED4<br>- “RESERVED5（RESERVED5）”：RESERVED5<br>- “RESERVED6（RESERVED6）”：RESERVED6<br>默认值：OTHER-1&INITREG-1&MOBILREG-1&DEREG-1&SYSCHANGE-1&SRVREQ-1&PAGING-1&ANREL-1&N2HO-1&XNHO-1&PDUSESSNEST-1&PDUSESSNMOD-1&PDUSESSNREL-1&UECONUPD-1&LOCATIONREPORT-1&RESERVED2-1&RESERVED3-1&RESERVED4-1&RESERVED5-1&RESERVED6-1<br>配置原则：无 |
| NGAPKEYSUCCSIG | NG接入成功信令事件上报选项 | 可选必选说明：可选参数<br>参数含义：NG接入成功信令事件上报选项。<br>数据来源：本端规划<br>取值范围：<br>- “CRTSMCTX（Nsmf_PDUSession_CreateSMContext）”：表示Nsmf_PDUSession_CreateSMContext信令事件需要上报CHR。<br>- “UPDSMCTX（Nsmf_PDUSession_UpdateSMContext）”：表示Nsmf_PDUSession_UpdateSMContext信令事件需要上报CHR。<br>- “RELSMCTX（Nsmf_PDUSession_ReleaseSMContext）”：表示Nsmf_PDUSession_ReleaseSMContext信令事件需要上报CHR。<br>- “DEREGNOTF（Nudm_UECM_Deregistration Notification）”：表示Nudm_UECM_Deregistration Notification信令事件需要上报CHR。<br>- “UNSUB（Nudm_SDM_Unsubscribe）”：表示Nudm_SDM_Unsubscribe信令事件需要上报CHR。<br>- “RESERVED1（RESERVED1）”：RESERVED1<br>- “RESERVED2（RESERVED2）”：RESERVED2<br>- “RESERVED3（RESERVED3）”：RESERVED3<br>- “RESERVED4（RESERVED4）”：RESERVED4<br>- “RESERVED5（RESERVED5）”：RESERVED5<br>- “RESERVED6（RESERVED6）”：RESERVED6<br>默认值：无<br>配置原则：无 |
| NGAPKEYFAILSIG | NG接入失败信令事件上报选项 | 可选必选说明：可选参数<br>参数含义：NG接入失败信令事件上报选项。<br>数据来源：本端规划<br>取值范围：<br>- “CRTSMCTX（Nsmf_PDUSession_CreateSMContext）”：表示Nsmf_PDUSession_CreateSMContext信令事件需要上报CHR。<br>- “UPDSMCTX（Nsmf_PDUSession_UpdateSMContext）”：表示Nsmf_PDUSession_UpdateSMContext信令事件需要上报CHR。<br>- “RELSMCTX（Nsmf_PDUSession_ReleaseSMContext）”：表示Nsmf_PDUSession_ReleaseSMContext信令事件需要上报CHR。<br>- “DEREGNOTF（Nudm_UECM_Deregistration Notification）”：表示Nudm_UECM_Deregistration Notification信令事件需要上报CHR。<br>- “UNSUB（Nudm_SDM_Unsubscribe）”：表示Nudm_SDM_Unsubscribe信令事件需要上报CHR。<br>- “RESERVED1（RESERVED1）”：RESERVED1<br>- “RESERVED2（RESERVED2）”：RESERVED2<br>- “RESERVED3（RESERVED3）”：RESERVED3<br>- “RESERVED4（RESERVED4）”：RESERVED4<br>- “RESERVED5（RESERVED5）”：RESERVED5<br>- “RESERVED6（RESERVED6）”：RESERVED6<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGACCCHRPRCTMPL]] · NG接入CHR流程控制模板（NGACCCHRPRCTMPL）

## 使用实例

新增索引为10的流程控制模板，指定只上报失败业务流程的CHR：

```
ADD NGACCCHRPRCTMPL: TMPLIDX=10, NGAPCHRFAILPRC=OTHER-1&INITREG-1&MOBILREG-1&DEREG-1&SYSCHANGE-1&SRVREQ-1&PAGING-1&ANREL-1&N2HO-1&XNHO-1&PDUSESSNEST-1&PDUSESSNMOD-1&PDUSESSNREL-1&UECONUPD-1&LOCATIONREPORT-1&RESERVED2-1&RESERVED3-1&RESERVED4-1&RESERVED5-1&RESERVED6-1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NGACCCHRPRCTMPL.md`
