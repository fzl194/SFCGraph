---
id: UNC@20.15.2@MMLCommand@ADD PERFOBJ
type: MMLCommand
name: ADD PERFOBJ（增加性能对象信息）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD PERFOBJ（增加性能对象信息）

## 功能

**适用网元：SGSN、MME**

该命令用于需要手工设置性能统计对象的配置。

当需要创建APN对象、TAI组对象或者HSS主机名对象时，执行此命令。

## 注意事项

- 该命令执行后立即生效。
- 不同的性能统计对象，支持的配置对象数存在差异，具体请参考对象对应的参数描述。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：测量对象类型。<br>数据来源：本端规划<br>取值范围：<br>- “APN(APN)”<br>- “TAIGP(TAI组)”<br>- “HSSHOSTNAME(HSS主机名)”<br>默认值：无 |
| NAME | 对象名称 | 可选必选说明：条件必选参数<br>参数含义：APN测量对象名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“APN(APN)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1~63位字符串<br>默认值：无<br>配置原则：<br>- 本参数需要配置APN对象所对应的APNNI信息。建立APN对象与索引之间的对应关系，以便在网管上添加APN对象进行性能统计。<br>- APN对象表最大记录数为1000。<br>说明：只能输入大小写字母、“.”、“-”、0~9的整数。 |
| TAIGPN | TAI组名 | 可选必选说明：条件必选参数<br>参数含义：TAI组测量对象名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：无<br>配置原则：<br>- 本参数用于配置需要进行统计的TAI组对象的名称。TAI组表最大记录数为1500。<br>- 请根据TAI组的范围设置明确的TAI组名称，不建议使用TAI值作为手动TAI组的名称。<br>- TAI组名不区分大小写，且不允许重复。<br>- 新添加**手动配置TAI组**的**TAI组名**请勿使用已存在的**自动配置TAI组**的**TAI组名**。<br>- 增加TAI组后，需要为此TAI组增加TAI组的规则，相关命令参考[**ADD PERFOBJRULE**](../性能对象规则管理/增加性能对象规则(ADD PERFOBJRULE)_72225873.md)，如果不为此TAI组配置任何TAI组规则，则此TAI组对象将无法进行性能统计。<br>- 简化对TAI性能对象的操作维护，及时获取TAI性能对象的变更场景下，可以使用TAI组对象的配置。<br>说明：- 系统开工时，缺省为每一个当前存在的TAI创建一个TAI组进行性能统计测量，规格为1500个，此TAI组命名为自动统计的TAI组对象。当系统中的TAI个数超出1500个后，多余的对象无法进行性能统计。可通过[**ADD PERFOBJ**](增加性能对象信息(ADD PERFOBJ)_26305998.md)以及[**ADD PERFOBJRULE**](../性能对象规则管理/增加性能对象规则(ADD PERFOBJRULE)_72225873.md)命令配置TAI组，将多个TAI划分到同一个TAI组中，以TAI组的粒度进行统计。<br>- 每个TAI只能加到一个TAI组进行测量，当新增TAI组规则后，符合该组规则的自动统计的TAI对象将会删除，不再作为单独的TAI组对象进行统计。<br>- TAI组对象作为北向网管的MOC对象导出，缺省情况下，TAI组对象名即为TAI。对于需要通过北向网管对接的局点，需要注意手工配置TAI组后，TAI组名是否能被北向网管正确解析。若北向网管不能解析TAI组对象，请谨慎配置此参数。 |
| HSSNAME | HSS对象名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定HSS对象名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“HSSHOSTNAME(HSS主机名)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母和数字。<br>- 不区分大小写，且不允许重复。<br>- HSS对象表最大记录数为64。 |
| HSSRULE | HSS主机名匹配规则 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定HSS主机名匹配规则。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“HSSHOSTNAME(HSS主机名)”<br>时，才需要配置。<br>数据来源：全网规划<br>取值范围：1~127位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“*”，“.”和“-”，比如“*.EPC.MNC123.MCC456.3GPPNETWORK.ORG”。<br>- “*”号表示1个或多个的连续的字母或者数字。<br>- “*”号的前后不能是字母、数字或者“*”，只能是“.”或者“-”。匹配规则可以以“*”开头或结尾。<br>- 不区分大小写。<br>说明：- 系统根据该参数对用户的HSS主机名进行匹配，如果HSS主机名满足匹配规则，则会在HSS对象对应的性能指标上进行统计。<br>- 用户的HSS主机名必须由字母，数字，“.”和“-”组成，不能包含其他字符。<br>- 匹配规则“*.EPC.MNC123.MCC456.3GPPNETWORK.ORG”可以匹配成功的HSS主机名举例如下：“HUAWEI.EPC.MNC123.MCC456.3GPPNETWORK.ORG”、“HUAWEI001.EPC.MNC123.MCC456.3GPPNETWORK.ORG”等。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFOBJ]] · 性能对象信息（PERFOBJ）

## 使用实例

- 为APN的一个对象huawei.com增加索引:
  ADD PERFOBJ: MOC=APN, NAME="huawei.com";
- 添加一个组名为huawei的TAI组对象，此TAI组包含的TAI范围为308014101~308014103：
  ADD PERFOBJ: MOC=TAIGP, TAIGPN="huawei";
  ADD PERFOBJRULE: MOC=TAIGP, TAIGPN="huawei", BGNTAI="308014101", ENDTAI="308014103";
- 添加一个名称为LOCAL的HSS对象，其中匹配规则为*.EPC.MNC123.MCC456.3GPPNETWORK.ORG:
  ADD PERFOBJ: MOC=HSSHOSTNAME, HSSNAME="LOCAL", HSSRULE="*.EPC.MNC123.MCC456.3GPPNETWORK.ORG";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PERFOBJ.md`
