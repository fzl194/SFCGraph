---
id: UNC@20.15.2@MMLCommand@ADD LLCXID
type: MMLCommand
name: ADD LLCXID（增加LLC协商参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LLCXID
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 4
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- LLC参数
status: active
---

# ADD LLCXID（增加LLC协商参数）

## 功能

**适用网元：SGSN**

该命令用于增加GB接口LLC层XID协商参数配置。

## 注意事项

- 该命令执行立即生效。
- 本表最大记录数为4。
- 可以通过这个命令来修改系统缺省的XID参数N201-U，T200配置。SGSN为后续接入的用户使用新的XID参数配置进行协商。如果没有对某个SAPI增加XID参数配置，则系统将使用3GPP 44.064定义的缺省值（N201-U为500字节，T200为5s（SAPI3），10s（SAPI5），20s（SAPI9），40s（SAPI11））。已增加的XID参数配置可以通过[**MOD LLCXID**](修改LLC协商参数(MOD LLCXID)_72225695.md)命令修改，[**LST LLCXID**](查询LLC协商参数(LST LLCXID)_26305826.md)命令查看。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SAPI | SAPI | 可选必选说明：必选参数<br>参数含义：该参数用于设置SAPI。LLC层用SAPI来识别所使用的服务名称。<br>数据来源：整网规划<br>取值范围：<br>- “SAPI3(SAPI3)”<br>- “SAPI5(SAPI5)”<br>- “SAPI9(SAPI9)”<br>- “SAPI11(SAPI11)”<br>默认值：无<br>说明：SAPI3，SAPI5，SAPI9，SAPI11表示用户数据。 |
| N201U | SN-UNITDATA PDU最大字节数 | 可选必选说明：必选参数<br>参数含义：该参数用于设置U帧的信息域最大长度。<br>数据来源：整网规划<br>取值范围：140～1520<br>默认值：无 |
| T200 | LLC重传定时器（s） | 可选必选说明：必选参数<br>参数含义：该参数用于设置LLC层重传定时器时长。发消息时启定时器，在定时器时长内收到对端的回复消息则停定时器，否则重发3次。<br>数据来源：整网规划<br>取值范围：5s～40s<br>默认值：无 |

## 操作的配置对象

- [LLC协商参数（LLCXID）](configobject/UNC/20.15.2/LLCXID.md)

## 使用实例

增加SAPI为3的一条配置，N201U为1520，T200为40秒：

ADD LLCXID: SAPI=SAPI3, N201U=1520, T200=40;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加LLC协商参数(ADD-LLCXID)_72345615.md`
