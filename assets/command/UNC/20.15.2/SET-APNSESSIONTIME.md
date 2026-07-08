---
id: UNC@20.15.2@MMLCommand@SET APNSESSIONTIME
type: MMLCommand
name: SET APNSESSIONTIME（设置APN会话上下文定时器配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNSESSIONTIME
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- APN定时器属性
status: active
---

# SET APNSESSIONTIME（设置APN会话上下文定时器配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置指定APN最大会话时长。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 该命令不适用于NB-IoT终端，因为此类终端很长时间才和网络交互一次，NB-IoT终端的空闲上下文功能参考软参BYTE801。
- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：SESSTIMESWITCH：DISABLE，SESSTIMELENGTH：1，DFTBEARERSW：DISABLE，DFTBEARERLEN：0。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| SESSTIMESWITCH | 会话时长开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置最大会话在线时长功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNSESSIONTIME查询当前参数配置值。<br>配置原则：<br>- 该功能对于Qchat用户不生效。<br>- 对于长时间在线的用户，为防止出现垃圾上下文和浪费无线侧资源可以配置该功能。 |
| SESSTIMELENGTH | 会话时长 | 可选必选说明：该参数在"SESSTIMESWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置最大会话在线时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNSESSIONTIME查询当前参数配置值。<br>配置原则：<br>- 二次激活的PDP继承一次激活PDP的时长。<br>- 当该激活的承载所配置的会话时长超时后，如果该承载为缺省承载，那么该用户会被去活；如果该承载为专有承载，去激活该专有承载。 |
| DFTBEARERSW | 缺省承载去激活时间间隔开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置专有承载去激活以后缺省承载去激活时间间隔开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNSESSIONTIME查询当前参数配置值。<br>配置原则：<br>此参数仅针对PGW和CGW形态生效。 |
| DFTBEARERLEN | 缺省承载去激活时间间隔 | 可选必选说明：该参数在"DFTBEARERSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置专有承载去激活以后缺省承载去激活时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNSESSIONTIME查询当前参数配置值。<br>配置原则：<br>此参数仅针对PGW和CGW形态生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNSESSIONTIME]] · APN会话上下文定时器配置（APNSESSIONTIME）

## 使用实例

设置APN为huawei.com的会话时长为120分钟

```
SET APNSESSIONTIME: APN="huawei.com", SESSTIMESWITCH=ENABLE, SESSTIMELENGTH=120;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置APN会话上下文定时器配置（SET-APNSESSIONTIME）_96243086.md`
