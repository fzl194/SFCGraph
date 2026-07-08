---
id: UNC@20.15.2@MMLCommand@SET NGSCTPPARA
type: MMLCommand
name: SET NGSCTPPARA（设置N2接口SCTP协议参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NGSCTPPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# SET NGSCTPPARA（设置N2接口SCTP协议参数）

## 功能

适用NF：AMF

该命令用于设置N2接口SCTP协议参数。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 当系统内5G Paging流量导致接口板流量拥塞时，开启Paging消息绑定功能。“SCTP数据绑定方式”设置成“BIND_PAGING_MESSAGES(Paging消息绑定)”后，在绑定定时器时长内发给同一个eNodeB的Paging消息会组成一个包发给eNodeB。对用户的Paging时延有影响。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BUNDLETYPE | SCTP数据绑定方式 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否把多个S2接口消息组在一个SCTP包中发给eNodeB。<br>数据来源：本端规划<br>取值范围：<br>- “NOT_BIND(不绑定)”<br>- “BIND_PAGING_MESSAGES(Paging消息绑定)”<br>系统初始设置值：<br>“NOT_BIND(不绑定)” |
| BUNDLETIME | 绑定等待时长（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于控制S2接口消息一次组包的时间间隔。<br>数据来源：本端规划<br>取值范围：10~100ms<br>系统初始设置值：20ms<br>配置原则：以10ms为粒度配置<br>说明：- 此参数设置越大，对业务增加的时延越大，为兼顾业务时延和组包效率，建议使用系统初始设置值20ms。<br>- “SCTP数据绑定方式”配置成“NOT_BIND(不绑定)”，该参数不生效。<br>- “SCTP数据绑定方式”配置成“BIND_PAGING_MESSAGES(Paging消息绑定)”，则会把该时间段内，发给同一个eNodeB的Paging消息组成一个SCTP包发给eNodeB。<br>- 如果在绑定等待时长内，需要组包的包长超过MTU值，则会按照MTU的长度组包。<br>- 本参数取值为特定话务模型下的评估结果，考虑到现网的话务模型和Paging业务的时延要求，本参数取值强依赖具体的话务模型，请联系华为公司本地机构提供专业的网络评估服务支持。 |
| BUNDLENUM | 最大绑定包数 | 可选必选说明：可选参数<br>参数含义：该参数用于指示SCTP开启组包功能后，一个SCTP包中最大能组的包数（个）。<br>数据来源：本端规划<br>取值范围：2~10<br>系统初始设置值：2 |
| TSCTPDOWN | 防闪断定时器（s） | 可选必选说明：可选参数<br>参数含义：该定时器用于指定N2接口SCTP链路的防闪断定时器时长。在AMF监测到SCTP偶联断时启动，超时后检测SCTP偶联是否重建，如果重建则恢复gNodeB信息，如果没有重建则删除gNodeB信息。<br>数据来源：与对端gNodeB设备协商<br>取值范围：2s~65534s<br>系统初始设置值：40s |

## 操作的配置对象

- [N2接口SCTP协议参数（NGSCTPPARA）](configobject/UNC/20.15.2/NGSCTPPARA.md)

## 使用实例

设置SCTP协议参数信息的SCTP数据绑定方式为不绑定，设置“绑定等待时长（ms）”为30，配置格式如下：

SET NGSCTPPARA: BUNDLETYPE=NOT_BIND , BUNDLETIME=30;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置N2接口SCTP协议参数(SET-NGSCTPPARA)_26306152.md`
