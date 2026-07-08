# 设置L2TP N4密码配置（SET L2TPN4KEY）

- [命令功能](#ZH-CN_CONCEPT_0264015280__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0264015280__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0264015280__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0264015280__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0264015280__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0264015280)

**适用NF：PGW-U、UPF**

![](设置L2TP N4密码配置（SET L2TPN4KEY）_64015280.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，需要与SMF的配置保持一致，否则可能会导致L2TP用户激活失败。

该命令用于配置N4接口L2TP私有信元PCO info和Tunnel info的密钥。

#### [注意事项](#ZH-CN_CONCEPT_0264015280)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置N4KeyValue和CfmN4KeyValue即启用密钥，N4KeyValue和CfmN4KeyValue都输入空格即清空配置关闭密钥。

#### [操作用户权限](#ZH-CN_CONCEPT_0264015280)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0264015280)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| N4KEYVALUE | N4密钥 | 可选必选说明：可选参数<br>参数含义：指定N4密钥。<br>数据来源：本端规划<br>取值范围：密码类型，不加密输入时，取值范围16-30位字符串，只能输入0-9，A-F，不区分大小写，最小16位，最大30位。输入N4KEYVALUE时，必须同时输入确认密码CFMN4KEYVALUE，且密码相同。<br>默认值：无<br>配置原则：无 |
| CFMN4KEYVALUE | 确认N4密钥 | 可选必选说明：可选参数<br>参数含义：该参数用于确认N4密钥。<br>数据来源：本端规划<br>取值范围：密码类型，不加密输入时，取值范围16-30位字符串，CfmN4KeyValue需要和N4KeyValue密码相同。<br>默认值：无<br>配置原则：CFMN4KEYVALUE需要和N4KEYVALUE密码相同。 |

#### [使用实例](#ZH-CN_CONCEPT_0264015280)

启用N4KeyValue密钥，配置密码为“123456789ABCDEF123”：

```
SET L2TPN4KEY: N4KEYVALUE="*****", CFMN4KEYVALUE="*****";
```
