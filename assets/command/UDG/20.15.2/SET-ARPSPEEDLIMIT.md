---
id: UDG@20.15.2@MMLCommand@SET ARPSPEEDLIMIT
type: MMLCommand
name: SET ARPSPEEDLIMIT（配置速率限制）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ARPSPEEDLIMIT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP系统配置
status: active
---

# SET ARPSPEEDLIMIT（配置速率限制）

## 功能

该命令用于设置ARP报文或者ARP Miss消息的抑制速率。非法用户使用大量的ARP报文对目标设备攻击时，将导致设备将大量资源浪费在处理ARP报文上，影响设备对其他业务的处理；或者非法用户利用工具扫描本网段内的主机或者跨网段进行扫描时，会导致设备因目的IP地址对应的MAC地址不存在，而产生大量的ARP Miss消息，导致设备大量的资源都浪费在处理ARP Miss消息上，影响设备对其他业务的处理。为了解决该问题，用户可以配置基于IP地址对ARP报文或者ARP-Miss消息进行限速，在一定时间内处理指定数目以内的ARP报文或ARP-Miss消息，保证业务的正常运行。

## 注意事项

- 该命令执行后立即生效。
- 当参数SUPPTYPE取值为ARP Miss时，参数SUPPBASETYPE只能取值为Src IP。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| SUPPTYPE | SUPPBASETYPE | SUPPVALUE |
| --- | --- | --- |
| ARP | Src_Ip | 100 |
| ARP | Dest_Ip | 500 |
| ARP-miss | Src_Ip | 500 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUPPTYPE | 抑制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置ARP的报文限速还是ARP Miss的消息限速。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ARP：针对ARP报文上送速率进行抑制。<br>- ARP-miss：针对上送的ARP Miss消息上送速率进行抑制。<br>默认值：无 |
| SUPPBASETYPE | 抑制基础类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定限速方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Dest_Ip：基于目的IP地址进行时间戳抑制。<br>- Src_Ip：基于源IP地址进行时间戳抑制。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：需要配置限速功能的资源单元名称。通过DSP RU命令可以查询资源单元信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| SUPPVALUE | 抑制值（pps） | 可选必选说明：必选参数<br>参数含义：报文限速值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65536。<br>默认值：无<br>配置原则：推荐ARP报文限速值为500。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPSPEEDLIMIT]] · 速率限制（ARPSPEEDLIMIT）

## 使用实例

对VNODE_VNRS_VNFC_OMU_0001基于源IP对上送的ARP报文速率进行抑制，速率为每秒1000个报文：

```
SET ARPSPEEDLIMIT:SUPPTYPE=ARP,SUPPBASETYPE=Src_Ip,RUNAME="VNODE_VNRS_VNFC_OMU_0001",SUPPVALUE=1000;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置速率限制（SET-ARPSPEEDLIMIT）_00840941.md`
