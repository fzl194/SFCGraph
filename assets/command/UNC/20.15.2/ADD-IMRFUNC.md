---
id: UNC@20.15.2@MMLCommand@ADD IMRFUNC
type: MMLCommand
name: ADD IMRFUNC（增加用户消息统计功能配置）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD IMRFUNC（增加用户消息统计功能配置）

## 功能

**适用网元：SGSN、MME**

该命令用于增加消息统计任务，配置消息统计的用户范围和接口范围，以方便问题定位。

## 注意事项

- 开启消息统计功能会增加系统负荷。
- 该命令执行后对正在进行流程处理的用户暂不生效，系统会在用户的任意新的流程，根据最新的配置进行消息统计。
- 基于所有用户的消息统计功能配置最多可以输入1条记录。
- 基于指定用户的消息统计功能配置最多可以输入64条记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_USER(指定用户)”<br>默认值 ：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_USER”<br>后生效。<br>数据来源：全网规划<br>取值范围：5~15位数字<br>默认值 ：无 |
| INTERFACETYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “S11(S11接口)”<br>- “S6a(S6a接口)”<br>- “SGs(SGs接口)”<br>- “Sv(Sv接口)”<br>默认值 ：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMRFUNC]] · 用户消息统计功能配置（IMRFUNC）

## 使用实例

增加一条 “用户范围” 为 “SPECIAL_USER” ， “IMSI前缀” 为 “123000” ， “接口类型” 为 “S11-1&S6a-1&SGs-1&Sv-1” 的IMRFUNC配置记录：

ADD IMRFUNC: SUBRANGE=SPECIAL_USER, IMSIPRE="123000", INTERFACETYPE=S11-1&S6a-1&SGs-1&Sv-1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加用户消息统计功能配置(ADD-IMRFUNC)_72225087.md`
