---
id: UDG@20.15.2@MMLCommand@ADD UPDIAMCONNGRP
type: MMLCommand
name: ADD UPDIAMCONNGRP（增加Diameter链路组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPDIAMCONNGRP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 用户面服务管理
- Diameter管理
- Diameter连接
- Diameter链路组
status: active
---

# ADD UPDIAMCONNGRP（增加Diameter链路组）

## 功能

**适用NF：UPF**

该命令用于指定本端主机名与指定对端服务器之间建立一组Diameter链路。本端主机名，对端主机名唯一确定了一组Diameter链路。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 配置LOCALHOSTNAME需要保证已经配置了Local Info。
- 配置PEERHOSTNAME时，需要保证已经配置了与APPLICATION对应类型的服务器。
- APPLICATION和对端主机名的应用类型必须一致。
- PEERHOSTNAME和LOCALHOSTNAME不能重复。
- 每个Peer与Swm应用最多绑定16个Local Host。
- 配置SELECTMODE为MASTER_SLAVE时，删除Diameter链路组下配置的第一个Diameter链路或删除主链路的对端地址信息会导致主备链路切换，准确的主备关系未知。当前不支持用命令设置主链路，如果需要明确指定主链路，请删除并重新配置Diameter链路组下的Diameter链路，配置的第一个Diameter链路即对应主链路。
- 配置SELECTMODE为SESSION_ID时，根据session-id选择Diameter链路状态异常时，会选择其他可用Diameter链路进行消息交互。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONNGROUPNAME | Diameter链路组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCALHOSTNAME | 本端主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路组的本端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMLOCINFO命令配置生成。 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路组的应用类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |
| PEERHOSTNAME | 对端主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路组的对端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMETERAAA或ADD UPDRA命令配置生成。 |
| SELECTMODE | 链路选择模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的链路选择模式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SESSION_ID：基于会话（Session-id）轮询方式进行链路选择。<br>- MASTER_SLAVE：基于主备方式进行链路选择。<br>- ROUND_ROBIN：基于消息轮询方式进行链路选择。<br>默认值：SESSION_ID<br>配置原则：无 |

## 操作的配置对象

- [Diameter链路组（UPDIAMCONNGRP）](configobject/UDG/20.15.2/UPDIAMCONNGRP.md)

## 使用实例

如果希望为本端主机swmlocalhost和对端dra主机drahost创建一个swm diameter链路组，可以使用该命令配置链路组：

```
ADD UPDIAMCONNGRP: CONNGROUPNAME="swmconngrp", LOCALHOSTNAME="swmlocalhost", APPLICATION=SWM, PEERHOSTNAME="drahost", SELECTMODE=SESSION_ID;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加Diameter链路组（ADD-UPDIAMCONNGRP）_97314555.md`
