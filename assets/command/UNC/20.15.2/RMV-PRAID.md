---
id: UNC@20.15.2@MMLCommand@RMV PRAID
type: MMLCommand
name: RMV PRAID（删除PRA标识）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PRAID
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- PRA区域管理
- PRA区域标识管理
status: active
---

# RMV PRAID（删除PRA标识）

## 功能

**适用网元：MME**

该命令用于删除PRA区域基本信息，包括PRA区域标识、PRA区域内本网异地用户的可用属性，以及PRA区域描述信息。

## 注意事项

删除PRA区域信息时必须首先执行 [**RMV PRALSTMEM**](../PRA区域成员管理/删除PRA列表成员(RMV PRALSTMEM)_26305404.md) 删除该区域内的所有位置成员。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRAID | PRA标识 | 可选必选说明：必选参数<br>参数含义：该参数表示PRA区域的标识。<br>数据来源：整网规划<br>取值范围：0x800000～0xFFFFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRAID]] · PRA标识（PRAID）

## 使用实例

删除以“0x800001”为PRA标识的PRA区域基本信息。

RMV PRAID: PRAID="0x800001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PRAID.md`
