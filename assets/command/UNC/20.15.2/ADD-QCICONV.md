---
id: UNC@20.15.2@MMLCommand@ADD QCICONV
type: MMLCommand
name: ADD QCICONV（增加扩展QCI转换关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QCICONV
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 245
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- 扩展QCI转换关系
status: active
---

# ADD QCICONV（增加扩展QCI转换关系）

## 功能

**适用网元：MME**

该命令用于增加扩展QCI（QoS Class Identifier）向标准QCI的转换关系配置表。扩展QCI是指取值大于9并小于255的QCI，当UE不支持扩展QCI时，则需要将扩展QCI转换为标准QCI（取值为1～9）。

当在承载创建和承载修改的流程中，会对QCI的值进行标准化转换。

## 注意事项

- 该命令执行后立即生效。
- 此命令的最大记录数为245。
- 如果没有配置扩展QCI向标准QCI的转换关系配置表，系统会默认将此扩展QCI转换为标准QCI值9。
- 如果扩展QCI与QCI范围值确定的扩展QCI范围内已有相关记录，命令将执行失败。
- UNC按照此配置，把P-GW下发的扩展QCI转换为标准QCI后发送给UE，同时也会把P-GW下发的MBR（Maximum Bit Rate）/GBR（Guaranteed Bit Rate）发给UE。因此扩展QCI与标准QCI之间的映射关系，需要运营商端到端规划，确保P-GW、MME、eNodeB等设备上规划一致，否则，可能会导致端到端QoS的不一致，影响用户业务感受。
- 此配置涉及基于用户等级的QCI扩展特性（特性编号：WSFD-105103，License部件编码：LKV2QCIE02），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。
- 部署“LTE一键通”特性时，推荐的QCI映射关系如[表1](#ZH-CN_MMLREF_0000001126306024__tab1)所示。
  *表1 PTT专用QCI和标准QCI推荐映射关系*

  | PTT专用QCI | 标准QCI |
  | --- | --- |
  | 65 | 1 |
  | 66 | 1 |
  | 69 | 5 |
  | 70 | 6 |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCIEXT | 扩展QCI基准值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展QCI基准值。<br>数据来源：整网规划<br>取值范围：10～254<br>默认值：无<br>说明：扩展QCI是指取值大于9并小于255的QCI，当UE不支持扩展QCI时，则需要将扩展QCI转换为标准QCI（取值为1～9）。 |
| QCISTEP | 扩展QCI范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展QCI取值范围值。扩展QCI范围是指<br>“扩展QCI基准值”<br>加上<br>“扩展QCI范围”<br>，在这一范围内的扩展QCI都统一的转换为一标准QCI的值。<br>数据来源：整网规划<br>取值范围：0～244<br>默认值：无<br>配置原则：<br>“扩展QCI范围”<br>与<br>“扩展QCI基准值”<br>之和必须大于9并小于255。<br>说明：如果不输入，则表示增加扩展QCI值为扩展QCI基准值向QCI标准值的转换关系。 |
| QCISTD | 标准QCI值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定转换后的标准QCI值。标准QCI值是指协议规定的QCI取值范围(1～9)内的QCI值。<br>数据来源：整网规划<br>取值范围：<br>- 1～4：GBR业务的标准QCI值。<br>- 5～9：Non-GBR业务的标准QCI值。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QCICONV]] · 扩展QCI转换关系（QCICONV）

## 使用实例

增加扩展QCI值从10到30转换为标准QCI值1的关系配置表：

ADD QCICONV: QCIEXT=10, QCISTEP=20, QCISTD=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加扩展QCI转换关系(ADD-QCICONV)_26306024.md`
