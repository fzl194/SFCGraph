---
id: UNC@20.15.2@MMLCommand@MOD RESTOUSRSEG
type: MMLCommand
name: MOD RESTOUSRSEG（修改容灾用户号段参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: RESTOUSRSEG
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME容灾管理
- 容灾用户号段管理
status: active
---

# MOD RESTOUSRSEG（修改容灾用户号段参数）

## 功能

**适用网元：MME**

此命令用于修改容灾用户号段参数置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链式备份功能服务的用户范围。<br>取值范围：<br>- IMSI_PREFIX(指定IMSI前缀)<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 必选说明：条件必选参数<br>参数含义：该参数用于指定链式备份功能服务的用户范围的IMSI前缀。<br>前提条件：该参数在“用户范围”参数配置为“IMSI_PREFIX(指定IMSI前缀)”后生效。<br>数据来源：全网规划<br>取值范围：5～15位十进制数字字符串。<br>默认值：无<br>配置原则： 无<br>说明：- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| ISRESTO | 是否备份用户 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否备份指定用户号段的用户信息。<br>取值范围：<br>- YES (是)<br>- NO (否)<br>默认值：YES (是)<br>配置原则：无 |

## 操作的配置对象

- [容灾用户号段参数（RESTOUSRSEG）](configobject/UNC/20.15.2/RESTOUSRSEG.md)

## 使用实例

1. 修改容灾用户号段参数配置，可以用如下命令：
  ```
  MOD RESTOUSRSEG: SUBRANGE=IMSI_PREFIX, IMSIPRE="12345", ISRESTO=YES;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改容灾用户号段参数-(MOD-RESTOUSRSEG)_10474089.md`
