---
id: UNC@20.15.2@MMLCommand@LST RDSACCTREQVSA
type: MMLCommand
name: LST RDSACCTREQVSA（查询RADIUS计费服务器组的私有扩展属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RDSACCTREQVSA
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
- 扩展信元控制
status: active
---

# LST RDSACCTREQVSA（查询RADIUS计费服务器组的私有扩展属性）

## 功能

**适用NF：PGW-C、SMF**

该命令用来显示指定RADIUS服务器组的RADIUS计费3gpp和3gpp2私有扩展属性的配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | RADIUS Server Group名称 | 可选必选说明：可选参数<br>参数含义：RADIUS服务器组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RDSACCTREQVSA]] · RADIUS计费服务器组的私有扩展属性（RDSACCTREQVSA）

## 使用实例

查询名为“radiusgroup”的RADIUS服务器组的Radius计费3gpp和3gpp2私有扩展属性信息：

```
%%LST RDSACCTREQVSA:RDSSVRGRPNAME="radiusgroup";
```

```
%%
RETCODE = 0  操作成功

RADIUS计费请求消息私有扩展属性
------------------------------
                     RADIUS Server Group名称  =  radiusgroup
                        支持3gpp私有扩展属性  =  支持
                           携带3GPP-IMSI属性  =  不携带该字段
                    携带3GPP-Charging-ID属性  =  携带该字段
                       携带3GPP-PDP-Type属性  =  携带该字段
                     携带3GPP-CG-Address属性  =  携带该字段
携带3GPP-GPRS-Negotiated-QoS-Profile扩展属性  =  携带该字段
                携带3GPP-SGSN（SGW）-Address  =  携带该字段
                   携带3GPP-GGSN-Address信元  =  携带该字段
                        携带IMSI-MCC-MNC信元  =  携带该字段
                        携带GGSN-MCC-MNC信元  =  携带该字段
                          携带3GPP-NSAPI属性  =  携带该字段
                 携带3GPP-Selection-Mode属性  =  携带该字段
       携带3GPP-Charging-Characteristics属性  =  携带该字段
             携带SGSN（SGW）-MCC-MNC扩展属性  =  携带该字段
                          携带IMEISV扩展属性  =  携带该字段
 Accouting Interim消息是否携带IMEISV扩展属性  =  不携带该字段
    Accouting Stop消息是否携带IMEISV扩展属性  =  不携带该字段
                   携带3GPP-RAT-Type扩展属性  =  携带该字段
              携带User-Location-Info扩展属性  =  携带该字段
                    携带3GPP-MS-TimeZone属性  =  携带该字段
                  携带stop-indicator扩展属性  =  携带该字段
                携带3GPP-Negotiated-DSCP属性  =  携带该字段
                   携带packet-filter扩展属性  =  携带该字段
              携带3GPP-SGSN-IPv6-Address属性  =  携带该字段
              携带3GPP-GGSN-IPv6-Address属性  =  携带该字段
                         携带twan-id扩展属性  =  不携带该字段
                       支持3gpp2私有扩展属性  =  支持
                      携带3gpp2-bsid私有属性  =  不携带该字段
                携带3GPP-CG-IPv6-Address属性  =  不携带该字段
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RDSACCTREQVSA.md`
