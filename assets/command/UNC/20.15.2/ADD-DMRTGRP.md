---
id: UNC@20.15.2@MMLCommand@ADD DMRTGRP
type: MMLCommand
name: ADD DMRTGRP（增加Diameter路由组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DMRTGRP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 2048
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter路由组
status: active
---

# ADD DMRTGRP（增加Diameter路由组）

## 功能

**适用网元：SGSN、MME**

该命令用于新增一条Diameter路由组。Diameter路由组是由Diameter域路由和Diameter主机路由组成。通过命令 [**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md) 和 **ADD DMHOSTRT** 配置Diameter域路由和主机路由。当与对端进行Diameter连接时，业务通过命令 [**ADD IMSIHSS**](../../../Diameter应用协议/IMSI-HSS转换信息/增加IMSI-HSS对应关系(ADD IMSIHSS)_26145454.md) 引用此路由组的配置来应用相应路由模式。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数2048。
- 同一个Diameter路由组最多可以配置16个主机路由和1个域路由，1个主机路由最多可以配置1个DMPE，1个域路由最多可配置10个DMPE。
- 同一个Diameter路由组下的主机路由的选路模式必须一致。
- 同一个Diameter路由组下，路由优选模式必须一致。
- 不建议在路由组中配置默认域路由，配置默认域路由可能导致选路异常。
- 当路由组配置了非默认域路由时，IMSIHSS配置的“HSS域名”与路由组中域路由索引对应在域路由中的“目的实体域名”需一致。
- 当Diameter路由组应用于S6a/S6d接口，“路由优选模式”为“REALM_ROUTE_PREFER(优选域路由)”时，需要将“路由模式”配置为“REALM_ROUTE(域路由)”，且当“路由索引”在对应[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)中的“选路模式”为“SELMODE_IMSI_PRIORITY(IMSI指定优选)”时，需要配置“路由索引”、“对端实体索引”参数。
- 当Diameter路由组应用于S6a/S6d接口时，需要通过[**ADD IMSIHSS**](../../../Diameter应用协议/IMSI-HSS转换信息/增加IMSI-HSS对应关系(ADD IMSIHSS)_26145454.md)配置引用关系。路由组内添加的主机路由和域路由的“应用名称”需要是“S6A/S6D(S6a/S6d)”。
- 当Diameter路由组应用于SLg接口时，需要通过[**ADD GMLCSELPLCY**](../../../业务安全管理/LCS/GMLC选择策略/增加GMLC选择策略(ADD GMLCSELPLCY)_72225491.md)配置引用关系。路由组内只允许添加“应用名称”为“SLG(SLg)”的主机路由，而且路由组的“路由优选模式”只能是“HOST_ROUTE_PREFER(优选主机路由)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPIDX | 路由组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统范围内标识一条Diameter路由组。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无 |
| RTMODE | 路由模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该条路由的路由索引对应的路由模式。<br>数据来源：整网规划<br>取值范围：<br>- “REALM_ROUTE（域路由）”：表示该条路由的路由模式为域路由模式；<br>- “HOST_ROUTE（主机路由）”：表示该条路由的路由模式为主机路由模式；<br>默认值：HOST_ROUTE（主机路由）<br>配置原则：<br>- 与HSS通过DRA转接或者不明确IMSI与主机名的对应关系时采用“REALM_ROUTE(域路由)”。<br>- 与HSS直连时采用“HOST_ROUTE(主机路由)”。<br>- 与GMLC直连时采用“HOST_ROUTE(主机路由)”。 |
| RTPRIMODE | 路由优选模式 | 可选必选说明：可选参数<br>参数含义：该参数是指在路由组中既存在主机路由又存在域名路由时优先选择的路由模式。<br>数据来源：整网规划<br>取值范围：<br>- “REALM_ROUTE_PREFER(优选域路由)”：表示优先选择域路由；<br>- “HOST_ROUTE_PREFER(优选主机路由)”：表示优先选择主机路由；<br>默认值：<br>“HOST_ROUTE_PREFER(优选主机路由)”<br>配置原则：<br>- 在同一个路由组中，如果选择“REALM_ROUTE_PREFER(优选域路由)”，当域路由指定的对端全部故障时，则选择主机路由指定的对端（HSS）；如果选择“HOST_ROUTE_PREFER(优选主机路由)”，当主机路由指定的对端（HSS）全部故障时，则选择域路由指定的对端。<br>- 同一个Diameter路由组下，“路由优选模式”和“路由组名称”必须相同。<br>- 建议与HSS直连时选择“HOST_ROUTE_PREFER(优选主机路由)”，与DRA连接时选择“REALM_ROUTE_PREFER(优选域路由)”。<br>- 与GMLC直连时选择“HOST_ROUTE_PREFER(优选主机路由)”。 |
| ROUTEIDX | 路由索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于路由索引。<br>数据来源：本端规划<br>取值范围：0~2047<br>默认值：无<br>配置原则：<br>- 路由模式为域路由时该路由索引为[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)中的索引，同一路由组索引下最多只能配置1个。<br>- 路由模式为主机路由时该路由索引为**ADD DMHOSTRT**中的索引，同一路由组索引下最多可配置16个，且主机路由的选路模式必须相同。<br>- 当Diameter路由组应用于S6a/S6d接口，“路由优选模式”为“REALM_ROUTE_PREFER(优选域路由)”，“路由模式”为“REALM_ROUTE(域路由)”，且“路由索引”在对应[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)中的“选路模式”为“SELMODE_IMSI_PRIORITY(IMSI指定优选)”时，此参数必须填写。<br>- 当Diameter路由组应用于S6a/S6d接口，“路由优选模式”为“REALM_ROUTE_PREFER(优选域路由)”，“路由模式”为“REALM_ROUTE(域路由)”，且“路由索引”在对应[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)中的“选路模式”为非“SELMODE_IMSI_PRIORITY(IMSI指定优选)”时，此参数无需填写。如果填写，需要根据[**ADD IMSIHSS**](../../../Diameter应用协议/IMSI-HSS转换信息/增加IMSI-HSS对应关系(ADD IMSIHSS)_26145454.md)配置的“HSS域名”后向最大匹配[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)配置中的“目的实体域名”，选取对应的“路由索引”进行填写。<br>说明：- 在“MML命令行-UNC”窗口上执行命令[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)或者**ADD DMHOSTRT**设置此参数。<br>- ROUTEIDX未配置时，显示为65535。 |
| PEERIDX | 对端实体索引 | 可选必选说明：条件可选参数<br>参数含义：该参数用于标识目的对端。<br>前置条件：该参数在“路由模式”参数配置为“REALM_ROUTE（域路由）”后生效。<br>数据来源：本端规划<br>取值范围：0~639<br>默认值：无<br>配置原则：<br>- 一个路由组索引最多可配置10个对端实体索引。<br>- 对端实体索引必须在对应路由索引的[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)中存在。<br>- “路由模式”为“REALM_ROUTE(域路由)”，且“路由索引”在对应[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)中的“选路模式”为“SELMODE_IMSI_PRIORITY(IMSI指定优选)”时，此参数必须填写。<br>- “路由模式”为“REALM_ROUTE(域路由)”，且“路由索引”在对应[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)中的“选路模式”为非“SELMODE_IMSI_PRIORITY(IMSI指定优选)”时，此参数不能填写。<br>说明：- 在“MML命令行-UNC”窗口上执行命令[**ADD DMRT**](../Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)设置此参数。 |
| ROUTEGRPNAM | 路由组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定添加路由组的名称。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：noname<br>配置原则：同一<br>“路由组索引”<br>下的<br>“路由优选模式”<br>和<br>“路由组名称”<br>必须一致。 |

## 操作的配置对象

- [Diameter路由组（DMRTGRP）](configobject/UNC/20.15.2/DMRTGRP.md)

## 使用实例

增加一个路由模式为域路由，路由优选模式为域路由：

ADD DMRTGRP: GRPIDX=1, RTMODE=REALM_ROUTE, RTPRIMODE=REALM_ROUTE_PREFER, ROUTEIDX=1, PEERIDX=1, ROUTEGRPNAM="dra";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Diameter路由组(ADD-DMRTGRP)_26146292.md`
