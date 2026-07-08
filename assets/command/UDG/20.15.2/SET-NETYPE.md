---
id: UDG@20.15.2@MMLCommand@SET NETYPE
type: MMLCommand
name: SET NETYPE（设置 NE 类型）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NETYPE
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- DN管理
- NE信息管理
- NE类型管理
status: active
---

# SET NETYPE（设置 NE 类型）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

本命令用于改变网元形态。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 网元形态初始值由系统生成,该命令参数初始值为NULL。
- SET NETYPE的ProxySGWU仅限于设备作为独立关口局设备，承接国际漫游语音业务的ProxySGW形态时配置。其他场景不能配置为ProxySGWU。
- SET NETYPE的PorxyUPF仅限于设备作为独立关口局设备，承接国际漫游语音业务的PorxyUPF形态时配置。其他场景不能配置为PorxyUPF。
- SET NETYPE目前支持的形态设置值如下表：

| 逻辑类型 | 排查方法指导 | 配置结果确认 |
| --- | --- | --- |
| UPF | DSP NEINFO | 网元配置类型值为UPF(纯5G) |
| ProxySGWU | DSP NEINFO | 网元配置类型值为ProxySGWU |
| UPF;PGWU | DSP NEINFO | 网元配置类型值为UPF;PGWU(45G融合) |
| UPF;SGWU | DSP NEINFO | 网元配置类型值为UPF;SGWU(45G融合) |
| UPF;SGWU;PGWU | DSP NEINFO | 网元配置类型值为UPF;SGWU;PGWU(45G融合) |
| UPF;SGWU;PGWU;GGSNU | DSP NEINFO | 网元配置类型值为UPF;SGWU;PGWU;GGSNU(245G融合) |
| UPF;PGWU;GGSNU | DSP NEINFO | 网元配置类型值为UPF;PGWU;GGSNU(245G融合) |
| ProxySGWU;ProxyUPF;PGWU | DSP NEINFO | 网元配置类型值为ProxySGWU;ProxyUPF;PGWU |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NETYPEENUM | 网元形态 | 可选必选说明：必选参数<br>参数含义：网元形态枚举。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- SGWU<br>- PGWU<br>- UPF<br>- GGSNU<br>- ProxySGWU<br>- ProxyUPF<br>- UEGTypeL<br>- UEGTypeM<br>- AMF<br>- SMF<br>- UDM<br>- PCF<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ NeType默认值（NETYPE）](configobject/UDG/20.15.2/NETYPE.md)

## 关联任务

- [0-00280](task/UDG/20.15.2/0-00280.md)

## 使用实例

将网元形态设置为UPF;PGWU：

```
SET NETYPE:NETYPEENUM=GGSNU-0&PGWU-1&ProxySGWU-0&SGWU-0&UPF-1&ProxyUPF-0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置-NE-类型（SET-NETYPE）_84967916.md`
