---
id: UNC@20.15.2@MMLCommand@LST RDSAUTHREQVSA
type: MMLCommand
name: LST RDSAUTHREQVSA（查询RADIUS鉴权请求携带的私有扩展属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RDSAUTHREQVSA
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 鉴权管理
- 请求消息信元控制
status: active
---

# LST RDSAUTHREQVSA（查询RADIUS鉴权请求携带的私有扩展属性）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查询发送到指定RADIUS服务器组的鉴权请求消息中是否携带3GPP（26/10415）扩展属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | RADIUS服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定鉴权服务器组名。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>配置RADIUS服务器组名前，需要先使用ADD RDSSVRGRP命令配置RADIUS服务器组信息。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSAUTHREQVSA]] · RADIUS鉴权请求携带的私有扩展属性（RDSAUTHREQVSA）

## 使用实例

查询服务器组名称为rds的3GPP扩展属性在鉴权请求消息中是否支持：

```
%%LST RDSAUTHREQVSA:RDSSVRGRPNAME="rds";%%
RETCODE = 0  操作成功

结果如下
--------
              RADIUS服务器组名称  =  rds
            3GPP私有扩展属性开关  =  禁止
                       3GPP-IMSI  =  允许
                3GPP-Charging-ID  =  允许
                   3GPP-PDP-Type  =  允许
                 3GPP-CG-Address  =  允许
3GPP-GPRS-Negotiated-QoS-Profile  =  允许
          3GPP-SGSN(SGW)-Address  =  允许
               3GPP-GGSN-Address  =  允许
               3GPP-IMSI-MCC-MNC  =  允许
               3GPP-GGSN-MCC-MNC  =  允许
                      3GPP-NSAPI  =  允许
             3GPP-Selection-Mode  =  允许
   3GPP-Charging-Characteristics  =  允许
          3GPP-SGSN(SGW)-MCC-MNC  =  允许
                     3GPP-IMEISV  =  允许
                   3GPP-RAT-Type  =  允许
         3GPP-User-Location-Info  =  允许
                3GPP-MS-TimeZone  =  允许
            3GPP-Negotiated-DSCP  =  允许
          3GPP-SGSN-IPv6-Address  =  允许
          3GPP-GGSN-IPv6-Address  =  允许
            3GPP-CG-IPv6-Address  =  禁止
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RADIUS鉴权请求携带的私有扩展属性（LST-RDSAUTHREQVSA）_28567653.md`
