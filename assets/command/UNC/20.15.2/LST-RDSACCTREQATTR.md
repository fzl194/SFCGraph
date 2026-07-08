---
id: UNC@20.15.2@MMLCommand@LST RDSACCTREQATTR
type: MMLCommand
name: LST RDSACCTREQATTR（查询RADIUS计费服务器可选消息属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RDSACCTREQATTR
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS计费管理
- 基础信元控制
status: active
---

# LST RDSACCTREQATTR（查询RADIUS计费服务器可选消息属性）

## 功能

**适用NF：PGW-C、SMF**

该命令用来显示指定RADIUS服务器组的RADIUS计费私有扩展属性的配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | RADIUS Server Group名称 | 可选必选说明：可选参数<br>参数含义：RADIUS服务器组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RDSACCTREQATTR]] · RADIUS计费服务器可选消息属性（RDSACCTREQATTR）

## 使用实例

查询名为“radiusgroup”的RADIUS计费服务器组的私有扩展属性信息：

```
LST RDSACCTREQATTR:RDSSVRGRPNAME="radiusgroup";
```

```

RETCODE = 0  操作成功

radius Server Group的AAA计费私有扩展属性
----------------------------------------
                            RADIUS Server Group名称  =  radiusgroup
                             支持Calling-Station-Id  =  携带该信元。
                       指定Calling-Station-Id的内容  =  MSISDN
                                   支持携带IMSI属性  =  不携带该信元。
                  支持携带acct-multi-session-id属性  =  携带该信元。
                            支持携带Charging ID属性  =  不携带该信元。
                            支持携带Prepaid-ind属性  =  携带该信元。
                        支持携带GGSN-IP-address属性  =  携带该信元。
                支持携带SGSN（S-GW）-IP-address属性  =  不携带该信元。
                         支持携带Nas-Identifier属性  =  DISABLE
                               Nas-Identifier属性值  =  NULL
                                      Requested-apn  =  不携带该信元。
                                   计费扩展属性开关  =  携带该信元。
                        支持携带属性Acct-Link-Count  =  携带该信元。
                             支持携带属性Event-Time  =  携带该信元。
  支持携带属性Acct-Input-Octets和Acct-Output-Octets  =  携带该信元。
支持携带属性Acct-Input-Packets和Acct-Output-Packets  =  携带该信元。
                        支持携带属性acct-delay-time  =  携带该信元。
                        支持携带属性Acct-Session-ID  =  携带该信元。
                  支持携带属性Charge-Rule-Base-Name  =  不携带该信元。
                            支持携带属性GGSN-Vendor  =  不携带该信元。
                           支持携带属性GGSN-Version  =  不携带该信元。
                           支持携带属性trigger-type  =  不携带该信元。
                             支持携带属性Served-MDN  =  不携带该信元。
                                     HW-RAI属性开关  =  不携带该信元。
                                NAS-Port-Id属性开关  =  不携带该信元。
                                  NAS-Port-Id属性值  =  UNC
                   UE-Local-IP-Address和UE-UDP-Port  =  不携带该信元。
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RDSACCTREQATTR.md`
