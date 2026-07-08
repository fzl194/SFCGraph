# 删除EDNS（RMV EDNS）

- [命令功能](#ZH-CN_CONCEPT_0283909786__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0283909786__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0283909786__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0283909786__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0283909786__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0283909786)

**适用NF：PGW-U、UPF**

该命令用来删除EDNS的相关配置。用于取消用户相应的EDNS配置。

#### [注意事项](#ZH-CN_CONCEPT_0283909786)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0283909786)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0283909786)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EDNSNAME | EDNS名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置EDNS的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置EDNS的数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MSISDN1：指定插入项的类型为MSISDN。<br>- MSISDN2：指定插入项的类型为MSISDN。<br>- MSISDN3：指定插入项的类型为MSISDN。<br>- IMSI1：指定插入项的类型为IMSI。<br>- IMSI2：指定插入项的类型为IMSI。<br>- IMSI3：指定插入项的类型为IMSI。<br>- IMEI1：指定插入项的类型为IMEI。<br>- IMEI2：指定插入项的类型为IMEI。<br>- IMEI3：指定插入项的类型为IMEI。<br>- DNN：指定插入项的类型为DNN。<br>- RAT1：指定插入项的类型为RAT。<br>- RAT2：指定插入项的类型为RAT。<br>- RAT3：指定插入项的类型为RAT。<br>- ULI1：指定插入项的类型为ULI。<br>- ULI2：指定插入项的类型为ULI。<br>- ULI3：指定插入项的类型为ULI。<br>- USERDEF1：指定插入项的类型为用户自定义类型。<br>- USERDEF2：指定插入项的类型为用户自定义类型。<br>- USERDEF3：指定插入项的类型为用户自定义类型。<br>- USERDEF4：指定插入项的类型为用户自定义类型。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0283909786)

假如运营商想删除名称为“edns1”，DataType为USERDEF1的EDNS记录：

```
RMV EDNS: EDNSNAME="edns1", DATATYPE=USERDEF1;
```
