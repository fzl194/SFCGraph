---
id: UNC@20.15.2@MMLCommand@ADD DMHOSTRT
type: MMLCommand
name: ADD DMHOSTRT（增加Diameter主机路由）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DMHOSTRT
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter主机路由
status: active
---

# ADD DMHOSTRT（增加Diameter主机路由）

## 功能

**适用网元：SGSN、MME**

该命令用于新增一条Diameter主机路由。主机路由是指通过请求消息中的destination-host信元来选择对端。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数1024。
- 当本配置应用于S6a/S6d或者S13接口时，如果BYTE_EX17 BIT1置为1，本配置不生效。
- 在UNC和HSS或者GMLC直连时使用此命令。相同选路模式的主机路由可以通过命令[**ADD DMRTGRP**](../Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md)配到同一个Diameter路由组中，业务通过引用路由组配置进行选路。
- 若Diameter路由组中存在属于该Diameter主机路由的“路由索引”，则配置才能生效。Diameter路由组信息请参考[**LST DMRTGRP**](../Diameter路由组/查询Diameter路由组(LST DMRTGRP)_26306104.md)命令。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ROUTEIDX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统范围内标识一条Diameter主机路由。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无 |
| APPNAM | 应用名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该条主机路由对应的应用接口类型。<br>数据来源：整网规划<br>取值范围：<br>- “S6A/S6D(S6a/S6d)”：表示该主机路由用于S6a/S6d接口，在对端网元为HSS时，选择该应用。<br>- “S13(S13)”：表示该主机路由用于S13接口，在对端网元为EIR时，选择该应用。<br>- “SLG(SLg)”：表示该主机路由用于SLg接口，在对端网元为GMLC时，选择该应用。<br>- “T6A/T6AI/T6B/T6BI(T6a/T6ai/T6b/T6bi)”：表示该主机路由用于T6a/T6ai/T6b/T6bi接口。其中T6a为MME到SCEF的接口；T6ai为MME到IWK-SCEF的接口；T6b为SGSN到SCEF的接口；T6bi为SGSN到IWK-SCEF的接口。<br>默认值：S6A/S6D(S6a/S6d)<br>配置原则：<br>- 目前不支持S13(S13) |
| RSELMODE | 选路模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主机路由选择对端的模式。<br>数据来源：整网规划<br>取值范围：<br>- “SELMODE_ROUND_ROBIN(轮选)”：当同一Diameter路由组存在多条Diameter主机路由时，采用顺序选择的方式选择主机路由。这种选路模式在负荷分担场景时使用。<br>- “SELMODE_MASTER_SLAVE(主从)”：当同一Diameter路由组存在多条Diameter主机路由时，采用主从选择的方式选择主机路由。主从关系根据配置的优先级来确定，参见PRIORITY参数。这种选路模式在主备场景时使用。<br>- “SELMODE_PRIORITY_WEIGHT(优先级权重)”：表示同一Diameter路由组存在多条Diameter主机路由时，先根据优先级选择主机路由，优先级相同时，再根据权重选择主机路由。 这种选路模式用于对端设备支持不同的接入能力时，通过指定不同的权重来使得能力较强的设备可以处理更多的消息。通过指定优先级可将设备根据优先级分组，支持复杂的负载分担方式。<br>默认值：SELMODE_MASTER_SLAVE(主从)<br>说明：- 如果此主机路由配到Diameter路由组中，同一Diameter路由组下主机路由的选路模式必须相同。在“MML命令行-UNC”窗口上执行命令[**LST DMRTGRP**](../Diameter路由组/查询Diameter路由组(LST DMRTGRP)_26306104.md)查询路由组配置。<br>- “目的实体选择方式”为“PEER_HOST_NAME(对端主机名)”的主机路由不能配置成“SELMODE_MASTER_SLAVE(主从)”模式<br>- 当参数设置为“SELMODE_PRIORITY_WEIGHT(优先级权重)”时，“基于权重/优先级的Diameter负荷分担”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-104404，License项：LKV2DMLS01）。 |
| PEERSEL | 目的实体选择方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端选择方式。为了保持兼容性，可以选择对端索引或者对端主机名两种方式标识对端。<br>数据来源：对端协商<br>取值范围：<br>- “PEER_INDEX(对端索引)”<br>- “PEER_HOST_NAME(对端主机名)”<br>默认值：PEER_INDEX(对端索引)<br>说明：只有要添加的对端主机名在DMPE中未配置，才允许将<br>“目的实体选择方式”<br>配置为<br>“PEER_HOST_NAME(对端主机名)”<br>。 |
| PEERIDX | 对端实体索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于标识目的对端。<br>数据来源：本端规划<br>取值范围：0~639<br>默认值：无<br>说明：- 该参数在“目的实体选择方式”设置为“PEER_INDEX(对端索引)”有效。<br>- 该对端需支持该条主机路由的“应用名称”。<br>- 建议网元类型为HSS的对端索引被主机路由引用。<br>- 在“MML命令行-UNC”窗口上执行命令[**ADD DMPE**](../Diameter对端实体/增加Diameter对端实体(ADD DMPE)_72225963.md)设置此参数。 |
| PEERHTNAM | 对端主机名 | 可选必选说明：条件必选参数<br>参数含义：该参数用于标识目的对端的主机名。<br>数据来源：全网规划<br>取值范围：1~127位字符串。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“.”，其他均为非法字符<br>默认值：无<br>说明：- 该参数在“目的实体选择方式”设置为“PEER_HOST_NAME(对端主机名)”有效。<br>- 如果该参数在DMPE中已配置，请将“目的实体选择方式”选择为“PEER_INDEX(对端索引)”，在“对端实体索引”中引用该DMPE的“对端实体索引”。 |
| ROUTENAM | 路由名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定添加主机路由的名称。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。 |
| PRIORITY | 优先级 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定主机路由中对端的优先级。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>说明：- 该参数在“选路模式”设置为“SELMODE_MASTER_SLAVE(主从)”时和“SELMODE_PRIORITY_WEIGHT(优先级权重)”有效，如果该参数未配置，则系统默认优先级为0。<br>- 当“选路模式”设置为“SELMODE_MASTER_SLAVE(主从)”时，同一路由组索引中主机路由的优先级不能相同。在“MML命令行-UNC”窗口上执行命令[**LST DMRTGRP**](../Diameter路由组/查询Diameter路由组(LST DMRTGRP)_26306104.md)查询路由组配置。<br>- 数值越小，优先级越高。 |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主机路由中对端的权重。<br>数据来源：整网规划<br>取值范围：1～255<br>默认值：1<br>说明：- 该参数只在“选路模式”设置为“SELMODE_PRIORITY_WEIGHT(优先级权重)”有效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMHOSTRT]] · Diameter主机路由（DMHOSTRT）

## 使用实例

增加一个选路模式为优先级权重，对端实体选择方式为对端索引的主机路由:

ADD DMHOSTRT: ROUTEIDX=1, RSELMODE=SELMODE_PRIORITY_WEIGHT, PEERSEL=PEER_INDEX, PEERIDX=1, ROUTENAM="DRA", PRIORITY=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Diameter主机路由(ADD-DMHOSTRT)_26146272.md`
