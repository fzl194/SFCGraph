---
id: UNC@20.15.2@MMLCommand@RMV TAGPMEM
type: MMLCommand
name: RMV TAGPMEM（删除TA群组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TAGPMEM
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
- 跟踪区管理
- 跟踪区群组成员管理
status: active
---

# RMV TAGPMEM（删除TA群组成员）

## 功能

**适用网元：MME**

该命令用于删除跟踪区群组成员记录。

## 注意事项

- 此命令执行后立即生效。
- 删除某个跟踪区群组标识的最后一组记录时，必须保证相关表中不存在该TA群组成员对应跟踪区群组的相关记录。可执行[**LST S1SUBRRLST**](../../区域漫游限制管理/S1模式用户漫游限制管理/查询S1模式用户漫游限制列表(LST S1SUBRRLST)_72345157.md)查看相关表的记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAGPID | 跟踪区群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>数据来源：本端规划<br>取值范围：1~2048<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TAGPMEM]] · TA群组成员（TAGPMEM）

## 使用实例

删除一个TA群组，跟踪区群组标识为1，群组成员的移动国家码为456，移动网号为12，跟踪区域码为0x1234：

RMV TAGPMEM: TAGPID=1, MCC="456", MNC="12", TAC="0x1234";

RMV TAGP: TAGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-TAGPMEM.md`
