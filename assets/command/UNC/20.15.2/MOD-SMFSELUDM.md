---
id: UNC@20.15.2@MMLCommand@MOD SMFSELUDM
type: MMLCommand
name: MOD SMFSELUDM（修改SMF选择UDM策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SMFSELUDM
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- NF发现和选择管理
- UDM选择策略管理
status: active
---

# MOD SMFSELUDM（修改SMF选择UDM策略）

## 功能

**适用NF：SMF**

该命令用于对指定的用户群修改UDM的选择策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用UDM选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>默认值：无<br>配置原则：<br>对于指定的用户群，UDM选择策略的匹配优先级从高到低依次为：“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| GPSISW | 是否使用GPSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用用户的GPSI作为目标UDM的选择条件。<br>数据来源：全网规划<br>取值范围：<br>- NO（否）<br>- YES（是）<br>默认值：无<br>配置原则：<br>SMF默认根据用户的SUPI发现和选择目标UDM；本参数只有在运营商仅使用GPSI号段规划UDM的时候才需要打开。<br>当本参数设置为YES时，则SMF发现和选择目标UDM时使用GPSI，不再使用SUPI。 |
| NSSW | 是否使用网络切片 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用用户的可用网络切片作为目标UDM的选择条件。<br>数据来源：全网规划<br>取值范围：<br>- NO（否）<br>- YES（是）<br>默认值：无<br>配置原则：<br>SMF默认发现和选择目标UDM时不使用网络切片信息；只有运营商网络需要用网络切片去发现和选择UDM时才需要打开。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFSELUDM]] · SMF选择UDM策略（SMFSELUDM）

## 使用实例

修改为漫游用户配置的目标UDM选择策略，支持使用网络切片选择UDM，执行如下命令：

```
MOD SMFSELUDM: SUBRANGE=FOREIGN_USER, NSSW=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SMFSELUDM.md`
