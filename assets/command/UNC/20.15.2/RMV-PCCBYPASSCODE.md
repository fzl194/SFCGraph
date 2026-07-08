---
id: UNC@20.15.2@MMLCommand@RMV PCCBYPASSCODE
type: MMLCommand
name: RMV PCCBYPASSCODE（删除PCC故障场景维持BYPASS状态码配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCCBYPASSCODE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 信令控制
- 返回码控制
status: active
---

# RMV PCCBYPASSCODE（删除PCC故障场景维持BYPASS状态码配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除PCRF/PCF Bypass故障状态码配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCTEMPLATE | PCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置该返回码所绑定的PCC模板。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>- 如果配置为“global”则表示全局配置。<br>- 如果配置为非“global”，则必须是已经通过ADD PCCTEMPLATE配置过的PCC模板名称。 |
| INTFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：接口类型。<br>数据来源：对端协商<br>取值范围：<br>- INTFTYPE_N7（N7接口类型）<br>- INTFTYPE_GX（Gx接口类型）<br>默认值：无<br>配置原则：无 |
| N7RESULTCODEVAL | N7返回码 | 可选必选说明：该参数在"INTFTYPE"配置为"INTFTYPE_N7"时为条件必选参数。<br>参数含义：N7返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~3。300-599或者3xx-5xx，不区分大小写。其中xx代表一个范围，例如3xx代表300~399。<br>默认值：无<br>配置原则：<br>配置的单个的返回码落在一个范围内时，单个的优先级高。 |
| GXRESULTCODEVAL | Gx返回码 | 可选必选说明：该参数在"INTFTYPE"配置为"INTFTYPE_GX"时为条件必选参数。<br>参数含义：Gx返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~4。1000-9999，1xxx-9xxx，不区分大小写。其中xxxx代表一个范围，例如1xxx代表1000~1999。配置的单个的返回码落在一个范围内时，单个的优先级高。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCBYPASSCODE]] · PCC故障场景维持BYPASS状态码配置（PCCBYPASSCODE）

## 使用实例

- 删除全局PCRF/PCF Bypass故障状态码配置，当非直连组网场景，UNC退出Bypass时发送探测消息后，Gx接口收到对端网元返回“GXRESULTCODEVAL”为“5012”的状态码时，退出Bypass状态：
  ```
  RMV PCCBYPASSCODE:PCCTEMPLATE="global",INTFTYPE=INTFTYPE_GX,GXRESULTCODEVAL="5012";
  ```
- 删除全局PCRF/PCF Bypass故障状态码配置，当非直连组网场景，UNC退出Bypass时发送探测消息后，N7接口收到对端网元返回“GXRESULTCODEVAL”为“5xx”的状态码时，退出Bypass状态：
  ```
  RMV PCCBYPASSCODE:PCCTEMPLATE="global",INTFTYPE=INTFTYPE_N7,N7RESULTCODEVAL="5xx";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除PCC故障场景维持BYPASS状态码配置（RMV-PCCBYPASSCODE）_18689757.md`
