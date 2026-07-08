---
id: UNC@20.15.2@MMLCommand@RMV RESULTCODECTRL
type: MMLCommand
name: RMV RESULTCODECTRL（删除返回码控制）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RESULTCODECTRL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 信令控制
- 返回码控制
status: active
---

# RMV RESULTCODECTRL（删除返回码控制）

## 功能

**适用NF：PGW-C、SMF**

![](删除返回码控制（RMV RESULTCODECTRL）_09897086.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果不输入接口类型或N7返回码，表示删除此PCC模板下的所有返回码。删除后使用该PCC模板的用户可能会因为无法命中返回码配置导致业务受损，请谨慎使用并联系华为支持协助操作。

此命令用来删除指定返回码的控制信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCTEMPLATE | PCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置该返回码所绑定的PCC模板。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| INTFTYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：接口类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- INTFTYPE_N7：N7接口类型。<br>- INTFTYPE_GX：Gx接口类型。<br>默认值：无<br>配置原则：无 |
| N7RESULTCODEVAL | N7返回码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTFTYPE”配置为“INTFTYPE_N7”时为可选参数。<br>参数含义：N7返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～3。300-599或者3xx-5xx，不区分大小写。其中xx代表一个范围，例如3xx代表300~399。<br>默认值：无<br>配置原则：<br>- 超时返回码504不受该配置控制，而是执行一次failover操作，若failover失败则根据APN/DNN绑定的PCCTEMPLATE或全局用户PCCFAILACTION相关配置获取失败动作。其中，APN/DNN绑定的PCCTEMPLATE配置优先级高。<br>- 配置的单个的返回码落在一个范围内时，单个的优先级高。 |
| VENDORID | 设备提供商标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTFTYPE”配置为“INTFTYPE_GX”时为可选参数。<br>参数含义：设备提供商标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |
| GXRESULTCODEVAL | Gx返回码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTFTYPE”配置为“INTFTYPE_GX”时为可选参数。<br>参数含义：返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～4。1000-9999，1xxx-9xxx，不区分大小写。其中xxxx代表一个范围，例如1xxx代表1000~1999。配置的单个的返回码落在一个范围内时，单个的优先级高。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESULTCODECTRL]] · 返回码控制（RESULTCODECTRL）

## 使用实例

删除所有全局RESULTCODECTRL返回码的控制信息：

```
RMV RESULTCODECTRL:PCCTEMPLATE="global";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除返回码控制（RMV-RESULTCODECTRL）_09897086.md`
