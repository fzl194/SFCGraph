---
id: UNC@20.15.2@MMLCommand@MOD PDPFILTERAPN
type: MMLCommand
name: MOD PDPFILTERAPN（修改APN优先级配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PDPFILTERAPN
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- PDP过滤功能
status: active
---

# MOD PDPFILTERAPN（修改APN优先级配置）

## 功能

**适用网元：SGSN**

该命令用于修改APN优先级配置。APN优先级可以用于在RAU或者RELOCATION流程中指示新侧保留PDP的顺序。高优先级APN对应的PDP会优先保留，低优先级APN对应的PDP会在切换后主动删掉。

在GU网络存在无线侧PDP能力不足的情况下，可通过此命令修改APN优先级，当系统通过RAU或者Relocation流程切换到GU网络后主动去激活低优先级的PDP，从而确保高优先级PDP业务不受影响。如不配置APN优先级，无线侧将可能随机删除重要的PDP，造成重要业务中断。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>该参数用于指定PDP过滤功能适用的用户范围。参考<br>[**SET PDPFILTERCTL**](设置PDP过滤功能参数(SET PDPFILTERCTL)_26145688.md)<br>命令。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “LOCAL_USER(本网用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件: 该参数在“用户范围”参数配置为“IMSI_PREFIX(指定IMSI前缀)”时生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字字符串。<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI名称。<br>数据来源：整网规划<br>取值范围：1～62位字符串。<br>默认值：无 |
| PRI | 优先级 | 可选必选说明：可选参数<br>该参数用于指定优先级，高优先级的配置对应的PDP会优先保留，高优先级的PDP个数未达到最大PDP保留个数时（最大PDP保留个数通过<br>[**SET PDPFILTERCTL**](设置PDP过滤功能参数(SET PDPFILTERCTL)_26145688.md)<br>配置），选择次高优先级配置对应的PDP进行保留。<br>数据来源：整网规划<br>取值范围：1~100<br>默认值：无<br>配置原则：1为最高优先级，100为最低优先级。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数是APN优先级配置的描述信息。<br>数据来源：整网规划<br>取值范围：0～32位字符串。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDPFILTERAPN]] · APN优先级配置（PDPFILTERAPN）

## 使用实例

修改一个APN优先级记录，“用户范围”为“ALL_USER(所有用户)”，“APNNI”为“huawei1.com”，“优先级”变更为“2”：

MOD PDPFILTERAPN: SUBRANGE=ALL_USER, APNNI="huawei1.com", PRI=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN优先级配置(MOD-PDPFILTERAPN)_26145690.md`
