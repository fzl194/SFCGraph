---
id: UNC@20.15.2@MMLCommand@ADD TMT3N3
type: MMLCommand
name: ADD TMT3N3（增加Tm接口指定消息T3N3参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TMT3N3
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Tm接口管理
- Tm接口消息重传参数管理
status: active
---

# ADD TMT3N3（增加Tm接口指定消息T3N3参数）

## 功能

**适用网元：MME**

本命令用于增加Tm接口消息T3N3参数。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMSPECIALMSGCFG | 指定Tm接口消息 | 可选必选说明：必选参数<br>参数含义：指定具体的Tm接口消息设置T3N3参数。<br>数据来源：全网规划<br>取值范围：<br>- “SPECIAL_TM_MSG（指定Tm接口消息）”<br>默认值 ：无 |
| TMMSG | Tm接口消息 | 可选必选说明：条件必选参数<br>前提条件：该参数在“指定Tm接口消息”参数配置为“SPECIAL_TM_MSG”后生效。<br>参数含义：Tm接口消息列表。<br>数据来源：全网规划<br>取值范围：<br>- “ECHO（Echo Request）”<br>- “STRT_ENB_TA_INFO_UPDATE_REQ（Start eNB TA Information Update Request）”<br>- “UPDATE_ENB_TA_INFO_REQ（Update eNodeB TA Information Request）”<br>- “TRK_GP_UL_S1_DT_NTF（Trunk Group UL S1 Direct Transfer Notification）”<br>- “TRK_USR_ATT_REQ（Trunk User Attach Request）”<br>- “TRK_USR_DET_REQ（Trunk User Detach Request）”<br>- “TRK_USR_HO_REQ（Trunk User Handover Request）”<br>- “TRK_USR_HO_NTF（Trunk User Handover Notification）”<br>- “TRK_USR_TAU_REQ（Trunk User TAU Request）”<br>- “TRK_USR_SR_REQ（Trunk User Service Request）”<br>- “NODE_ST_NTF（NE Status Notification）”<br>默认值 ：无 |
| TRSP | T-RESPONSE(s) | 可选必选说明：必选参数<br>参数含义：该参数用于指定等待一条T3请求消息的响应消息的最大时长。如果请求消息没有在“TRSP”内收到响应，并且发送次数小于“NREQ”，则重新发送该请求消息。<br>数据来源：全网规划<br>取值范围：1~20<br>默认值 ：无 |
| NREQ | N-REQUEST(times) | 可选必选说明：必选参数<br>参数含义：该参数用于指定Tm接口发送一条请求消息的最大尝试次数。<br>数据来源：本端规划<br>取值范围：1~5<br>默认值 ：无 |

## 操作的配置对象

- [Tm接口消息T3N3参数（TMT3N3）](configobject/UNC/20.15.2/TMT3N3.md)

## 使用实例

该命令用于增加Tm接口指定消息T3N3参数，执行如下命令：

```
ADD TMT3N3:TMSPECIALMSGCFG=SPECIAL_TM_MSG,TMMSG=ECHO,TRSP=3,NREQ=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Tm接口指定消息T3N3参数(ADD-TMT3N3)_41654657.md`
