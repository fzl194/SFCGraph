---
id: UDG@20.15.2@MMLCommand@RMV PROTBINDSRVS
type: MMLCommand
name: RMV PROTBINDSRVS（删除业务统计协议绑定配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PROTBINDSRVS
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新流生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务统计协议绑定
status: active
---

# RMV PROTBINDSRVS（删除业务统计协议绑定配置）

## 功能

**适用NF：PGW-U、UPF**

![](删除业务统计协议绑定配置（RMV PROTBINDSRVS）_82837389.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定业务统计对象与指定或所有的协议或协议组的绑定关系，会导致匹配到协议的业务无法统计到业务统计对象中，请谨慎使用。

该命令用于删除基于业务的性能统计组合中的Protocol和Protocol Group对象，取消相应七层协议类型报文的上下行数据包数及字节数等性能统计指标的统计。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令支持批量删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVSTATNAME | 业务统计名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务统计配置的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| PROTOCOLLEVEL | 协议等级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定被绑定的协议级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOLGROUP：协议组级别。<br>- PROTOCOL：协议级别。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOLGROUP”时为可选参数。<br>参数含义：该参数用于指定被绑定的协议组名称。数据源为系统支持识别的所有类型的协议分类，或者通过ADD PROTOCOLGROUP命令配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOL”时为可选参数。<br>参数含义：该参数用于指定被绑定的协议名称。数据源为系统支持识别的所有类型的协议、子协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [业务统计协议绑定配置（PROTBINDSRVS）](configobject/UDG/20.15.2/PROTBINDSRVS.md)

## 使用实例

- 运营商希望配置基于业务的性能统计组合，取消统计使用协议“p2p”的业务的性能统计项，不再统计其基于业务实例相关的性能统计指标：
  ```
  RMV PROTBINDSRVS:SRVSTATNAME="stat1",PROTOCOLLEVEL=PROTOCOLGROUP,PROTGROUPNAME="p2p";
  ```
- 运营商希望清空性能统计组合“stat1”中绑定的协议组，删除所有性能统计的协议组绑定：
  ```
  RMV PROTBINDSRVS:SRVSTATNAME="stat1",PROTOCOLLEVEL=PROTOCOLGROUP;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除业务统计协议绑定配置（RMV-PROTBINDSRVS）_82837389.md`
