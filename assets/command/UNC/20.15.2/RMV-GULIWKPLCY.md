---
id: UNC@20.15.2@MMLCommand@RMV GULIWKPLCY
type: MMLCommand
name: RMV GULIWKPLCY（删除GUL互操作本地策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GULIWKPLCY
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
- N26互操作管理
- GUL互操作本地策略
status: active
---

# RMV GULIWKPLCY（删除GUL互操作本地策略）

## 功能

**适用网元：MME**

此命令用于删除GUL互操作本地策略。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要限制Non-GBR承载的QoS的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX(指定IMSI前缀)”：指网络中与指定的IMSI前缀匹配的用户。<br>- “HOME_USER(本网用户)”：指网络中的本网签约用户。<br>- “FOREIGN_USER(外网用户)” ：指网络中的漫游用户。<br>- “ALL_USER(所有用户)”：指网络中的所有用户。<br>默认值：无<br>配置原则：<br>- “SUBRANGE（用户范围）”的优先级从高到低为：“IMSI_PREFIX”，“FOREIGN_USER”或“HOME_USER”，“ALL_USER”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：整网规划<br>前提条件：该参数在“SUBRANGE”配置为“FOREIGN_USER”或“HOME_USER”后生效。<br>取值范围：整数类型，取值范围为0~64，128~254。<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在ADD MNO中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在ADD MVNO中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>数据来源：整网规划<br>前提条件：该参数在“用户范围”参数配置为“IMSI_PREFIX”后生效。<br>取值范围：5～15位十进制数字字符串。<br>默认值：无<br>配置原则：<br>当该参数配置生效时，按照IMSI最长匹配进行查询，如果有匹配的记录，使用该记录的配置；如果没有匹配的记录，则查找IMSI次长匹配的记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GULIWKPLCY]] · GUL互操作本地策略（GULIWKPLCY）

## 使用实例

删除用户范围为所有用户的GUL互操作本地策略，可以用如下命令：

```
RMV GULIWKPLCY: SUBRANGE=ALL_USER;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GUL互操作本地策略-(RMV-GULIWKPLCY)_68230973.md`
