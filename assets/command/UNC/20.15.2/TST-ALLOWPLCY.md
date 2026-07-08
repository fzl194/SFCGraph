---
id: UNC@20.15.2@MMLCommand@TST ALLOWPLCY
type: MMLCommand
name: TST ALLOWPLCY（测试允许访问策略配置）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: ALLOWPLCY
command_category: 调测类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 访问授权控制
- 访问授权策略管理
status: active
---

# TST ALLOWPLCY（测试允许访问策略配置）

## 功能

**适用NF：NRF**

该命令用于测试配置的访问授权控制策略。

## 注意事项

- 输入参数中源NF类型，源NF实例标识，源FQDN至少输入一个。
- 输入参数中目标NF类型，目标NF实例标识，目标FQDN至少输入一个。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCNFTYPE | 源NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示访问的源NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| SRCNFINSTID | 源NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示访问的源NF实例标识，该参数通过DSP REGNFINSTANCE命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| SRCFQDN | 源FQDN | 可选必选说明：可选参数<br>参数含义：该参数用于表示访问的源FQDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| SRCMCC | 源移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示访问的源NF对象所允许访问的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| SRCMNC | 源移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示访问的源NF对象所允许访问的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位3位十进制数。<br>默认值：无<br>配置原则：无 |
| TARGETNFTYPE | 目标NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示访问的目标NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |
| TARGETINSTID | 目标NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示访问的目标NF实例标识，该参数通过DSP REGNFINSTANCE命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：无 |
| TARGETFQDN | 目标FQDN | 可选必选说明：可选参数<br>参数含义：该参数用于表示访问的目标FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| DETAILSW | 调试日志开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示详细内容打印开关，开关默认为关闭状态。<br>数据来源：本端规划<br>取值范围：<br>- DETAILSW_OFF（关闭）<br>- DETAILSW_ON（打开）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [提交允许访问策略配置（ALLOWPLCY）](configobject/UNC/20.15.2/ALLOWPLCY.md)

## 使用实例

测试配置的允许访问控制策略：

```
TST ALLOWPLCY: SRCNFTYPE=SMF, TARGETNFTYPE=AMF;
%%TST ALLOWPLCY: SRCNFTYPE=SMF, TARGETNFTYPE=AMF;%%
RETCODE = 0  操作成功

结果如下
------------------------
测试结果  =  {"NfInstanceID":"ff02-1","ServiceInfo":[{"ServiceInstanceID":"service_instance_2","ServiceName":"namf-mt"},{"ServiceInstanceID":"service_instance_3","ServiceName":"namf-loc"}]}
(结果个数  = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试允许访问策略配置（TST-ALLOWPLCY）_09653106.md`
