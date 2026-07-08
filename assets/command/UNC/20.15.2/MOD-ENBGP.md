---
id: UNC@20.15.2@MMLCommand@MOD ENBGP
type: MMLCommand
name: MOD ENBGP（修改eNodeB群组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: ENBGP
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
- eNodeB群组管理
status: active
---

# MOD ENBGP（修改eNodeB群组）

## 功能

**适用网元：MME**

此命令用于修改eNodeB群组记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBGPID | eNodeB群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB群组标识。<br>数据来源：本端规划<br>取值范围：1~2048<br>默认值：无 |
| TYPE | 类型 | 可选必选说明：必选参数<br>参数含义：用于指定该eNodeB群组的类型。<br>数据来源：整网规划<br>取值范围：<br>- “ENTRY(入口)”<br>- “INSIDE(内部)”<br>默认值：无<br>配置原则：<br>- ENTRY(入口)：入口eNodeB群组用于定义在MME覆盖边界专用网络区域和高铁站候车厅配置专网入口的eNodeB群组。对于从入口eNodeB进入内部eNodeB群组覆盖区域的用户，当其驻留时长超过三倍“驻留时长（min）”时，UNC将其从该区域迁出。<br>- INSIDE(内部)：内部eNodeB群组用于定义低速区域专用网络的eNodeB群组。对于在内部eNodeB群组覆盖区域的用户，当驻留时长超过“驻留时长（min）”时，UNC将其从该区域迁出。 |
| STICK_TIME | 驻留时长（min） | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置UE在内部eNodeB群组覆盖区域的驻留时间阈值，当UE在区域内的驻留时间超过配置值，或者UE在该参数配置的周期内接入次数超过参数“接入次数”配置值时，<br>UNC<br>将其从该区域迁出。<br>前提条件：该参数在“TYPE（类型）”参数配置为“INSIDE(内部)”后生效。<br>数据来源：本端规划<br>取值范围：10min~120min<br>默认值：无 |
| ACC_TIMES | 接入次数 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置UE在内部eNodeB群组覆盖区域的接入次数阈值。如果在“驻留时长（min）”参数配置的时间里，UE连续接入内部eNodeB群组次数超过配置值，<br>UNC<br>将其从该区域迁出。<br>前提条件：该参数在<br>“TYPE（类型）”<br>参数配置为<br>“INSIDE(内部)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0,3~100<br>默认值：无<br>配置原则：参数设置为0时，依据接入次数迁出功能不生效。 |
| ENBGPNAME | eNodeB群组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB群组名称。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ENBGP]] · eNodeB群组（ENBGP）

## 使用实例

修改一个eNodeB群组，eNodeB群组标识为“1”，类型为“入口”，群组名称为“highspeed_usercheck_entry”:

MOD ENBGP: ENBGPID=1, TYPE=ENTRY, ENBGPNAME="highspeed_usercheck_entry";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-ENBGP.md`
