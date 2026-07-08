---
id: UNC@20.15.2@MMLCommand@MOD PGWRESEL
type: MMLCommand
name: MOD PGWRESEL（修改本地P-GW重选策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PGWRESEL
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 本地P-GW重选功能配置
status: active
---

# MOD PGWRESEL（修改本地P-GW重选策略）

## 功能

**适用网元：MME**

该命令用于修改一条本地P-GW重选策略的配置记录。UE在网络在中移动，可能造成S-GW与P-GW不属于同一区域。增加该配置后，系统可以针对指定APN的PDN连接，在对用户业务无影响的前提下，为UE重新选择和S-GW在同一区域的本地P-GW进行业务，节省网络中异地S-GW和P-GW之间的迂回流量，降低业务时延。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为32。
- 此配置涉及本地“P-GW的PDN重建”特性（特性编号：WSFD-205007，license部件编码：LKV2PRLP01），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。当PDN使用了该APN网络标识，系统对其进行本地P-GW重选的识别和处理。<br>数据来源：全网规划<br>取值范围：1~62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| NBEGIN | 区域标识起始Label | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域标识的域名起始Label位置。假设其取值为N，N表示从设备Host Name最后一个Label向前数的第N个Label。<br>数据来源：全网规划<br>取值范围：1～20<br>默认值：无<br>配置原则：<br>- 本参数和“区域标识终止Label”一起，表示作为区域标识的域名Label位置范围，记为Nbegin~Nend。<br>- 当用户PDN连接使用的S-GW和P-GW的HostName都是以“topon”Label开头，并且Nbegin Label后的各Label完全相同时，系统会对这两个Host Name的Canonical Node Name部分的第Nbegin~Nend个Label进行比较：如果完全相同，说明P-GW与本地S-GW属于同一区域，这样的P-GW被称为本地P-GW；否则，说明P-GW与本地S-GW不属于同一区域，这样的P-GW被称为非本地P-GW。<br>- 对于使用非本地P-GW的PDN连接，在满足“触发条件”参数定义的条件时，系统会发起P-GW重选过程，要求UE重建PDN，尝试选择本地P-GW。 |
| NEND | 区域标识终止Label | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域标识的域名起始Label位置。假设其取值为N，N表示从设备Host Name最后一个Label向前数的第N个Label。<br>数据来源：全网规划<br>取值范围：1～20<br>默认值：无<br>配置原则：该参数的取值需要大于等于“区域标识起始Label”，请参见“区域标识起始Label”参数的说明。 |
| TRIGGER | 触发条件 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统针对非本地P-GW的PDN连接发起P-GW重选过程的触发条件。<br>数据来源：全网规划<br>取值范围：<br>- “TIME(根据指定时间)”<br>- “BEARER(根据承载状态)”<br>默认值：无<br>配置原则：<br>- TIME(根据指定时间)：每天的固定时段，UE处于ECM-IDLE状态的时间超过一定的时间阈值后，系统发起的P-GW重选过程。对用于PS数据业务的PDN连接，建议采用该方式。<br>- BEARER(根据承载状态)：当用户没有QCI为1或2的承载时，系统发起P-GW重选过程。对用于IMS语音业务的PDN连接，推荐使用该方式。 |
| ST | 起始时间 | 可选必选说明：条件可选参数<br>参数含义：该参数指定了系统进行P-GW重选处理的起始时间。<br>前提条件：该参数在<br>“触发条件”<br>参数设置为<br>“TIME(根据指定时间)”<br>后生效。<br>数据来源：全网规划<br>取值范围：00:00:00~23:59:59<br>默认值：无<br>配置原则：该参数与“结束时间”构成一段时间区间。P-GW重选过程会引起Paging、PDN连接断连/建立等业务流程增多，增加系统负荷，因此建议选择凌晨等系统业务负荷较轻的时间段。 |
| ET | 结束时间 | 可选必选说明：条件可选参数<br>参数含义：该参数指定了系统进行P-GW重选处理的结束时间。<br>前提条件：该参数在<br>“触发条件”<br>参数设置为<br>“TIME(根据指定时间)”<br>后生效。<br>数据来源：全网规划<br>取值范围：00:00:00~23:59:59<br>默认值：无<br>配置原则：该参数与“起始时间”构成一段时间区间。 如果该参数与“起始时间”都为00：00：00，表示一整天24小时。 |
| ECMIDLETIME | ECM-IDLE状态时间阈值（秒） | 可选必选说明：条件可选参数<br>参数含义：该参数指定了UE处于ECM-IDLE状态的时间阈值。<br>前提条件：该参数在<br>“触发条件”<br>参数设置为<br>“TIME(根据指定时间)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0~3600秒<br>默认值：无<br>配置原则：0表示UE进入ECM-IDLE状态后，系统立即发起P-GW重选过程。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PGWRESEL]] · 本地P-GW重选策略（PGWRESEL）

## 使用实例

修改一条 “APN网络标识” 为HUAWEI记录， “区域标识起始Label” 修改为1、 “区域标识终止Label” 修改为2、 “起始时间” 修改为00:00:00、 “结束时间” 修改为23:16:56、 “ECM-IDLE状态时间阈值(秒)” 修改为70。

MOD PGWRESEL: APNNI="HUAWEI", NBEGIN=1, NEND=2, TRIGGER=TIME, ST=00&00&00, ET=23&16&56, ECMIDLETIME=70;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PGWRESEL.md`
