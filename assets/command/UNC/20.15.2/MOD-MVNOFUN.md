---
id: UNC@20.15.2@MMLCommand@MOD MVNOFUN
type: MMLCommand
name: MOD MVNOFUN（修改MVNO功能配置信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: MVNOFUN
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
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

# MOD MVNOFUN（修改MVNO功能配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于修改这个MVNO用户功能信息。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOID | MVNO标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示修改这个MVNO用户的功能配置。<br>数据来源：整网规划<br>取值范围：1～64<br>建议值：无 |
| SMS | 是否支持短消息 | 可选必选说明：可选参数<br>参数含义：该参数用于表示此MVNO用户是否支持短消息业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>建议值：无<br>配置原则：如果填写<br>“YES(是)”<br>，此MVNO用户可以使用短消息业务。如果填写<br>“NO(否)”<br>，系统将限制此MVNO用户不能使用短消息业务。 |
| LCS | 是否支持LCS | 可选必选说明：可选参数<br>参数含义：该参数用于表示此MVNO用户是否支持LCS业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>建议值：无<br>配置原则：如果填写<br>“YES(是)”<br>，此MVNO用户可以使用LCS业务。如果填写<br>“NO(否)”<br>，系统将限制此MVNO用户不能使用LCS业务。 |
| CMP | 是否支持SNDCP压缩 | 可选必选说明：可选参数<br>参数含义：该参数用于表示此MVNO用户是否支持Gb接口的SNDCP压缩功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>建议值：无<br>配置原则：如果填写<br>“YES(是)”<br>，此MVNO用户可以使用Gb接口的SNDCP压缩功能。如果填写<br>“NO(否)”<br>，系统将限制此MVNO用户不能使用Gb接口的SNDCP压缩功能。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MVNOFUN]] · MVNO功能配置信息（MVNOFUN）

## 使用实例

修改标识为1的MVNO的功能，支持SMS功能：

MOD MVNOFUN: MVNOID=1, SMS=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改MVNO功能配置信息(MOD-MVNOFUN)_26146062.md`
