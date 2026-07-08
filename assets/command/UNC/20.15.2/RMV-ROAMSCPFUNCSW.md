---
id: UNC@20.15.2@MMLCommand@RMV ROAMSCPFUNCSW
type: MMLCommand
name: RMV ROAMSCPFUNCSW（删除漫游跨PLMN场景间接路由配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV ROAMSCPFUNCSW（删除漫游跨PLMN场景间接路由配置）

## 功能

**适用NF：AMF、SMF**

该命令用于删除漫游跨PLMN场景间接路由配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNFTYPE | 本端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “AMF（AMF）”：NF类型为AMF<br>- “SMF（SMF）”：NF类型是SMF<br>默认值：无<br>配置原则：无 |
| PNFTYPE | 对端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “UDM（UDM）”：NF类型是UDM<br>- “AUSF（AUSF）”：NF类型为AUSF<br>- “AMF（AMF）”：NF类型为AMF<br>- “SMF（SMF）”：NF类型为SMF<br>- “EIR（5G-EIR）”：NF类型为5G-EIR<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMSCPFUNCSW]] · 漫游跨PLMN场景间接路由配置（ROAMSCPFUNCSW）

## 使用实例

运营商需要删除漫游跨PLMN场景下本端AMF与对端UDM之间的间接路由配置。

```
RMV ROAMSCPFUNCSW: LNFTYPE=AMF, PNFTYPE=UDM;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ROAMSCPFUNCSW.md`
