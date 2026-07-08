---
id: UDG@20.15.2@MMLCommand@LST HEADEN
type: MMLCommand
name: LST HEADEN（查询头增强）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HEADEN
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- 头增强
status: active
---

# LST HEADEN（查询头增强）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询头增强全部配置信息，或根据输入名称显示指定头增强的配置信息，查询已加入的头增强功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HEADERENNAME | 头增强名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置头增强名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置头增强的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MSISDN1：指定插入项的类型为MSISDN。<br>- MSISDN2：指定插入项的类型为MSISDN。<br>- MSISDN3：指定插入项的类型为MSISDN。<br>- IMSI1：指定插入项的类型为IMSI。<br>- IMSI2：指定插入项的类型为IMSI。<br>- IMSI3：指定插入项的类型为IMSI。<br>- IMEI1：指定插入项的类型为IMEI。<br>- IMEI2：指定插入项的类型为IMEI。<br>- IMEI3：指定插入项的类型为IMEI。<br>- SGSNIP1：指定插入项的类型为SGSN IP。<br>- SGSNIP2：指定插入项的类型为SGSN IP。<br>- SGSNIP3：指定插入项的类型为SGSN IP。<br>- SUBPROFILE1：指定插入项的类型为Subscriber Profile。<br>- SUBPROFILE2：指定插入项的类型为Subscriber Profile。<br>- SUBPROFILE3：指定插入项的类型为Subscriber Profile。<br>- MSIP1：指定插入项的类型为MS IP。<br>- APN：指定插入项的类型为APN。<br>- ZONEID：指定插入项的类型为Zone ID。<br>- BILLINGTYPE：指定插入项的类型为Billing Type。<br>- CHGCHAR1：指定插入项的类型为Charge Characteristic。<br>- CHGCHAR2：指定插入项的类型为Charge Characteristic。<br>- CHGCHAR3：指定插入项的类型为Charge Characteristic。<br>- RAT1：指定插入项的类型为RAT。<br>- RAT2：指定插入项的类型为RAT。<br>- RAT3：指定插入项的类型为RAT。<br>- ULI1：指定插入项的类型为ULI。<br>- ULI2：指定插入项的类型为ULI。<br>- ULI3：指定插入项的类型为ULI。<br>- CHGID：指定插入项的类型为Charging ID。<br>- ROAMING1：指定插入项的类型为Roaming。<br>- ROAMING2：指定插入项的类型为Roaming。<br>- ROAMING3：指定插入项的类型为Roaming。<br>- SGSN_MCC_MNC1：指定插入项的类型为SGSN MCC MNC。<br>- SGSN_MCC_MNC2：指定插入项的类型为SGSN MCC MNC。<br>- SGSN_MCC_MNC3：指定插入项的类型为SGSN MCC MNC。<br>- USERDEF1：指定插入项的类型为User Defined。<br>- USERDEF2：指定插入项的类型为User Defined。<br>- USERDEF3：指定插入项的类型为User Defined。<br>- USERDEF4：指定插入项的类型为User Defined。<br>- USERPROFALIAS：指定插入项的类型为用户模板别名。<br>- MCC：指定插入项的类型为移动国家码。<br>- MNC：指定插入项的类型为移动网络码。<br>- SESSIONID：指定插入项的类型为用户标识。<br>- GGSNIP1：指定插入项的类型为GGSN IP。<br>- GGSNIP2：指定插入项的类型为GGSN IP。<br>- GGSNIP3：指定插入项的类型为GGSN IP。<br>- TIMESTAMP1：指定插入项的类型为TIMESTAMP。<br>- TIMESTAMP2：指定插入项的类型为TIMESTAMP。<br>- TIMESTAMP3：指定插入项的类型为TIMESTAMP。<br>- MSIP2：指定插入项的类型为MS IP。<br>- MSIP3：指定插入项的类型为MS IP。<br>- UPIPV4：指定插入项的类型为用户面网关逻辑接口的IPv4地址。该逻辑接口地址包含Pa、Sa、N3、S1-U地址之一，按优先级Pa>Sa>N3>S1-U的顺序获取。<br>- UPIPV6：指定插入项的类型为用户面网关逻辑接口的IPv6地址。该逻辑接口地址包含Pa、Sa、N3、S1-U地址之一，按优先级Pa>Sa>N3>S1-U的顺序获取。<br>- RANDNUM：指定插入项的类型为RANDNUM，该随机数作为加密算法MD5/SHA256盐值使用。<br>- MULTIPARA1：指定插入项的类型为多参数类型。<br>- MULTIPARA2：指定插入项的类型为多参数类型。<br>- MULTIPARA3：指定插入项的类型为多参数类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HEADEN]] · 头增强（HEADEN）

## 使用实例

- 假如运营商想查看名称为“headen1”，插入数据类型为“MSISDN1”的头增强记录：
  ```
  LST HEADEN: HEADERENNAME="headen1", DATATYPE=MSISDN1;
  ```
  ```

  RETCODE = 0  操作成功

  头增强信息
  ----------
                                                 头增强名称  =  headen1
                                                   数据类型  =  MSISDN1
                                                   前缀名称  =  test
                                               用户自定义值  =  NULL
                                                   IMEI类型  =  IMEI
                                             错误码前缀名称  =  NULL
                                               加密算法标识  =  AES128，有安全风险，不建议使用
                                                       密钥  =  *****
                                                 防欺诈标识  =  不使能（关闭）
                                                   头域长度  =  31
                                         需去除的移动国家码  =  NULL
                                            RSA2048公钥名称  =  NULL
                                            RSA2048加密方式  =  STAT
  RSA2048加密明文填充模式，推荐使用RSA_PKCS1_OAEP_PADDING。  =  RSA_PKCS1_PADDING，有安全风险，不建议使用
                                            RSA1024公钥名称  =  NULL
                                            RSA1024加密方式  =  STAT
  RSA1024加密明文填充模式，推荐使用RSA_PKCS1_OAEP_PADDING。  =  RSA_PKCS1_PADDING，有安全风险，不建议使用
                                            RSA3072公钥名称  =  NULL
                                            RSA3072加密方式  =  STAT
  RSA3072加密明文填充模式，推荐使用RSA_PKCS1_OAEP_PADDING。  =  RSA_PKCS1_PADDING，有安全风险，不建议使用
                                             是否添加盐值  =  使能
                                                   时间精度  =  秒
                                  Charge Characteristic格式  =  十进制
                                                     灰名单  =  不使能（关闭）
                                  RC4的密钥MD5 Hash使能标识  =  继承
                                         头增强密文编码方式  =  继承
                                         头增强等号替换标识  =  不替换
                                       头增强等号替换字符串  =  NULL
                                       头增强斜杠替换字符串  =  NULL
                                       头增强加号替换字符串  =  NULL
                                                 配置域名称  =  NULL
                                            参数1的数据类型  =  NONE
                                            参数2的数据类型  =  NONE
                                            参数3的数据类型  =  NONE
                                           多参数拼接分隔符  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商想查看所有的头增强记录：
  ```
  LST HEADEN:;
  ```
  ```

  RETCODE = 0  操作成功

  头增强信息
  ----------
  头增强名称  数据类型  前缀名称  用户自定义值  IMEI类型  错误码前缀名称  加密算法标识 密钥   防欺诈标识      头域长度  需去除的移动国家码  RSA2048公钥名称  RSA2048加密方式  RSA2048加密明文填充模式，推荐使用RSA_PKCS1_OAEP_PADDING。  RSA1024公钥名称  RSA1024加密方式  RSA1024加密明文填充模式，推荐使用RSA_PKCS1_OAEP_PADDING。  RSA3072公钥名称  RSA3072加密方式  RSA3072加密明文填充模式，推荐使用RSA_PKCS1_OAEP_PADDING。  是否添加盐值  时间精度  Charge Characteristic格式  灰名单          RC4的密钥MD5 Hash使能标识  头增强密文编码方式  头增强等号替换标识  头增强等号替换字符串  头增强斜杠替换字符串  头增强加号替换字符串  配置域名称  参数1的数据类型  参数2的数据类型  参数3的数据类型  多参数拼接分隔符  
                                                                                              
  headen1     MSISDN1   test1     NULL          IMEI      NULL            AES128，有安全风险，不建议使用      *****  不使能（关闭）  31        NULL                NULL             STAT             RSA_PKCS1_PADDING，有安全风险，不建议使用                  NULL             STAT             RSA_PKCS1_PADDING，有安全风险，不建议使用            NULL             STAT             RSA_PKCS1_PADDING，有安全风险，不建议使用                  使能          秒        十进制                     不使能（关闭）  继承                       继承                不替换              NULL                  NULL                  NULL                  NULL        NONE             NONE             NONE             NULL              
  headen2     MSISDN2   test2     NULL          IMEI      NULL            AES128，有安全风险，不建议使用      *****  不使能（关闭）  31        NULL                NULL             STAT             RSA_PKCS1_PADDING，有安全风险，不建议使用                  NULL             STAT             RSA_PKCS1_PADDING，有安全风险，不建议使用            NULL             STAT             RSA_PKCS1_PADDING，有安全风险，不建议使用                  使能          秒        十进制                     不使能（关闭）  继承                       继承                不替换              NULL                  NULL                  NULL                  NULL        NONE             NONE             NONE             NULL              
  (结果个数 = 2
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询头增强（LST-HEADEN）_86527861.md`
