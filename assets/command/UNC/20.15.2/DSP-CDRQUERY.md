---
id: UNC@20.15.2@MMLCommand@DSP CDRQUERY
type: MMLCommand
name: DSP CDRQUERY（查询话单）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CDRQUERY
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 话单查询
status: active
---

# DSP CDRQUERY（查询话单）

## 功能

**适用NF：NCG**

该命令用于查询指定话单，并将查询的数据压缩后提供下载。

## 注意事项

- 该命令执行后，只是启动话单查询，查询进度请参见[**DSP CDRQUERYSTATUS**](查询话单查询任务状态（DSP CDRQUERYSTATUS）_74917353.md)的参数说明。
- 正在执行的话单查询任务数最大不超过8个。
- 在网管上执行该命令时，只支持相同版本（包括补丁号）的NCG并行查询，不支持多版本并行查询。
- 执行该MML命令成功后，在OM Portal界面，通过单击“系统 > 文件传输 > NCG话单查询结果文件”，进入话单查询文件系统进行下载。
- 话单查询结果文件在查询结束后保留4小时，超过4小时被老化删除。
- 话单属于个人数据，下载话单存在个人数据泄露风险，系统默认匿名化处理，匿名化开关通过SETCGSECPOLICY命令的“MML话单查询匿名”参数控制。
- 该命令最多支持15万张话单记录结果的保存，话单记录结果超出时请优化查询条件或减少查询的时间范围。
- 查询话单会耗费大量CPU资源，业务繁忙时慎重操作。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 查询任务标识 | 可选必选说明：必选参数<br>参数含义：该参数用来表示查询任务标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| FILETYPE | 文件类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示查询的文件类型。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- Original：原始话单文件<br>- Final：最终话单文件<br>默认值：无<br>配置原则：无。 |
| RECORDTYPE | 话单类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILETYPE”配置为“Original”或者“Final”时为条件必选参数。<br>参数含义：该参数用来表示查询的话单类型。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- chargingFunctionRecord：CHF-CDR<br>- sgsnPDPRecord：S-CDR<br>- ggsnPDPRecord：G-CDR<br>- sgsnMMRecord：M-CDR<br>- sgsnSMORecord：S-SMO-CDR<br>- sgsnSMTRecord：S-SMT-CDR<br>- sgsnLCTRecord：LCS-MT-CDR<br>- sgsnLCORecord：LCS-MO-CDR<br>- sgsnLCNRecord：LCS-NI-CDR<br>- egsnPDPRecord：EG-CDR<br>- sgsnMBMSRecord：S-MB-CDR<br>- ggsnMBMSRecord：G-MB-CDR<br>- sGWRecord：SGW-CDR<br>- pGWRecord：PGW-CDR<br>- gwMBMSRecord：GW-MB-CDR<br>默认值：无<br>配置原则：无。 |
| SDATETIME | 话单文件起始时间 | 可选必选说明：必选参数<br>参数含义：该参数用来表示查询话单文件的起始日期和时间。<br>数据来源：本端规划<br>取值范围：时间类型<br>默认值：无<br>配置原则：无。 |
| EDATETIME | 话单文件终止时间 | 可选必选说明：必选参数<br>参数含义：该参数用来表示查询话单文件的终止日期和时间。<br>数据来源：本端规划<br>取值范围：时间类型<br>默认值：无<br>配置原则：无。 |
| AGID | 接入网元分组标识 | 可选必选说明：必选参数<br>参数含义：该参数用来表示查询的接入网元分组标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| MNAME | 模块名 | 可选必选说明：可选参数<br>参数含义：该参数用来表示查询的模块名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| SOURCECHL | 通道名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FILETYPE”配置为“Final”时为条件必选参数。当“RECORDTYPE”配置为“chargingFunctionRecord”，该参数可以填写“CHANNLE_ALL”查询R15:CHF-CDR话单类型的所有通道话单。<br>参数含义：该参数用来表示查询的通道名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“sgsnSMORecord”、“sgsnSMTRecord”、“sgsnLCTRecord”、“sgsnLCORecord”、“sgsnLCNRecord”、“egsnPDPRecord”、“sGWRecord”或者“pGWRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的IMSI值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| IMEI | IMEI | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“sgsnSMORecord”、“sgsnSMTRecord”、“sgsnLCNRecord”、“egsnPDPRecord”、“sGWRecord”或者“pGWRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的IMEI值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| MSISDN | MSISDN | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“sgsnSMORecord”、“sgsnSMTRecord”、“sgsnLCTRecord”、“sgsnLCORecord”、“sgsnLCNRecord”、“egsnPDPRecord”、“sGWRecord”或者“pGWRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的MSISDN值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| MAXCHARGINGID | MAX Charging ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”、“sGWRecord”、“pGWRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的Charging ID的上限值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～12。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| MINCHARGINGID | Min Charging ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”、“sGWRecord”、“pGWRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的Charging ID的下限值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～12。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| APNNI | APNNI | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“sgsnPDPRecord”、“ggsnPDPRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”、“sGWRecord”、“pGWRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的APNNI值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| SGSNADDRESS | SGSN Address | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“sgsnLCTRecord”、“sgsnLCORecord”、“sgsnLCNRecord”或者“egsnPDPRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的SGSN Address值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～46。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| GGSNADDRESS | GGSN Address Used | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“sgsnPDPRecord”、“ggsnPDPRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”或者“ggsnMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的GGSN Address Used值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～46。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| PDPADDRESS | Served PDP Address | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“sgsnPDPRecord”、“ggsnPDPRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”、“sGWRecord”、“pGWRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的Served PDP Address值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～46。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| SERNODEADDRESS | ServingNodeAddress | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“sGWRecord”或者“pGWRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的ServingNodeAddress值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～46。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| PGWADDRESS | PGWAddress | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“pGWRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的PGWAddress值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～46。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| SGWADDRESS | SGWAddress | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“sGWRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的SGWAddress值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～46。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| SRECOPENTIME | Start Record Opening Time | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”、“sGWRecord”、“pGWRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的Record Opening Time的起始日期和时间。<br>数据来源：本端规划<br>取值范围：时间类型。<br>默认值：无<br>配置原则：无。 |
| ERECOPENTIME | End Record Opening Time | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”、“sGWRecord”、“pGWRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的Record Opening Time的终止日期和时间。<br>数据来源：本端规划<br>取值范围：时间类型。<br>默认值：无<br>配置原则：无。 |
| SEVENTTIME | Start EventTimeStamp | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“sgsnSMORecord”、“sgsnSMTRecord”、“sgsnLCTRecord”、“sgsnLCORecord”或者“sgsnLCNRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的EventTimeStamp的起始日期和时间。<br>数据来源：本端规划<br>取值范围：时间类型。<br>默认值：无<br>配置原则：无。 |
| EEVENTTIME | End EventTimeStamp | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“sgsnSMORecord”、“sgsnSMTRecord”、“sgsnLCTRecord”、“sgsnLCORecord”或者“sgsnLCNRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的EventTimeStamp的终止日期和时间。<br>数据来源：本端规划<br>取值范围：时间类型。<br>默认值：无<br>配置原则：无。 |
| MAXDURATION | Max Duration | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“sgsnLCTRecord”、“sgsnLCORecord”、“sgsnLCNRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”、“sGWRecord”、“pGWRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的Duration的上限值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～12。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| MINDURATION | Min Duration | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“sgsnLCTRecord”、“sgsnLCORecord”、“sgsnLCNRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”、“sGWRecord”、“pGWRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的Duration的下限值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～12。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| MAXRECSEQNUM | Max Record Sequence Number | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnMMRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的Record Sequence Number的上限值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～12。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| MINRECSEQNUM | Min Record Sequence Number | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnMMRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的Record Sequence Number的下限值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～12。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| MAXRATYPE | Max Rattype | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“sgsnSMORecord”、“sgsnSMTRecord”、“sgsnLCTRecord”、“sgsnLCORecord”、“sgsnLCNRecord”、“egsnPDPRecord”、“sGWRecord”或者“pGWRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的Rattype的上限值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～12。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| MINRATYPE | Min Rattype | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“sgsnSMORecord”、“sgsnSMTRecord”、“sgsnLCTRecord”、“sgsnLCORecord”、“sgsnLCNRecord”、“egsnPDPRecord”、“sGWRecord”或者“pGWRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的Rattype的下限值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～12。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| CC | ChargingCharacteristics | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“sgsnSMORecord”、“sgsnSMTRecord”、“sgsnLCTRecord”、“sgsnLCORecord”、“sgsnLCNRecord”、“egsnPDPRecord”、“sGWRecord”或者“pGWRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的ChargingCharacteristics值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| CLOSECAUSE | CauseForRecClosing | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”、“sgsnPDPRecord”、“ggsnPDPRecord”、“sgsnMMRecord”、“egsnPDPRecord”、“sgsnMBMSRecord”、“ggsnMBMSRecord”、“sGWRecord”、“pGWRecord”或者“gwMBMSRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的CauseForRecClosing值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- normalRelease：normalRelease<br>- abnormalRelease：abnormalRelease<br>- cAMELInitCallRelease：cAMELInitCallRelease<br>- volumeLimit：volumeLimit<br>- timeLimit：timeLimit<br>- servingNodeChange：servingNodeChange<br>- maxChangeCond：maxChangeCond<br>- managementIntervention：managementIntervention<br>- intraSGSNIntersystemChange：intraSGSNIntersystemChange<br>- rATChange：rATChange<br>- mSTimeZoneChange：mSTimeZoneChange<br>- sGSNPLMNIDChange：sGSNPLMNIDChange<br>- sGWChange：sGWChange<br>- aPNAMBRChange：aPNAMBRChange<br>- mOExceptionDataCounterReceipt：mOExceptionDataCounterReceipt<br>- unauthorizedRequestingNetwork：unauthorizedRequestingNetwork<br>- unauthorizedLCSClient：unauthorizedLCSClient<br>- positionMethodFailure：positionMethodFailure<br>- unknownOrUnreachableLCSClient：unknownOrUnreachableLCSClient<br>- listofDownstreamNodeChange：listofDownstreamNodeChange<br>默认值：无<br>配置原则：无。 |
| PDUIPV4 | PDUIPv4Address | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的PDUIPv4Address值。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无。 |
| PDUIPV6 | PDUIPv6Address | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的PDUIPv6Address值。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无。 |
| DATANETID | DataNetworkNameIdentifier | 可选必选说明：条件可选参数<br>前提条件：该参数在“RECORDTYPE”配置为“chargingFunctionRecord”时为条件可选参数。<br>参数含义：该参数用来表示查询的话单的DataNetworkNameIdentifier值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |
| CHARSEID | ChargingSessionIdentifier | 可选必选说明：必选参数<br>参数含义：该参数用来表示查询的话单的ChargingSessionIdentifier值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。<br>默认值：无<br>配置原则：不能输入的特殊字符请参考“<br>[**特殊字符表**](../../业务配置管理/话单稽核/增加话单稽核（ADD CDRAUDIT）_51174239.md#ZH-CN_CONCEPT_0251174239__table_0365FEF0)<br>”。 |

## 操作的配置对象

- [话单（CDRQUERY）](configobject/UNC/20.15.2/CDRQUERY.md)

## 使用实例

查询“查询任务标识”为“task”，“文件类型”为“原始话单文件”，“话单类型”为“SCDR”，“起始时间”为“2022–08–11 16:26:01”，“终止时间”为“2022–08–12 16:26:01”，接入网元分组标识为“PS1”，模块名为“AP64_1”的话单。示例如下：

```
DSP CDRQUERY: TASKID="task", FILETYPE=Original, RECORDTYPE=sgsnPDPRecord, SDATETIME=2022&08&11&16&26&01, EDATETIME=2022&08&11&16&26&03, AGID="PS1", MNAME="AP64_1";
```

```
RETCODE = 0  操作成功
结果如下:
---------
查询任务标识  =  task
查询启动状态  =  成功
    补充信息  =  启动任务成功
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话单（DSP-CDRQUERY）_23797342.md`
