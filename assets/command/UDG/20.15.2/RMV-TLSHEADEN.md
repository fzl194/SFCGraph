---
id: UDG@20.15.2@MMLCommand@RMV TLSHEADEN
type: MMLCommand
name: RMV TLSHEADEN（删除HTTPS头增强）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TLSHEADEN
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- HTTPS头增强
status: active
---

# RMV TLSHEADEN（删除HTTPS头增强）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除HTTPS头增强的相关配置。用于取消用户相应的头增强配置。

## 注意事项

- 该命令执行后立即生效。
- 已经被绑定到RULE命令中的HTTPS头增强不能删除，若需要删除该头增强的信息，需要先执行RMV RULE命令解除绑定关系后，再删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HEADERENNAME | 头增强名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置头增强名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置头增强的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MSISDN1：指定插入项的类型为MSISDN。<br>- MSISDN2：指定插入项的类型为MSISDN。<br>- MSISDN3：指定插入项的类型为MSISDN。<br>- IMSI1：指定插入项的类型为IMSI。<br>- IMSI2：指定插入项的类型为IMSI。<br>- IMSI3：指定插入项的类型为IMSI。<br>- IMEI1：指定插入项的类型为IMEI。<br>- IMEI2：指定插入项的类型为IMEI。<br>- IMEI3：指定插入项的类型为IMEI。<br>- SGSNIP1：指定插入项的类型为SGSN IP。<br>- SGSNIP2：指定插入项的类型为SGSN IP。<br>- SGSNIP3：指定插入项的类型为SGSN IP。<br>- SUBPROFILE1：指定插入项的类型为Subscriber Profile。<br>- SUBPROFILE2：指定插入项的类型为Subscriber Profile。<br>- SUBPROFILE3：指定插入项的类型为Subscriber Profile。<br>- MSIP1：指定插入项的类型为MS IP。<br>- APN：指定插入项的类型为APN。<br>- ZONEID：指定插入项的类型为Zone ID。<br>- BILLINGTYPE：指定插入项的类型为Billing Type。<br>- CHGCHAR1：指定插入项的类型为Charge Characteristic。<br>- CHGCHAR2：指定插入项的类型为Charge Characteristic。<br>- CHGCHAR3：指定插入项的类型为Charge Characteristic。<br>- RAT1：指定插入项的类型为RAT。<br>- RAT2：指定插入项的类型为RAT。<br>- RAT3：指定插入项的类型为RAT。<br>- ULI1：指定插入项的类型为ULI。<br>- ULI2：指定插入项的类型为ULI。<br>- ULI3：指定插入项的类型为ULI。<br>- CHGID：指定插入项的类型为Charging ID。<br>- ROAMING1：指定插入项的类型为Roaming。<br>- ROAMING2：指定插入项的类型为Roaming。<br>- ROAMING3：指定插入项的类型为Roaming。<br>- SGSN_MCC_MNC1：指定插入项的类型为SGSN MCC MNC。<br>- SGSN_MCC_MNC2：指定插入项的类型为SGSN MCC MNC。<br>- SGSN_MCC_MNC3：指定插入项的类型为SGSN MCC MNC。<br>- USERDEF1：指定插入项的类型为User Defined。<br>- USERDEF2：指定插入项的类型为User Defined。<br>- USERDEF3：指定插入项的类型为User Defined。<br>- USERDEF4：指定插入项的类型为User Defined。<br>- USERPROFALIAS：指定插入项的类型为用户模板别名。<br>- MCC：指定插入项的类型为移动国家码。<br>- MNC：指定插入项的类型为移动网络码。<br>- SESSIONID：指定插入项的类型为用户标识。<br>- GGSNIP1：指定插入项的类型为GGSN IP。<br>- GGSNIP2：指定插入项的类型为GGSN IP。<br>- GGSNIP3：指定插入项的类型为GGSN IP。<br>- TIMESTAMP1：指定插入项的类型为TIMESTAMP。<br>- TIMESTAMP2：指定插入项的类型为TIMESTAMP。<br>- TIMESTAMP3：指定插入项的类型为TIMESTAMP。<br>- MSIP2：指定插入项的类型为MS IP。<br>- MSIP3：指定插入项的类型为MS IP。<br>- UPIPV4：指定插入项的类型为用户面网关逻辑接口的IPv4地址。该逻辑接口地址包含Pa、Sa、N3、S1-U地址之一，按优先级Pa>Sa>N3>S1-U的顺序获取。<br>- UPIPV6：指定插入项的类型为用户面网关逻辑接口的IPv6地址。该逻辑接口地址包含Pa、Sa、N3、S1-U地址之一，按优先级Pa>Sa>N3>S1-U的顺序获取。<br>- RANDNUM：指定插入项的类型为RANDNUM，该随机数作为加密算法MD5/SHA256盐值使用。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTPS头增强（TLSHEADEN）](configobject/UDG/20.15.2/TLSHEADEN.md)

## 使用实例

假如运营商想删除名称为“headen1”，数据类型为“MSISDN1”的HTTPS头增强记录：

```
RMV TLSHEADEN:HEADERENNAME="headen1",DATATYPE=MSISDN1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除HTTPS头增强（RMV-TLSHEADEN）_82837523.md`
