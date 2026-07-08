---
id: UNC@20.15.2@MMLCommand@ADD TAGPMEM
type: MMLCommand
name: ADD TAGPMEM（增加TA群组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TAGPMEM
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
- 跟踪区管理
- 跟踪区群组成员管理
status: active
---

# ADD TAGPMEM（增加TA群组成员）

## 功能

**适用网元：MME**

此命令用于为 [**ADD TAGP**](../跟踪区群组管理/增加TA群组(ADD TAGP)_26145580.md) 增加的跟踪区群组添加一条成员记录。

## 注意事项

- 此命令最大记录数为10000。
- 此命令执行后立即生效。
- 不同的跟踪区群组相互独立，同一个跟踪区群组下的各跟踪区域不能有重叠。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAGPID | 跟踪区群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>前提条件：<br>“跟踪区群组标识”<br>已经通过<br>[**ADD TAGP**](../跟踪区群组管理/增加TA群组(ADD TAGP)_26145580.md)<br>配置。<br>数据来源：本端规划<br>取值范围：1~2048<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| TACRANGE | 跟踪区域码范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区域码范围。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：该参数的取值需要大于或等于<br>“TAC（跟踪区域码）”<br>。<br>说明：- 该参数与“TAC（跟踪区域码）”参数构成一个TAC区段，方便维护人员配置连续的跟踪区域。<br>- 如果不输入，表示配置单个TAC。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TAGPMEM]] · TA群组成员（TAGPMEM）

## 使用实例

增加一个TA群组，跟踪区群组标识为1，其群组名称为“shanghai”，群组成员的移动国家码为456，移动网号为12，跟踪区域码为0x1234：

ADD TAGP: TAGPID=1, TANAME="shanghai";

ADD TAGPMEM: TAGPID=1, MCC="456", MNC="12", TAC="0x1234";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TAGPMEM.md`
