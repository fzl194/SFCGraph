---
id: UNC@20.15.2@MMLCommand@ADD GMLCSELPLCY
type: MMLCommand
name: ADD GMLCSELPLCY（增加GMLC选择策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GMLCSELPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC选择策略
status: active
---

# ADD GMLCSELPLCY（增加GMLC选择策略）

## 功能

**适用网元：MME**

该命令用于增加GMLC选择策略。产品可以根据LCS客户端类型和位置信息来选择Diameter路由组和GMLC域名，从而选择GMLC。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为2048。
- 相同GMLC选择策略组内，同一LCS客户端类型下的位置区域范围不能重叠。
- 此配置涉及位置定位服务（LCS）特性（特性编号：WSFD-106401，license部件编码：LKV2LCS02），请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCGRPID | GMLC选择策略组索引 | 可选必选说明：必选参数<br>参数含义：该参数在系统内唯一标识一个GMLC组。<br>数据来源：本端规划<br>取值范围：0~191<br>默认值：无<br>配置原则：该参数需要在<br>[**ADD GMLCSELGRP**](../GMLC选择策略组/增加GMLC选择策略组(ADD GMLCSELGRP)_26145810.md)<br>中事先配置，可执行<br>[**LST GMLCSELGRP**](../GMLC选择策略组/查询GMLC选择策略组(LST GMLCSELGRP)_72345411.md)<br>进行查看。 |
| LCSCLIENTTYPE | LCS客户端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识LCS客户端类型。<br>数据来源：整网规划<br>取值范围：<br>- “EMERGENCY_SERVICES(紧急业务)”<br>- “VALUE_ADDED_SERVICES(增值业务)”<br>- “PLMN_OPERATOR_SERVICES(运营商业务)”<br>- “LAWFUL_INTERCEPT_SERVICES(合法定位)”<br>默认值：无<br>配置原则：目前就紧急呼叫类型触发的NI-LR流程会选择GMLC，其他参数取值预留使用。 |
| LOCATIONTYPE | 位置区标识类型 | 可选必选说明：必选参数<br>参数含义：该参数标识位置标识类型。<br>数据来源：整网规划<br>取值范围：<br>- “ECI(小区标识)”<br>- “TAC(跟踪区编码)”<br>默认值：无<br>配置原则：相同GMLC选择策略组内，同一LCS客户端类型下优先匹配“位置区标识类型”参数为“小区标识”的记录。 |
| TACBEGIN | 跟踪区起始编码 | 可选必选说明：条件必选参数<br>参数含义：该参数表示跟踪区起始编码。<br>前提条件：该参数在"位置区标识类型"参数配置为"跟踪区编码"后生效。<br>数据来源：整网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| TACEND | 跟踪区结束编码 | 可选必选说明：条件可选参数<br>参数含义：该参数表示跟踪区结束编码。<br>前提条件：该参数在"位置区标识类型"参数配置为"跟踪区编码"后生效。<br>数据来源：整网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无<br>配置原则：<br>- 本参数与跟踪区起始编码配合使用，表示配置从跟踪区起始编码到本参数之间的一段范围。<br>- 如果该参数不输入，表示配置单个TAC。<br>- 该参数取值需要大于等于“跟踪区起始编码”。 |
| ECIBEGIN | 小区起始标识 | 可选必选说明：条件必选参数<br>参数含义：该参数表示E-UTRAN小区起始标识。<br>前提条件：该参数在"位置区标识类型"参数配置为"小区标识"后生效。<br>数据来源：整网规划<br>取值范围：0~268435455<br>默认值：无 |
| ECIEND | 小区结束标识 | 可选必选说明：条件可选参数<br>参数含义：该参数表示E-UTRAN小区结束标识。<br>前提条件：该参数在"位置区标识类型"参数配置为"小区标识"后生效。<br>数据来源：整网规划<br>取值范围：0~268435455<br>默认值：无<br>配置原则：<br>- 本参数与小区起始标识配合使用，表示配置从小区起始标识到本参数之间的一段范围。<br>- 如果该参数不输入，表示配置单个ECI。<br>- 该参数取值需要大于等于“小区起始标识”。 |
| REALMNAME | GMLC域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GMLC域名。<br>数据来源：整网规划<br>取值范围：1~127位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”，不区分大小写。例如：gmlc.epc.mnc123.mcc123.3gppnetwork.org。<br>- 不允许配置字符串“NULL”。<br>- 与对端GMLC配置的GMLC域名保持一致。 |
| GRPIDX | Diameter路由组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统范围内标识一条Diameter路由组。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无<br>配置原则：<br>- 通过命令[**ADD DMRTGRP**](../../../信令传输管理/Diameter管理/Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md)设置此参数。<br>- SLg接口中的消息必须要携带对端主机名，所以需要保证Diameter路由组中只有主机路由，并且是优选主机路由模式。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC选择策略的描述信息。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLCSELPLCY]] · GMLC选择策略（GMLCSELPLCY）

## 使用实例

在索引为0的GMLC选择策略组内添加一条记录。使所有ECI区域内的紧急呼叫类型的NI-LR都上报到索引为1的Diameter路由组内的GMLC上，其中GMLC的域名为“gmlc.epc.mnc123.mcc123.3gppnetwork.org”。

ADD GMLCSELPLCY: GMLCGRPID=0, LCSCLIENTTYPE=EMERGENCY_SERVICES, LOCATIONTYPE=ECI, ECIBEGIN=0, ECIEND=268435455, REALMNAME="gmlc.epc.mnc123.mcc123.3gppnetwork.org", GRPIDX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加GMLC选择策略(ADD-GMLCSELPLCY)_72225491.md`
