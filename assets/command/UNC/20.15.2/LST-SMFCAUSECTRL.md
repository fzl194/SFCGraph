---
id: UNC@20.15.2@MMLCommand@LST SMFCAUSECTRL
type: MMLCommand
name: LST SMFCAUSECTRL（查询SMF流程控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFCAUSECTRL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM原因值管理
- 5GC会话流程原因值控制
status: active
---

# LST SMFCAUSECTRL（查询SMF流程控制参数）

## 功能

**适用NF：SMF**

该命令用于查询SMF流程控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流程类型，要根据场景来配置相应的流程。<br>数据来源：全网规划<br>取值范围：<br>- PDU_SESSION_EST_PROC（PDU Session创建流程）<br>- PDU_SESSION_MOD_PROC（PDU Session修改流程）<br>默认值：无<br>配置原则：<br>当需要针对会话创建流程配置控制规则时，该参数设置为PDU_SESSION_EST_PROC。<br>当需要针对会话修改流程配置控制规则时，该参数设置为PDU_SESSION_MOD_PROC。 |
| NFTYPE | 异常来源 | 可选必选说明：可选参数<br>参数含义：该参数用于描述发生异常的NF名称。<br>数据来源：全网规划<br>取值范围：<br>- UPF（UPF）<br>- CHG_3GPP（3GPP计费）<br>- POLICY_PCF（PCF策略）<br>- INNER（内部异常）<br>- RADIUS_AUTH（Radius鉴权）<br>- RADIUS_CHG（Radius计费）<br>- UDM（UDM）<br>- CHF_3GPP（3GPP CHF）<br>- INNER_EMG（紧急会话内部异常）<br>默认值：无<br>配置原则：<br>UDM网元类型仅在“流程类型”为“PDU Session创建流程”时生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFCAUSECTRL]] · SMF流程控制参数（SMFCAUSECTRL）

## 使用实例

查询全部的SMF流程控制参数:

```
%%LST SMFCAUSECTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
                                     流程类型  =  PDU Session创建流程
                                     异常来源  =  3GPP CHF
                 NF拒绝导致流程拒绝原因值组号  =  0
              响应超时导致流程拒绝的NAS原因值  =  0
     APN锁定或整机锁定导致流程拒绝的NAS原因值  =  NULL
          发送消息流控导致流程拒绝的NAS原因值  =  NULL
发送消息因紧急业务配置导致流程拒绝的NAS原因值  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMF流程控制参数（LST-SMFCAUSECTRL）_09652371.md`
