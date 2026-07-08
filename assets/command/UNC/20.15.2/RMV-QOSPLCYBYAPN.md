---
id: UNC@20.15.2@MMLCommand@RMV QOSPLCYBYAPN
type: MMLCommand
name: RMV QOSPLCYBYAPN（删除基于APN的QoS策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSPLCYBYAPN
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- QoS限制配置
- 基于APN的QOS策略
status: active
---

# RMV QOSPLCYBYAPN（删除基于APN的QoS策略）

## 功能

**适用网元：MME**

该命令用于删除一条或多条基于APN的QoS策略配置。

## 注意事项

该命令执行后对于新接入的EPS承载立即生效。如果当前用户已经激活了EPS承载，该命令的限制会在用户下一次会话管理业务流程中生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPE | RAT类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的接入类型，系统优先匹配与当前用户所处网络类型相同的配置数据，当相同RAT类型配置中不包含该用户时，再进行<br>“ALL”<br>类型的匹配。<br>数据来源：整网规划<br>取值范围：<br>- “ALL(ALL)”<br>- “GERAN(GERAN)”<br>- “UTRAN(UTRAN)”<br>- “E-UTRAN(E-UTRAN)”<br>- “NB-IoT(NB-IoT)”<br>默认值：无 |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定基于APN的QoS策略配置的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX(指定IMSI前缀)”：指网络中与指定的IMSI前缀匹配的用户。<br>- “HOME_USER(本网用户)”：指网络中的本网签约用户。<br>- “FOREIGN_USER(外网用户)”：指网络中的漫游用户。<br>- “ALL_USER(所有用户)”：指网络中的所有用户。<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>该参数必须先由<br>[**ADD QOSPLCYBYAPN**](增加基于APN的QoS策略(ADD QOSPLCYBYAPN)_88832402.md)<br>命令定义，才能在此处引用。<br>对于外网用户，该参数用于指定与互联PLMN签订漫游协议的本局运营商标识，对于本网用户，该参数是本网用户对应的运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定进行匹配的IMSI前缀。系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>该参数必须先由<br>[**ADD QOSPLCYBYAPN**](增加基于APN的QoS策略(ADD QOSPLCYBYAPN)_88832402.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>前提条件：该参数必须先由<br>[**ADD QOSPLCYBYAPN**](增加基于APN的QoS策略(ADD QOSPLCYBYAPN)_88832402.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSPLCYBYAPN]] · 基于APN的QoS策略（QOSPLCYBYAPN）

## 使用实例

删除 “RAT类型” 为 “E-UTRAN” ， “用户范围” 为 “IMSI_PREFIX” ， “IMSI前缀” 为 “3080107000” ， “APNNI” 为 “HUAWEI1.COM” 的基于APN的QoS策略配置。

```
RMV QOSPLCYBYAPN: RATTYPE=E-UTRAN, SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000", APNNI="HUAWEI1.COM";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-QOSPLCYBYAPN.md`
