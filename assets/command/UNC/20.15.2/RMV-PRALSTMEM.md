---
id: UNC@20.15.2@MMLCommand@RMV PRALSTMEM
type: MMLCommand
name: RMV PRALSTMEM（删除PRA列表成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PRALSTMEM
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
- PRA区域管理
- PRA区域成员管理
status: active
---

# RMV PRALSTMEM（删除PRA列表成员）

## 功能

**适用网元：MME**

该命令用于从指定的PRA区域删除位置成员。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRAID | PRA标识 | 可选必选说明：必选参数<br>参数含义：该参数表示PRA区域的标识。<br>数据来源：整网规划<br>取值范围：0x800000～0xFFFFFF<br>默认值：无 |
| LOCIDTYPE | 位置区标识类型 | 可选必选说明：必选参数<br>参数含义：该参数表示PRA区域的位置成员的类型。<br>数据来源：整网规划<br>取值范围：<br>- “ALL(所有标识类型)”<br>- “TAI(跟踪区标识)”<br>- “MACRO_ENBID(宏基站标识)”<br>- “HOME_ENBID(家庭基站标识)”<br>- “ECGI(E-UTRAN小区全球标识)”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数表示组成PRA区域的位置成员的移动国家码。<br>前提条件：该参数在“位置区标识类型”参数配置后生效<br>数据来源：整网规划<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数表示组成PRA区域的位置成员的移动网号。<br>前提条件：该参数在“位置区标识类型”参数配置后生效<br>数据来源：整网规划<br>取值范围：2～3位十进制数字<br>默认值：无 |
| TACBEGIN | 跟踪区起始编码 | 可选必选说明：条件必选参数<br>参数含义：该参数表示PRA区域的跟踪区起始编码。<br>前提条件：该参数在“位置区标识类型”参数配置为“TAI(跟踪区标识)”后生效。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| ENBIDBEGIN | eNodeB起始标识 | 可选必选说明：条件必选参数<br>参数含义：该参数表示PRA区域的eNodeB起始标识。<br>前提条件：该参数在“位置区标识类型”参数配置为“MACRO_ENBID(宏基站标识)”或者“HOME_ENBID(家庭基站标识)”后生效。<br>数据来源：整网规划<br>取值范围：0～268435455<br>默认值：无<br>配置原则：<br>- 当“位置区标识类型”为“MACRO_ENBID(宏基站标识)”时，本参数的输入范围为0～1048575。<br>- 当“位置区标识类型”为“HOME_ENBID(家庭基站标识)”时，本参数的输入范围为0～268435455。 |
| ECIBEGIN | 小区起始标识 | 可选必选说明：条件必选参数<br>参数含义：该参数表示PRA区域的E-UTRAN小区起始标识。<br>前提条件：该参数在“位置区标识类型”参数配置为“ECGI(E-UTRAN小区全球标识)”后生效。<br>数据来源：整网规划<br>取值范围：0～268435455<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRALSTMEM]] · PRA列表成员（PRALSTMEM）

## 使用实例

删除PRA标识为“0x800001”的成员列表信息。

RMV PRALSTMEM: PRAID="0x800001", LOCIDTYPE=TAI, MCC="123", MNC="01", TACBEGIN="0x100";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PRALSTMEM.md`
