---
id: UNC@20.15.2@MMLCommand@RMV IMRFUNC
type: MMLCommand
name: RMV IMRFUNC（删除用户消息统计功能配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMRFUNC
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 跟踪配置管理
- 信令采集
status: active
---

# RMV IMRFUNC（删除用户消息统计功能配置）

## 功能

**适用网元：SGSN、MME**

该命令用于删除用户消息统计功能配置。

## 注意事项

- 该命令执行后对正在进行流程处理的用户暂不生效，系统会在用户的任意新的流程，根据最新的配置进行用户消息统计。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_USER(指定用户)”<br>默认值 ：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_USER”<br>后生效。<br>数据来源：全网规划<br>取值范围：5~15位数字<br>默认值 ：无 |

## 操作的配置对象

- [用户消息统计功能配置（IMRFUNC）](configobject/UNC/20.15.2/IMRFUNC.md)

## 使用实例

删除一条 “用户范围” 为 “ALL_USER” 的IMRFUNC配置记录：

RMV IMRFUNC: SUBRANGE=ALL_USER;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户消息统计功能配置(RMV-IMRFUNC)_72345009.md`
