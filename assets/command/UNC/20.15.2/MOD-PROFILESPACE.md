---
id: UNC@20.15.2@MMLCommand@MOD PROFILESPACE
type: MMLCommand
name: MOD PROFILESPACE（修改Profile Space）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PROFILESPACE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- Profile Space
status: active
---

# MOD PROFILESPACE（修改Profile Space）

## 功能

**适用NF：PGW-C、SMF**

本命令用于修改Profile Space实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROFSPACENAME | Profile Space名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ProfileSpace名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ALWAYSALLOWPROF | Always Allowed Profile名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ProfileSpace下默认生效的UserProfile。如果配置了默认生效的UserProfile，则用户激活时默认安装此UserProfile下绑定的规则。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PREFIXSW | 拼接开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制将PCRF下发的Charging-Rule-Base-Name/Charging-Rule-Name映射至本地配置的USERPROFILE/RULE过程中，是否进行拼接处理。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：N\A。 |
| PREFIXSTRING | 拼接字符串 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PREFIXSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于控制拼接时用“PROFSPACENAME”拼接还是用本参数指定的字符串拼接。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PROFILESPACE]] · Profile Space（PROFILESPACE）

## 使用实例

修改ProfileSpace配置，PROFSPACENAME为“profilespace1”，ALWAYSALLOWPROF为“userprofile2”，PREFIXSW为“ENABLE”：

```
MOD PROFILESPACE:PROFSPACENAME="profilespace1",ALWAYSALLOWPROF="userprofile2",PREFIXSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Profile-Space（MOD-PROFILESPACE）_09897048.md`
