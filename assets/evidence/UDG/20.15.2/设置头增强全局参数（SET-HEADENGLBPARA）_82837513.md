# 设置头增强全局参数（SET HEADENGLBPARA）

- [命令功能](#ZH-CN_CONCEPT_0182837513__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837513__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837513__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837513__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837513__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837513)

**适用NF：PGW-U、UPF**

该命令用于设置头增强全局参数。

#### [注意事项](#ZH-CN_CONCEPT_0182837513)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RC4KEYMD5EN | MSISDNMINLEN | RSANODEAGETIME | RSAEXPIREDALM | RSACERTEXPALMDAYS | HEADENSALTTYPE |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 0 | 10 | ENABLE | 30 | RANDNUM |

#### [操作用户权限](#ZH-CN_CONCEPT_0182837513)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837513)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RC4KEYMD5EN | RC4的密钥MD5 Hash使能标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置RC4的密钥MD5 Hash使能标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能，RC4加密前不需要做一次MD5加密。<br>- ENABLE：使能，RC4加密前需要做一次MD5加密。<br>默认值：无<br>配置原则：无 |
| MSISDNMINLEN | MSISDN字段最小长度 | 可选必选说明：可选参数<br>参数含义：该参数用于设置头增强功能去除国家码之后MSISDN字段最小长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～17。<br>默认值：无<br>配置原则：无 |
| RSANODEAGETIME | RSA加密节点老化时间（分） | 可选必选说明：可选参数<br>参数含义：该参数用于设置RSA加密节点的老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1440，单位是分钟。<br>默认值：无<br>配置原则：无 |
| RSAEXPIREDALM | RSA证书过期告警 | 可选必选说明：可选参数<br>参数含义：该参数用于配置RSA证书文件过期告警开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：无 |
| RSACERTEXPALMDAYS | RSA证书过期告警提前天数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置RSA证书过期告警提前天数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～365，单位是天。<br>默认值：无<br>配置原则：无 |
| HEADENSALTTYPE | 头增强插入盐值生成方法类型 | 可选必选说明：可选参数<br>参数含义：头增强盐值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RANDNUM：使用随机数生成盐值。<br>- TIMESTAMP：使用时间戳生成盐值，有安全风险，不建议使用。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837513)

假如运营商需要设置MSISDN字段最小长度为1：

```
SET HEADENGLBPARA: MSISDNMINLEN=1;
```
