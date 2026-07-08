---
id: UNC@20.15.2@MMLCommand@LST TMT3N3
type: MMLCommand
name: LST TMT3N3（查询Tm接口消息T3N3参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TMT3N3
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Tm接口管理
- Tm接口消息重传参数管理
status: active
---

# LST TMT3N3（查询Tm接口消息T3N3参数）

## 功能

**适用网元：MME**

本命令用于查询Tm接口消息的T3N3参数。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMMSGCFGMODE | Tm接口消息配置模式 | 可选必选说明：可选参数<br>参数含义：本参数用于选择Tm接口消息配置方式。<br>数据来源：全网规划<br>取值范围：<br>- “TMMSG_ALL（Tm接口消息全集）”<br>- “SPECIAL_TM_MSG（指定Tm接口消息）”<br>默认值 ：无 |
| TMMSG | Tm接口消息 | 可选必选说明：条件可选参数<br>前提条件：该参数在“指定Tm接口消息”参数配置为“SPECIAL_TM_MSG”后生效。<br>参数含义：Tm接口消息列表。<br>数据来源：全网规划<br>取值范围：<br>- “ECHO（Echo Request）”<br>- “STRT_ENB_TA_INFO_UPDATE_REQ（Start eNB TA Information Update Request）”<br>- “UPDATE_ENB_TA_INFO_REQ（Update eNodeB TA Information Request）”<br>- “TRK_GP_UL_S1_DT_NTF（Trunk Group UL S1 Direct Transfer Notification）”<br>- “TRK_USR_ATT_REQ（Trunk User Attach Request）”<br>- “TRK_USR_DET_REQ（Trunk User Detach Request）”<br>- “TRK_USR_HO_REQ（Trunk User Handover Request）”<br>- “TRK_USR_HO_NTF（Trunk User Handover Notification）”<br>- “TRK_USR_TAU_REQ（Trunk User TAU Request）”<br>- “TRK_USR_SR_REQ（Trunk User Service Request）”<br>- “NODE_ST_NTF（NE Status Notification）”<br>默认值 ：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TMT3N3]] · Tm接口消息T3N3参数（TMT3N3）

## 使用实例

1. 查询指定Tm接口消息为Tm接口消息全集的参数配置：
  LST TMT3N3:TMMSGCFGMODE=TMMSG_ALL ;
  ```
  %%LST TMT3N3:TMMSGCFGMODE=TMMSG_ALL ;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
    指定Tm接口消息  =  Tm接口消息全集         
        Tm接口消息  =  NULL     
     T-RESPONSE(s)  =  1   
  N-REQUEST(times)  =  1

  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TMT3N3.md`
