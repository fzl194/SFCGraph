---
id: UNC@20.15.2@MMLCommand@RMV CHGGNCCCFG
type: MMLCommand
name: RMV CHGGNCCCFG（删除Gn接口计费属性选择策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHGGNCCCFG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- Gn接口计费属性选择策略配置
status: active
---

# RMV CHGGNCCCFG（删除Gn接口计费属性选择策略）

## 功能

**适用网元：SGSN**

该命令用于删除 “SPECIAL_USER(指定用户)” 的Gn接口计费属性选择策略。

## 注意事项

- 该命令执行后立即生效。
- 系统默认配置的“ALL_USER(所有用户)”无法被删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要删除<br>“SPECIAL_USER(指定用户)”<br>的IMSI前缀，系统根据该参数与用户的IMSI进行匹配，从而区分不同的用户群。<br>取值范围：5～15位十进制数字<br>默认值：无<br>说明：- 按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGGNCCCFG]] · Gn接口计费属性选择策略（CHGGNCCCFG）

## 使用实例

“删除IMSIPRE（IMSI前缀）” 为 “10010” 的记录：

RMV CHGGNCCCFG: IMSIPRE="10010";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CHGGNCCCFG.md`
