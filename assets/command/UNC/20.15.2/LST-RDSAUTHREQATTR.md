---
id: UNC@20.15.2@MMLCommand@LST RDSAUTHREQATTR
type: MMLCommand
name: LST RDSAUTHREQATTR（查询Radius鉴权请求消息携带的属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RDSAUTHREQATTR
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
- 请求消息携带的属性
status: active
---

# LST RDSAUTHREQATTR（查询Radius鉴权请求消息携带的属性）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来显示指定RADIUS服务器组的可选鉴权消息属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | RADIUS服务器组名称 | 可选必选说明：可选参数<br>参数含义：RADIUS服务器组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>需要确保RADIUS服务器组名称已经通过ADD RDSSVRGRP配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RDSAUTHREQATTR]] · Radius鉴权请求消息携带的属性（RDSAUTHREQATTR）

## 使用实例

查询名为“radiusgroup”的Radius服务器组的可选鉴权消息属性信息：

```
%%LST RDSAUTHREQATTR: RDSSVRGRPNAME="radiusgroup";%%
RETCODE = 0  操作成功

结果如下
--------
              RADIUS服务器组名称  =  radiusgroup
                 Acct-Session-Id  =  禁止
                          NAS-ID  =  禁止
                     NAS ID Type  =  APN
                    NAS ID Value  =  NULL
                            IMSI  =  禁止
                     Charging-ID  =  禁止
                     Prepaid-ind  =  禁止
                         GGSN-IP  =  禁止
                  SGSN (S-GW)-IP  =  禁止
                   Requested-APN  =  禁止
                     GGSN-Vendor  =  禁止
                    GGSN-Version  =  禁止
           Request Authenticator  =  禁止
           Acct-Multi-Session-Id  =  允许
                 Event-Timestamp  =  允许
             NAS-Port-Id属性开关  =  禁止
               NAS-Port-Id属性值  =  UNC
UE-Local-IP-Address和UE-UDP-Port  =  禁止
              Calling-Station-Id  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RDSAUTHREQATTR.md`
