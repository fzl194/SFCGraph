---
id: UNC@20.15.2@MMLCommand@RMV N26IWKPLCY
type: MMLCommand
name: RMV N26IWKPLCY（删除EPS与5GS互操作本地策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: N26IWKPLCY
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
- N26互操作策略
status: active
---

# RMV N26IWKPLCY（删除EPS与5GS互操作本地策略）

## 功能

**适用网元：MME**

该命令用于5GS部署时，删除用户的EPS与5GS互操作本地策略。

## 注意事项

- 该命令执行后不会对正在进行信令流程的用户立即生效，该命令中的限制会在用户的下一次信令流程中生效。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置EPS与5GS互操作策略的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：表示用户范围为系统内所有用户。<br>- “HOME_USER（本网用户）”：表示用户范围为本网用户。<br>- “FOREIGN_USER（外网用户）”：表示用户范围为外网用户。<br>- “IMSI_PREFIX（指定IMSI前缀）”：表示用户范围通过IMSI前缀指定。<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用以指定待配置EPS与5GS互操作控本地策略用户的IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～15十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [EPS与5GS互操作本地策略（N26IWKPLCY）](configobject/UNC/20.15.2/N26IWKPLCY.md)

## 使用实例

删除一条 “用户范围” 为“ALL_USER(所有用户)”的记录。

RMV N26IWKPLCY: SUBRANGE=ALL_USER;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除EPS与5GS互操作本地策略(RMV-N26IWKPLCY)_26146136.md`
