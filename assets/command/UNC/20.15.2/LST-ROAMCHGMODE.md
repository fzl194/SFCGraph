---
id: UNC@20.15.2@MMLCommand@LST ROAMCHGMODE
type: MMLCommand
name: LST ROAMCHGMODE（查询基于漫游属性的计费接口选择方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ROAMCHGMODE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 漫游属性计费模式
status: active
---

# LST ROAMCHGMODE（查询基于漫游属性的计费接口选择方式）

## 功能

**适用NF：PGW-C、SMF、GGSN、SGW-C**

该命令用于查询不同DNN、不同漫游属性、不同类型终端接入不同网络时所选择的计费接口。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMACCTYPE | 指定终端和接入类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定终端和接入类型。<br>数据来源：本端规划<br>取值范围：<br>- “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活流程中，激活消息的PCO中携带5G PDU session ID信息。<br>- “UE5G_RAT5G（5G终端5G接入）”：5G终端5G接入是指在5G接入的PDU激活流程。<br>- “UENON5G_RAT4G（非5G终端4G接入）”：非5G终端4G接入是指在4G接入的PDN激活流程。<br>- “RAT2G（2G接入）”：2G接入是指在2G接入的一次PDP激活流程。<br>- “RATNBIOT（NB-IoT接入）”：NB-IoT接入是指NB-IoT用户接入。<br>- “NON_3GPP（非3GPP接入）”：非3GPP接入是指用户从非3GPP网络接入。<br>- “RATLTEM（LTE-M接入）”：LTE-M接入是指LTE-M用户接入。<br>- “RAT3G（3G接入）”：3G接入是指在3G接入的PDP一次激活流程。<br>默认值：无<br>配置原则：无 |
| ROAMINGTYPE | 漫游属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户漫游属性。<br>数据来源：本端规划<br>取值范围：<br>- ROAMING（漫游用户）<br>- VISITING（拜访用户）<br>- HOME（本地用户）<br>默认值：无<br>配置原则：无 |
| CTRLTYPE | 控制类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费接口选择的类型。<br>数据来源：全网规划<br>取值范围：<br>- APN_LEVEL（APN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"CTRLTYPE"配置为"APN_LEVEL"时为条件可选参数。<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMCHGMODE]] · 基于漫游属性的计费接口选择方式（ROAMCHGMODE）

## 使用实例

查询所有基于漫游属性的计费接口选择方式，执行如下命令：

```
%%LST ROAMCHGMODE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
指定终端和接入类型  控制类型     APN名称   漫游属性    按5GS互操作指示选择计费接口  指定的计费接口  作为SGW计费模式  作为V-SMF计费模式  按5GC无限制接入标识选择计费接口

5G终端4G接入        整系统级别   null      漫游用户    False                        GaGy模式        GaGy模式         Nchf模式           False
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ROAMCHGMODE.md`
