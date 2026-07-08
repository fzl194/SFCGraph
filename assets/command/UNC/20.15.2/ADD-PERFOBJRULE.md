---
id: UNC@20.15.2@MMLCommand@ADD PERFOBJRULE
type: MMLCommand
name: ADD PERFOBJRULE（增加性能对象规则）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD PERFOBJRULE（增加性能对象规则）

## 功能

**适用网元：SGSN、MME**

该命令用于特定性能统计对象规则的配置，当前仅支持TAI组对象规则的配置。

TAI组是将同一区域范围内的TAI组合在一起。当配置了TAI组规则后，属于该规则下的TAI，性能指标均会统计到该TAI组对象下。

## 注意事项

- 该命令执行后立即生效。
- 最大可配TAI组规则数为1500条。
- 每个TAI组可以有多个规则，但是同一个TAI只能包含在一个TAI组内。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：待增加规则的测量统计对象类型。<br>数据来源：本端规划<br>取值范围：<br>- “TAIGP(TAI组)”<br>默认值：无 |
| TAIGPN | TAI组名 | 可选必选说明：条件必选参数<br>参数含义：待增加规则的TAI组名称。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：无<br>配置原则：<br>- TAI组名可通过命令[**LST PERFOBJ**](../性能对象管理/查询性能对象信息(LST PERFOBJ)_26306000.md)查询。 |
| BGNTAI | 起始TAI | 可选必选说明：条件必选参数<br>参数含义：待增加TAI组规则所包含的TAI起始值。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：9～10位字符串<br>默认值：无<br>配置原则：<br>- TAI值首位不允许为‘0’。<br>- 输入的起始TAI值必须小于或者等于结束TAI值。<br>- 输入的起始TAI值和终止TAI值定义的TAI号段范围不允许与其它记录定义的TAI号段范围相互交叉、包含或重合。<br>说明：TAI由MCC、MNC和TAC组成。<br>- MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度。<br>- TAC编码为16进制数，固定为4位，不足前面补0。 |
| ENDTAI | 终止TAI | 可选必选说明：条件必选参数<br>参数含义：待增加TAI组规则所包含的TAI结束值。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>数据来源：本端规划<br>取值范围：9～10位字符串<br>默认值：无<br>配置原则：<br>- TAI值首位不允许为‘0’。<br>- 输入的终止TAI值必须大于或者等于起始TAI值。<br>- 输入的起始TAI值和终止TAI值定义的TAI号段范围不允许与其它记录定义的TAI号段范围相互交叉、包含或重合。<br>说明：TAI由MCC、MNC和TAC组成。<br>- MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度。<br>- TAC编码为16进制数，固定为4位，不足前面补0。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFOBJRULE]] · 性能对象规则（PERFOBJRULE）

## 使用实例

为TAI组名为“huawei”的TAI组对象增加TAI组规则，其TAI范围为308014101~308014103:

ADD PERFOBJRULE: MOC=TAIGP, TAIGPN="huawei", BGNTAI="308014101", ENDTAI="308014103";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PERFOBJRULE.md`
