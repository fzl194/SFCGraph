---
id: UNC@20.15.2@MMLCommand@ADD MVNOFUN
type: MMLCommand
name: ADD MVNOFUN（增加MVNO功能配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MVNOFUN
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 64
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO功能配置表
status: active
---

# ADD MVNOFUN（增加MVNO功能配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于配置MVNO的用户可以使用的一些业务和功能。通过配置MVNO功能，可以限制MVNO用户的业务特性。

## 注意事项

- MVNOID在MVNO标识表中已经配置。
- 此命令执行后立即生效。
- 此命令最大记录数为64个。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOID | MVNO标识 | 可选必选说明：必选参数<br>参数含义：该参数用于增加此MVNO用户的功能配置。<br>数据来源：整网规划<br>取值范围：1～64<br>默认值：无 |
| SMS | 是否支持短消息 | 可选必选说明：可选参数<br>参数含义：该参数用于设置此MVNO的用户是否支持短消息业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)”<br>配置原则：如果填写<br>“YES(是)”<br>，此MVNO的用户可以使用短消息业务。如果填写<br>“NO(否)”<br>，系统将限制此MVNO的用户不能使用短消息业务。 |
| LCS | 是否支持LCS | 可选必选说明：可选参数<br>参数含义：该参数用于设置此MVNO的用户是否支持LCS业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)”<br>配置原则：如果填写<br>“YES(是)”<br>，此MVNO的用户可以使用LCS业务。如果填写<br>“NO(否)”<br>，系统将限制此MVNO的用户不能使用LCS业务。 |
| CMP | 是否支持SNDCP压缩 | 可选必选说明：可选参数<br>参数含义：该参数用于设置此MVNO的用户是否支持Gb接口的SNDCP压缩功能。<br>数据来源：整网规划<br>取值范围：<br>- “ NO(否)”<br>- “YES(是)”<br>默认值：<br>“ NO(否)”<br>配置原则：如果填写<br>“YES(是)”<br>，此MVNO的用户可以使用Gb接口的SNDCP压缩功能。如果填写<br>“ NO(否)”<br>，系统将限制此MVNO的用户不能使用Gb接口的SNDCP压缩功能。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MVNOFUN]] · MVNO功能配置信息（MVNOFUN）

## 使用实例

配置标识为2的MVNO的功能，不支持LCS功能，支持SNDCP压缩功能：

ADD MVNOFUN: MVNOID=2, LCS=NO, CMP=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加MVNO功能配置信息(ADD-MVNOFUN)_26305870.md`
