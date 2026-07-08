---
id: UNC@20.15.2@MMLCommand@MOD PERFOBJ
type: MMLCommand
name: MOD PERFOBJ（修改性能对象信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PERFOBJ
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能对象管理
status: active
---

# MOD PERFOBJ（修改性能对象信息）

## 功能

**适用网元：SGSN、MME**

本命令用于修改指定的性能统计对象信息。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：测量对象类型。<br>数据来源：本端规划<br>取值范围：<br>- “TAIGP(TAI组)”<br>- “HSSHOSTNAME(HSS主机名)”<br>默认值：无 |
| TAIGPIDX | TAI组索引 | 可选必选说明：条件必选参数<br>参数含义：待修改的TAI组对应的索引。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1~1500<br>默认值：无<br>说明：可通过<br>[**LST PERFOBJ**](查询性能对象信息(LST PERFOBJ)_26306000.md)<br>命令查询对应TAI组的索引。 |
| TAIGPN | TAI组名 | 可选必选说明：条件必选参数<br>参数含义：待修改的TAI组索引对应的TAI组对外呈现的性能统计名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：无<br>配置原则：<br>- 请根据TAI组的范围设置明确的TAI组名称，不建议使用TAI值作为手动TAI组的名称。<br>- TAI组名不区分大小写，且不允许重复。<br>- 请勿将**手动配置TAI组**的**TAI组名**修改为已存在的**自动配置TAI组**的**TAI组名**。<br>说明：- 修改TAI组的组名，对应该TAI组的规则不会被修改。 |
| HSSNAMEINDEX | HSS对象名称索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待删除的HSS对象名称索引。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“HSSHOSTNAME(HSS主机名)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1~64<br>默认值：无<br>说明：- 可通过<br>[**LST PERFOBJ**](查询性能对象信息(LST PERFOBJ)_26306000.md)<br>命令查询对应的HSS对象名称索引。 |
| HSSRULE | HSS主机名匹配规则 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待修改的HSS主机名匹配规则。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“HSSHOSTNAME(HSS主机名)”<br>时，才需要配置。<br>数据来源：全网规划<br>取值范围：1~127位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“*”，“.”和“-”，比如“*.EPC.MNC123.MCC456.3GPPNETWORK.ORG”。<br>- “*”号表示1个或多个的连续的字母或者数字。<br>- “*”号的前后不能是字母、数字或者“*”，只能是“.”或者“-”。匹配规则可以以“*”开头或结尾。<br>- 不区分大小写。<br>说明：- 此参数会与用户的HSS主机名进行匹配比较，如果匹配成功，则会在对应的HSS对象上进行指标统计。<br>- 用户的HSS主机名必须由字母，数字，“.”和“-”组成，不能包含其他字符。<br>- 匹配规则“*.EPC.MNC123.MCC456.3GPPNETWORK.ORG”可以匹配成功的HSS主机名举例如下：“HUAWEI.EPC.MNC123.MCC456.3GPPNETWORK.ORG”、“HUAWEI001.EPC.MNC123.MCC456.3GPPNETWORK.ORG”等。 |

## 操作的配置对象

- [性能对象信息（PERFOBJ）](configobject/UNC/20.15.2/PERFOBJ.md)

## 使用实例

- 将索引为1的TAI组名称修改为"huawei":
  MOD PERFOBJ: MOC=TAIGP, TAIGPIDX=1, TAIGPN="huawei";
- 将索引为1的HSS对象的匹配规则修改为"*.EPC.MNC123.MCC456.3GPPNETWORK.ORG":
  MOD PERFOBJ: MOC=HSSHOSTNAME, HSSNAMEINDEX=1, HSSRULE="*.EPC.MNC123.MCC456.3GPPNETWORK.ORG";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改性能对象信息(MOD-PERFOBJ)_26146188.md`
