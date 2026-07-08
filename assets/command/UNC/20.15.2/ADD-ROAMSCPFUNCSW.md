---
id: UNC@20.15.2@MMLCommand@ADD ROAMSCPFUNCSW
type: MMLCommand
name: ADD ROAMSCPFUNCSW（增加漫游跨PLMN场景间接路由配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ROAMSCPFUNCSW
command_category: 配置类
applicable_nf:
- AMF
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 漫游通信模式管理
- 漫游间接路由管理
status: active
---

# ADD ROAMSCPFUNCSW（增加漫游跨PLMN场景间接路由配置）

## 功能

**适用NF：AMF、SMF**

该命令用于增加漫游跨PLMN场景间接路由配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入10条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNFTYPE | 本端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “AMF（AMF）”：NF类型为AMF<br>- “SMF（SMF）”：NF类型是SMF<br>默认值：无<br>配置原则：无 |
| PNFTYPE | 对端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “UDM（UDM）”：NF类型是UDM<br>- “AUSF（AUSF）”：NF类型为AUSF<br>- “AMF（AMF）”：NF类型为AMF<br>- “SMF（SMF）”：NF类型为SMF<br>- “EIR（5G-EIR）”：NF类型为5G-EIR<br>默认值：无<br>配置原则：无 |
| SCPDISCSW | 服务发现代理开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置漫游跨PLMN场景下是否使用SCP代理NF的服务发现功能，如果设置为ON，则漫游跨PLMN场景下指定的本端和对端类型之间的NF服务发现功能通过SCP间接实现。注意，不是通过直接和SCP进行服务发现交互，而是在业务消息交互的过程中，SCP解码业务消息获得用户号码等信息进行消息路由或抽取业务消息里携带的服务发现头到NRF进行服务发现。<br>数据来源：全网规划<br>取值范围：<br>- OFF（OFF）<br>- ON（ON）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMSCPFUNCSW]] · 漫游跨PLMN场景间接路由配置（ROAMSCPFUNCSW）

## 使用实例

运营商需要增加漫游跨PLMN场景下本端AMF与对端UDM的间接路由功能配置，允许本端AMF与对端UDM通过SCP ModeC的方式通信。

```
ADD ROAMSCPFUNCSW: LNFTYPE=AMF, PNFTYPE=UDM, SCPDISCSW=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ROAMSCPFUNCSW.md`
