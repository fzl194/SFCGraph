---
id: UNC@20.15.2@MMLCommand@SWP RUGROUP
type: MMLCommand
name: SWP RUGROUP（资源单元组主备倒换）
nf: UNC
version: 20.15.2
verb: SWP
object_keyword: RUGROUP
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 倒换主备资源单元
status: active
---

# SWP RUGROUP（资源单元组主备倒换）

## 功能

![](资源单元组主备倒换（SWP RUGROUP）_59104272.assets/notice_3.0-zh-cn_2.png)

本命令为高危命令，用于执行资源单元组的主备倒换，可能使得操作资源单元组承载的业务受影响，请谨慎使用并联系华为技术支持协助操作。

该命令用于执行资源单元组的主备倒换。

## 注意事项

- 该操作可能使得操作资源单元组承载的业务受影响。
- 该命令执行后立即生效。
- 该命令只能在HA模式下使用，非HA模式不支持倒换。可以通过[**DSP RUGROUP**](显示资源单元组成员信息（DSP RUGROUP）_59103970.md)命令查询倒换状态是否为就绪。
- 执行本命令后，可以使用[**DSP RUGROUP**](显示资源单元组成员信息（DSP RUGROUP）_59103970.md)命令查询资源单元组主备状态，对照倒换前的资源单元组主备状态，以确定倒换是否成功。
- 该命令操作不当，可能引起资源单元组承载的业务受影响。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | RU组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示资源单元组名称。可使用<br>[**DSP RUGROUP**](显示资源单元组成员信息（DSP RUGROUP）_59103970.md)<br>命令查询对应的资源单元组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [资源单元组成员信息（RUGROUP）](configobject/UNC/20.15.2/RUGROUP.md)

## 使用实例

BG_IPCTRL为资源单元组名称，现在要执行该资源单元组的主备倒换操作：

```
SWP RUGROUP: GROUPNAME="BG_IPCTRL"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/资源单元组主备倒换（SWP-RUGROUP）_59104272.md`
