# 查询EDNS（LST EDNS）

- [命令功能](#ZH-CN_CONCEPT_0283909787__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0283909787__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0283909787__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0283909787__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0283909787__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0283909787__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0283909787)

**适用NF：PGW-U、UPF**

该命令用于查询EDNS全部配置信息，或根据输入名称显示指定EDNS的配置信息，查询已加入的EDNS功能。

#### [注意事项](#ZH-CN_CONCEPT_0283909787)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0283909787)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0283909787)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EDNSNAME | EDNS名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置EDNS的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置EDNS的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MSISDN1：指定插入项的类型为MSISDN。<br>- MSISDN2：指定插入项的类型为MSISDN。<br>- MSISDN3：指定插入项的类型为MSISDN。<br>- IMSI1：指定插入项的类型为IMSI。<br>- IMSI2：指定插入项的类型为IMSI。<br>- IMSI3：指定插入项的类型为IMSI。<br>- IMEI1：指定插入项的类型为IMEI。<br>- IMEI2：指定插入项的类型为IMEI。<br>- IMEI3：指定插入项的类型为IMEI。<br>- DNN：指定插入项的类型为DNN。<br>- RAT1：指定插入项的类型为RAT。<br>- RAT2：指定插入项的类型为RAT。<br>- RAT3：指定插入项的类型为RAT。<br>- ULI1：指定插入项的类型为ULI。<br>- ULI2：指定插入项的类型为ULI。<br>- ULI3：指定插入项的类型为ULI。<br>- USERDEF1：指定插入项的类型为用户自定义类型。<br>- USERDEF2：指定插入项的类型为用户自定义类型。<br>- USERDEF3：指定插入项的类型为用户自定义类型。<br>- USERDEF4：指定插入项的类型为用户自定义类型。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0283909787)

- 假如运营商想查看名称为“edns1”，插入数据类型为“USERDEF1”的EDNS记录：
  ```
  LST EDNS: EDNSNAME="edns1", DATATYPE=USERDEF1;
  ```
  ```

  RETCODE = 0  操作成功

  EDNS信息
  --------
                                                   EDNS名称  =  edns1
                                                   数据类型  =  USERDEF1
                                   DNS报文中的Option Code值  =  10
                                               用户自定义值  =  test1
                                                   IMEI类型  =  IMEI
                                               加密算法标识  =  AES128_GCM
                                            RSA2048公钥名称  =  NULL
                                            RSA2048加密方式  =  STAT
                                    RSA2048加密明文填充模式  = RSA_PKCS1_PADDIN
                                            RSA3072公钥名称  =  NULL
                                            RSA3072加密方式  =  STAT
                                    RSA3072加密明文填充模式  = RSA_PKCS1_PADDIN
                                                       密钥  =  *****
                                                   确认密钥  =  *****
                                                 配置域名称  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商想查看所有的EDNS记录：
  ```
  LST EDNS:;
  ```
  ```

  RETCODE = 0  操作成功

  EDNS信息
  --------
  EDNS名称  数据类型  DNS报文中的Option Code值  用户自定义值  IMEI类型  加密算法标识  RSA2048公钥名称  RSA2048加密方式  密钥    确认密钥  RSA2048加密明文填充模式  RSA3072公钥名称  RSA3072加密方式  RSA3072加密明文填充模式  配置域名称

  edns1     USERDEF1  10                        test1         IMEI      AES128，有安全风险，不建议使用        NULL             STAT             *****   *****     RSA_PKCS1_PADDIN             NULL             STAT             RSA_PKCS1_PADDIN         NULL
  edns2     USERDEF1  15                        test2         IMEI      AES128，有安全风险，不建议使用        NULL             STAT             *****   *****     RSA_PKCS1_PADDIN             NULL             STAT             RSA_PKCS1_PADDIN         NULL
  (结果个数 = 2)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0283909787)

参见ADD EDNS的参数说明。
