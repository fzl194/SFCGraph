---
id: UNC@20.15.2@MMLCommand@MOD PERFOBJRULE
type: MMLCommand
name: MOD PERFOBJRULE（修改性能对象规则）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PERFOBJRULE
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
- 性能对象规则管理
status: active
---

# MOD PERFOBJRULE（修改性能对象规则）

## 功能

**适用网元：SGSN、MME**

该命令用于修改指定性能统计对象的统计规则。当前只支持TAI组对象。

## 注意事项

- 该命令执行后立即生效。
- 每个TAI组可以有多个规则，但是同一个TAI只能包含在一个TAI组内。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：待修改规则的测量统计对象类型。<br>数据来源：本端规划<br>取值范围：<br>- “TAIGP(TAI组)”<br>默认值：无 |
| TAIGPRULEIDX | TAI组规则索引 | 可选必选说明：条件必选参数<br>参数含义：待修改的TAI组规则索引。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>取值范围：1~1500<br>默认值：无<br>配置原则：TAI组规则索引通过<br>[**LST PERFOBJRULE**](查询性能对象规则(LST PERFOBJRULE)_26146196.md)<br>命令查询。 |
| TAIGPN | TAI组名 | 可选必选说明：条件可选参数<br>参数含义：待修改TAI组规则的TAI组名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：无<br>配置原则：<br>- 如果需要将该规则从一个TAI组划分到另外一个TAI组，可通过本命令修改。<br>- TAI组名可通过命令[**LST PERFOBJ**](../性能对象管理/查询性能对象信息(LST PERFOBJ)_26306000.md)查询。<br>说明：若修改TAI组规则对应的TAI组，会导致该规则修改前后涉及的TAI组对象，在修改时间点所属周期统计值不准确 |
| BGNTAI | 起始TAI | 可选必选说明：条件可选参数<br>参数含义：待修改TAI组规则所包含的TAI起始值。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：9～10位字符串<br>默认值：无<br>配置原则：<br>- TAI值首位不允许为‘0’。<br>- 输入的起始TAI值必须小于或者等于结束TAI值。<br>- 输入的起始TAI值和终止TAI值定义的TAI号段范围不允许与其它记录定义的TAI号段范围相互交叉、包含或重合。<br>说明：- TAI由MCC、MNC和TAC组成。MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度；TAC编码为16进制数，固定为4位，不足前面补0。<br>- 若修改TAI组规则的起始TAI，会导致修改时间点所属周期内该TAI组对象统计值出现波动。 |
| ENDTAI | 终止TAI | 可选必选说明：条件可选参数<br>参数含义：待修改TAI组规则所包含的TAI结束值。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：9～10位字符串<br>默认值：无<br>配置原则：<br>- TAI值首位不允许为‘0’。<br>- 输入的终止TAI值必须大于或者等于起始TAI值。<br>- 输入的起始TAI值和终止TAI值定义的TAI号段范围不允许与其它记录定义的TAI号段范围相互交叉、包含或重合。<br>说明：- TAI由MCC、MNC和TAC组成。MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度；TAC编码为16进制数，固定为4位，不足前面补0。<br>- 若修改TAI组规则的终止TAI，会导致修改时间点所属周期内该TAI组对象统计值出现波动。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFOBJRULE]] · 性能对象规则（PERFOBJRULE）

## 使用实例

将索引为1的TAI组规则划分到组名为“huawei”的TAI组，且将包含的TAI范围修改为308014101~308014103:

MOD PERFOBJRULE: MOC=TAIGP, TAIGPRULEIDX=1, TAIGPN="huawei", BGNTAI="308014101", ENDTAI="308014103";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PERFOBJRULE.md`
