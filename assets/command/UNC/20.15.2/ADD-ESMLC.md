---
id: UNC@20.15.2@MMLCommand@ADD ESMLC
type: MMLCommand
name: ADD ESMLC（增加E-SMLC配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ESMLC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 6
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- E-SMLC配置
status: active
---

# ADD ESMLC（增加E-SMLC配置）

## 功能

**适用网元：MME**

此命令用于增加E-SMLC配置。在MME系统中配置E-SMLC信息，用于MME进行负荷分担选择E-SMLC。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为6。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ESMLCID | E-SMLC 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定E-SMLC标识。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>说明：<br>- E-SMLC标识用于唯一标识整网络中某一可用的E-SMLC。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定E-SMLC的优先级。<br>数据来源：整网规划<br>取值范围：0～5<br>默认值：0<br>配置原则：<br>- 定位业务选择E-SMLC时，根据优先级选择高优先级的E-SMLC，0优先级最高，5优先级最低。<br>- 不同E-SMLC可以配置相同优先级。<br>- 相同优先级的E-SMLC，根据负荷分担原则选择E-SMLC。 |
| ESMLCNAME | E-SMLC名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定E-SMLC名称。<br>数据来源：整网规划<br>取值范围：1～20位字符串<br>默认值：无 |
| RATIESW | 是否携带RAT Type信元 | 可选必选说明：可选参数<br>参数含义：该参数表示在MME发送给E-SMLC的LCS-AP Location Request消息中是否携带RAT Type信元。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>配置原则：<br>- 当启用针对NB-IoT的延迟定位时，需要设置该参数为“YES(是)”。<br>- 如果对端E-SMLC不支持RAT Type信元，但需要开启延迟定位特性时，需要设置该参数为“NO(否)”。 |

## 操作的配置对象

- [E-SMLC配置（ESMLC）](configobject/UNC/20.15.2/ESMLC.md)

## 使用实例

增加一条“E-SMLC 标识”为“1”，“优先级”为“2”，“E-SMLC名称”为“ESMLC1”的E-SMLC配置记录：

ADD ESMLC: ESMLCID=1, PRIORITY=2, ESMLCNAME="ESMLC1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加E-SMLC配置(ADD-ESMLC)_26145800.md`
