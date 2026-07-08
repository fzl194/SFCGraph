---
id: UNC@20.15.2@MMLCommand@MOD PRAID
type: MMLCommand
name: MOD PRAID（修改PRA标识）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD PRAID（修改PRA标识）

## 功能

**适用网元：MME**

该命令用于修改指定PRA区域的基本信息，例如该PRA区域内本网异地用户的可用属性、PRA区域的描述信息。

## 注意事项

无

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRAID | PRA标识 | 可选必选说明：必选参数<br>参数含义：该参数表示PRA区域的标识。<br>数据来源：整网规划<br>取值范围：0x800000～0xFFFFFF<br>默认值：无 |
| NONLOCAL | 本网异地用户可用开关 | 可选必选说明：可选参数<br>参数含义：该参数用以表示本网异地用户是否可用PRA功能。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>默认值:无<br>配置原则：<br>- “ON(打开)”：表示本网异地用户可用PRA功能。<br>- “OFF(关闭)”：表示本网异地用户不可用PRA功能。<br>说明：当本参数设置为“ON”时，本网异地用户能否使用PRA功能还依赖于PCRF等网元是否启动对该用户的PRA订阅。 |
| PRANAME | PRA名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PRA名称。<br>数据来源：整网规划<br>取值范围：0～32位字符串<br>默认值：无 |

## 操作的配置对象

- [PRA标识（PRAID）](configobject/UNC/20.15.2/PRAID.md)

## 使用实例

配置以“0x800001”为PRA标识的PRA区域基本信息。

MOD PRAID: PRAID="0x800001", NONLOCAL=OFF, PRANAME="praname2";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PRA标识(MOD-PRAID)_72345193.md`
