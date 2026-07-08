---
id: UNC@20.15.2@MMLCommand@ADD PNFEXGROUPID
type: MMLCommand
name: ADD PNFEXGROUPID（增加对端NF的外部群组信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PNFEXGROUPID
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF扩展组管理
status: active
---

# ADD PNFEXGROUPID（增加对端NF的外部群组信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加本地配置的对端NF实例支持的外部群组标识的信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 注意事项

- 该命令执行后立即生效。

- 当前版本不支持此命令。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。不区分大小写。<br>默认值：无<br>配置原则：<br>建议本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致。 |
| EXGROUPID | 外部群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定外部组标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFEXGROUPID]] · 对端NF的外部群组信息（PNFEXGROUPID）

## 使用实例

增加对端NF的外部群组信息，对端NF实例标识为UDM_Instance_0上，支持外部群组标识为externalGroupId01。

```
ADD PNFEXGROUPID: NFINSTANCEID="UDM_Instance_0", EXGROUPID="externalGroupId01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加对端NF的外部群组信息（ADD-PNFEXGROUPID）_09652366.md`
