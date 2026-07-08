---
id: UNC@20.15.2@MMLCommand@RMV AREAGPMEM
type: MMLCommand
name: RMV AREAGPMEM（删除区域群成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AREAGPMEM
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
- 移动性管理
- 区域漫游限制管理
- 区域群成员管理
status: active
---

# RMV AREAGPMEM（删除区域群成员）

## 功能

**适用网元：SGSN、MME**

此命令用于删除区域群成员记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：待删除的区域群标识。<br>取值范围：1~50<br>默认值：无 |
| IDTYPE | 标识类型 | 可选必选说明：必选参数<br>参数含义：待删除的区域的标识类型。<br>取值范围：<br>- “LA(位置区)”：表示该区域标识类型为位置区。<br>- “RA(路由区)”：表示该区域标识类型为路由区。<br>- “TA(跟踪区)”：表示该区域标识类型为跟踪区。<br>默认值：无<br>说明：同一个<br>“AREAID”<br>下的<br>“IDTYPE”<br>必须相同。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：待删除的移动国家码。<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：待删除的移动网号。<br>取值范围：2~3位的十进制数字<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件必选参数<br>参数含义：待删除的位置区域码。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“LA(位置区)”<br>、<br>“RA(路由区)”<br>时生效。<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| LACRANGE | 位置区域码范围 | 可选必选说明：条件可选参数<br>参数含义：待删除的位置区域码范围。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“LA(位置区)”<br>时生效。<br>取值范围：0x0000~0xFFFF<br>默认值：无<br>说明：- 该参数的取值需要大于或等于“LAC”。<br>- 该参数与“LAC”参数构成一个LAC区段，会删除包含该LAC区段的记录。<br>- 如果不输入，表示配置单个LAC。 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：待删除的路由区域码。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“RA(路由区)”<br>时生效。<br>取值范围：0x00~0xFF<br>默认值：无 |
| RACRANGE | 路由区域码范围 | 可选必选说明：条件可选参数<br>参数含义：待删除的路由区域码范围。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“RA(路由区)”<br>时生效。<br>取值范围：0x00~0xFF<br>默认值：无<br>说明：- 该参数的取值需要大于或等于“RAC”。<br>- 该参数与“RAC”参数构成一个RAC区段，会删除包含该RAC区段的记录。<br>- 如果不输入，表示配置单个RAC。 |
| TAC | 跟踪区域码 | 可选必选说明：条件必选参数<br>参数含义：待删除的跟踪区域码。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“TA(跟踪区)”<br>时生效。<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| TACRANGE | 跟踪区域码范围 | 可选必选说明：条件可选参数<br>参数含义：待删除的跟踪区域码范围。<br>前提条件：该参数在<br>“IDTYPE(标识类型)”<br>设置为<br>“TA(跟踪区)”<br>时生效。<br>取值范围：0x0000~0xFFFF<br>默认值：无<br>说明：- 该参数的取值需要大于或等于“TAC”。<br>- 该参数与“TAC”参数构成一个TAC区段，会删除包含该TAC区段的记录。<br>- 如果不输入，表示配置单个TAC。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AREAGPMEM]] · 区域群成员（AREAGPMEM）

## 使用实例

删除一条区域群标识为1，标识类型为LA，移动国家码为111，移动网号为222，位置区域码为0x3333的区域群成员记录：

RMV AREAGPMEM: AREAID=1, IDTYPE=LA, MCC="111", MNC="222", LAC="0x3333";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-AREAGPMEM.md`
