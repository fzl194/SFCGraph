---
id: UNC@20.15.2@MMLCommand@LST SPGWCAUSECTRL
type: MMLCommand
name: LST SPGWCAUSECTRL（查询SGW-C/PGW-C原因值控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SPGWCAUSECTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM原因值管理
- GTPv2会话流程原因值控制
status: active
---

# LST SPGWCAUSECTRL（查询SGW-C/PGW-C原因值控制参数）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于查询PGW-C或融合的SGW-C/PGW-C的原因值控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流程类型。<br>数据来源：本端规划<br>取值范围：<br>- CRT_SES_PROC（初始会话创建流程）<br>- MOD_BR_PROC（承载修改流程）<br>默认值：无<br>配置原则：无 |
| CAUSESOURCE | 异常来源 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发生异常的来源。<br>数据来源：本端规划<br>取值范围：<br>- UPF（UPF）<br>- POLICY_PCF（PCF策略）<br>- CHG_3GPP（3GPP计费）<br>- POLICY_PCRF（PCRF策略）<br>- RADIUS_AUTH（Radius鉴权）<br>- INNER（内部异常）<br>- RADIUS_CHG（Radius计费）<br>- DIAMETER_AAA（Diameter AAA）<br>- CHF_3GPP（3GPP CHF）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SPGWCAUSECTRL]] · SGW-C/PGW-C原因值控制参数（SPGWCAUSECTRL）

## 使用实例

查询会话创建流程的原因值控制参数，执行命令如下：

```
%%LST SPGWCAUSECTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
                                  流程类型  =  初始会话创建流程
                                  异常来源  =  UPF
        周边网元拒绝导致流程拒绝原因值组号  =  2
      周边网元响应超时导致流程拒绝的原因值  =  26
APN锁定或整机锁定导致流程拒绝的GTPv2原因值  =  NULL
       IP地址耗尽导致流程拒绝的GTPv2原因值  =  NULL
     发送消息流控导致流程拒绝的GTPv2原因值  =  NULL
                            承载受限原因值  =  #73 无资源可用
                             CPU过载原因值  =  #73 无资源可用
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGW-C_PGW-C原因值控制参数（LST-SPGWCAUSECTRL）_09652447.md`
