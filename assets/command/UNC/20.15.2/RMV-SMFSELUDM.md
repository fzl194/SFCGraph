---
id: UNC@20.15.2@MMLCommand@RMV SMFSELUDM
type: MMLCommand
name: RMV SMFSELUDM（删除SMF选择UDM策略）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV SMFSELUDM（删除SMF选择UDM策略）

## 功能

**适用NF：SMF**

该命令用于对指定的用户群删除UDM的选择策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用UDM选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>默认值：无<br>配置原则：<br>对于指定的用户群，UDM选择策略的匹配优先级从高到低依次为：“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFSELUDM]] · SMF选择UDM策略（SMFSELUDM）

## 使用实例

删除为漫游用户配置的目标UDM选择策略，恢复到默认的选择策略，执行如下命令：

```
RMV SMFSELUDM: SUBRANGE=FOREIGN_USER;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SMF选择UDM策略（RMV-SMFSELUDM）_48290741.md`
