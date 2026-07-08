---
id: UNC@20.15.2@MMLCommand@MOD SCCPNGT
type: MMLCommand
name: MOD SCCPNGT（修改SCCP新全局翻译码）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SCCPNGT
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP新全局翻译码
status: active
---

# MOD SCCPNGT（修改SCCP新全局翻译码）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来修改SCCP新全局码表指定记录的信息。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTX | 新GT码索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定新GT码对应的索引值。<br>数据来源：本端规划<br>取值范围：0~4095<br>默认值：无 |
| GTEXP | GT码表示语 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GT码表示语。<br>数据来源：整网规划<br>取值范围：<br>- “FOUR(ITU四类)”<br>- “SIX(ANSI二类)”<br>默认值：无 |
| ITUTT | ITU翻译类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定ITU模式的翻译类型。<br>前提条件：该参数在<br>“GT码表示语”<br>参数设置为<br>“FOUR(ITU四类)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：当运营商需要使用STP基于GT码的Translation Type再次进行分类路由转发时，配置此参数。 |
| TT | 翻译类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定翻译类型。<br>前提条件：该参数在<br>“GT码表示语”<br>参数设置为<br>“SIX(ANSI二类)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “ANSI9(ANSI 9类)”<br>- “ANSI10(ANSI 10类)”<br>默认值：无 |
| NP | 编号计划 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定编号计划。<br>前提条件：该参数在<br>“GT码表示语”<br>参数设置为<br>“FOUR(ITU四类)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “ISDNP(ISDN/电话编号计划)”<br>- “DATA(数据编号计划)”<br>- “TELEX(Telex编号计划)”<br>- “SMS(海事移动编号计划)”<br>- “PMS(陆地移动编号计划)”<br>- “ISDNMS(ISDN/移动编号计划)”<br>默认值：无 |
| ADDREXP | 地址性质表示语 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定地址性质表示语。<br>前提条件：该参数在<br>“GT码表示语”<br>参数设置为<br>“FOUR(ITU四类)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “FREE(空闲)”<br>- “SUBDN(用户号码)”<br>- “NSU(国内备用号码)”<br>- “NVU(国内有效号码)”<br>- “INTDN(国际号码)”<br>默认值：无 |
| ADDR | 地址信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址信息。<br>数据来源：整网规划<br>取值范围：长度不超过20的十进制数字字符串<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCCP新全局码表的记录名称。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPNGT]] · SCCP新全局翻译码（SCCPNGT）

## 使用实例

参考 [**ADD SCCPNGT**](增加SCCP新全局翻译码(ADD SCCPNGT)_26146328.md) 的场景1，修改 “新GT码索引” 为 “2” 和 “3” 的记录的 “ITU翻译类型” 为 “20” ：

MOD SCCPNGT: NGTX=2, GTEXP=FOUR, ITUTT=20;

MOD SCCPNGT: NGTX=3, GTEXP=FOUR, ITUTT=20;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SCCPNGT.md`
