---
id: UNC@20.15.2@MMLCommand@RMV TMT3N3
type: MMLCommand
name: RMV TMT3N3（删除Tm接口指定消息T3N3参数）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV TMT3N3（删除Tm接口指定消息T3N3参数）

## 功能

**适用网元：MME**

本命令用于删除指定Tm接口消息T3N3参数。不能用于删除TM路径的T3和N3系统初始设置值，初始设置值请在 **ADD TMT3N3** 命令查看。

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

## 操作的配置对象

- [[configobject/UNC/20.15.2/TMT3N3]] · Tm接口消息T3N3参数（TMT3N3）

## 使用实例

删除Tm接口Trunk User Attach Request消息T3N3参数：

```
RMV TMT3N3: TMSPECIALMSGCFG=SPECIAL_TM_MSG, TMMSG=TRK_USR_ATT_REQ;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-TMT3N3.md`
