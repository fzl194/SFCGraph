---
id: UNC@20.15.2@MMLCommand@OPR FESVERIFICATION
type: MMLCommand
name: OPR FESVERIFICATION（触发FES对账）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: FESVERIFICATION
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎服务
- 设置FES对账
status: active
---

# OPR FESVERIFICATION（触发FES对账）

## 功能

该命令用于手工触发FES对账。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UCORMC | 对账模式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对账模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SLOW：慢对账。<br>- FAST_UC：单播快对账。<br>- FAST_MC：多播快对账。<br>默认值：无 |
| SLOWVRFCTYPE | 慢对账类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UCORMC”配置为“SLOW”时为可选参数。<br>参数含义：该参数用于慢对账类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：全对账。<br>- IP：IP信息对账。<br>- MPLS：MPLS信息对账。<br>- MC：组播信息对账。<br>默认值：ALL |
| FASTVRFCUCTYPE | 单播快对账类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“UCORMC”配置为“FAST_UC”时为必选参数。<br>参数含义：该参数用于表示单播快对账类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IP：IP信息对账。<br>- MPLS：MPLS信息对账。<br>- MC：组播信息对账。<br>默认值：无 |
| FASTVRFCMCTYPE | 多播快对账类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“UCORMC”配置为“FAST_MC”时为必选参数。<br>参数含义：该参数用于表示多播快对账类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RM：路由管理信息对账。<br>- MBFES：资源单元FES对账。<br>默认值：无 |
| IDENTITYFLAGUC | 单播快对账标志位 | 可选必选说明：条件可选参数<br>前提条件：该参数在“FASTVRFCUCTYPE”配置为“IP”、“MPLS” 或 “MC”时为可选参数。<br>参数含义：该参数用于表示单播快对账标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- COMPONENTID：组件ID。<br>- RUNAME：资源单元名称。<br>默认值：无<br>配置原则：如果不输入该参数，则表示触发与指定单播快对账类型相关的所有组件的对账。 |
| IDENTITYFLAGMC | 多播快对账标志位 | 可选必选说明：条件必选参数<br>前提条件：该参数在“FASTVRFCMCTYPE”配置为“RM” 或 “MBFES”时为必选参数。<br>参数含义：该参数用于表示多播快对账标志位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALLSLOT：所有资源单元。<br>- RUNAME：资源单元名称。<br>默认值：无 |
| COMPONENTID | 组件ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAGUC”配置为“COMPONENTID”时为必选参数。<br>参数含义：该参数用于表示组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAGUC”配置为“RUNAME”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“IDENTITYFLAGMC”配置为“RUNAME”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“UCORMC”配置为“SLOW”时为可选参数。<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：区分大小写，不支持空格，下发本MML命令前可使用DSP RU查看资源单元信息。 |

## 操作的配置对象

- [FES对账信息（FESVERIFICATION）](configobject/UNC/20.15.2/FESVERIFICATION.md)

## 使用实例

手工触发单播快对账：

```
OPR FESVERIFICATION: UCORMC=FAST_UC, FASTVRFCUCTYPE=MC;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/触发FES对账（OPR-FESVERIFICATION）_00440341.md`
