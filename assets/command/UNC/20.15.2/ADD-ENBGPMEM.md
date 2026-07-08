---
id: UNC@20.15.2@MMLCommand@ADD ENBGPMEM
type: MMLCommand
name: ADD ENBGPMEM（增加eNodeB群组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ENBGPMEM
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- eNodeB管理
- eNodeB群组成员管理
status: active
---

# ADD ENBGPMEM（增加eNodeB群组成员）

## 功能

**适用网元：MME**

此命令用于为 [**ADD ENBGP**](../eNodeB群组管理/增加eNodeB群组(ADD ENBGP)_26145606.md) 增加的eNodeB群组添加一条成员记录。

## 注意事项

- 此命令最大记录数为10000。
- 此命令执行后立即生效。
- 各个eNodeB群组下的eNodeB不能有重叠。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBGPID | eNodeB群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB群组标识。<br>前提条件：“eNodeB群组标识”已经通过<br>[**ADD ENBGP**](../eNodeB群组管理/增加eNodeB群组(ADD ENBGP)_26145606.md)<br>配置。<br>数据来源：本端规划<br>取值范围：1～2048<br>默认值：无 |
| ENBTYPE | eNodeB类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB类型。<br>数据来源：整网规划<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”<br>- “MACRO_ENODEB(Macro_eNodeB)”<br>默认值：MACRO_ENODEB(Macro_eNodeB) |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| BGNENBID | 起始eNodeB标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定起始eNodeB标识。<br>数据来源：整网规划<br>取值范围：0～268435455<br>默认值：无<br>说明：- 若参数“eNodeB类型”取值为“HOME_ENB(HOME_ENB)”，则该参数最大取值268435455。<br>- 若参数“eNodeB类型”取值为“MACRO_ENB(MACRO_ENB)”，则该参数最大取值1048575。 |
| ENDENBID | 终止eNodeB标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定终止eNodeB标识。<br>数据来源：整网规划<br>取值范围：0～268435455<br>默认值：无<br>说明：- 若参数“eNodeB类型”取值为“HOME_ENB(HOME_ENB)”，则该参数最大取值268435455。<br>- 若参数“eNodeB类型”取值为“MACRO_ENB(MACRO_ENB)”，则该参数最大取值1048575。<br>- 该参数与“起始eNodeB标识（BGNENBID）”参数构成一个eNodeB区段，方便维护人员配置连续的eNodeB标识。<br>- 如果不输入，表示配置单个eNodeB。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ENBGPMEM]] · eNodeB群组成员（ENBGPMEM）

## 使用实例

增加一个eNodeB群组，eNodeB群组标识为“1”，类型为“入口”，群组名称为“highspeed_usercheck_entry”，群组成员的eNodeB类型为“Macro_eNodeB”，移动国家码为“456”，移动网号为“12”，起始eNodeB标识为“1234”：

ADD ENBGP: ENBGPID=1, TYPE=ENTRY, ENBGPNAME="highspeed_usercheck_entry";

ADD ENBGPMEM: ENBGPID=1, ENBTYPE=MACRO_ENODEB, MCC="456", MNC="12", BGNENBID=1234;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ENBGPMEM.md`
