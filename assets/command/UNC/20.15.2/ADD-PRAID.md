---
id: UNC@20.15.2@MMLCommand@ADD PRAID
type: MMLCommand
name: ADD PRAID（增加PRA标识）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PRAID
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- PRA区域管理
- PRA区域标识管理
status: active
---

# ADD PRAID（增加PRA标识）

## 功能

**适用网元：MME**

该命令用于配置PRA区域基本信息，包括PRA区域标识、PRA区域内本网异地用户的可用属性，以及PRA区域描述信息。PRA可分为核心网预定义PRA（Core Network predefined PRA）和UE专属PRA（UE-dedicated PRA）两种。其中在MME上配置的PRA都是核心网预定义PRA。

## 注意事项

- 此命令执行后立即生效。
- 该命令最大记录数为1024。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRAID | PRA标识 | 可选必选说明：必选参数<br>参数含义：该参数表示PRA区域的标识。<br>数据来源：整网规划<br>取值范围：0x800000～0xFFFFFF<br>默认值：无 |
| NONLOCAL | 本网异地用户可用开关 | 可选必选说明：可选参数<br>参数含义：该参数用以表示本网异地用户是否可用PRA功能。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>默认值：OFF(关闭)<br>配置原则：<br>- “ON(打开)”：表示本网异地用户可用PRA功能。<br>- “OFF(关闭)”：表示本网异地用户不可用PRA功能。<br>说明：当本参数设置为“ON”时，本网异地用户能否使用PRA功能还依赖于PCRF等网元是否启动对该用户的PRA订阅。 |
| PRANAME | PRA名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PRA名称。<br>数据来源：整网规划<br>取值范围：0～32位字符串<br>默认值：noname |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PRAID]] · PRA标识（PRAID）

## 使用实例

配置以“0x800001”为PRA标识的PRA区域基本信息。

ADD PRAID: PRAID="0x800001", NONLOCAL=ON, PRANAME="praname1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PRAID.md`
