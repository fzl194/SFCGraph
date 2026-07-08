---
id: UNC@20.15.2@MMLCommand@RMV ENBGPMEM
type: MMLCommand
name: RMV ENBGPMEM（删除eNodeB群组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ENBGPMEM
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- eNodeB管理
- eNodeB群组成员管理
status: active
---

# RMV ENBGPMEM（删除eNodeB群组成员）

## 功能

**适用网元：MME**

该命令用于删除eNodeB群组成员记录。

## 注意事项

- 此命令执行后立即生效。
- 此命令执行后起始eNodeB标识对应的一组记录都将被删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBGPID | eNodeB群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB群组标识。<br>数据来源：本端规划<br>取值范围：1～2048<br>默认值：无 |
| ENBTYPE | eNodeB类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB类型。<br>数据来源：整网规划<br>取值范围：<br>- “HOME_ENODEB(Home_eNodeB)”<br>- “MACRO_ENODEB(Macro_eNodeB)”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| BGNENBID | 起始eNodeB标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定起始eNodeB标识。<br>数据来源：整网规划<br>取值范围：0～268435455<br>默认值：无<br>说明：- 若参数“eNodeB类型”取值为“HOME_ENB(HOME_ENB)”，则该参数最大取值268435455。<br>- 若参数“eNodeB类型”取值为“MACRO_ENB(MACRO_ENB)”，则该参数最大取值1048575。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ENBGPMEM]] · eNodeB群组成员（ENBGPMEM）

## 使用实例

删除一个eNodeB群组，eNodeB群组标识为“1”，群组成员的eNodeB类型为“Macro_eNodeB”，移动国家码为“456”，移动网号为“12”，起始eNodeB标识为“1234”：

RMV ENBGPMEM: ENBGPID=1, ENBTYPE=MACRO_ENODEB, MCC="456", MNC="12", BGNENBID=1234;

RMV ENBGP: ENBGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ENBGPMEM.md`
