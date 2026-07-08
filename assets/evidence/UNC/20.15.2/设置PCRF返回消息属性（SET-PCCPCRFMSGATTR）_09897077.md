# 设置PCRF返回消息属性（SET PCCPCRFMSGATTR）

- [命令功能](#ZH-CN_CONCEPT_0209897077__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897077__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897077__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897077__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897077__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897077)

**适用NF：PGW-C、SMF**

该命令用于配置激活和更新流程中，UNC是否支持由DRA或PCRF触发的PCRF重选。

如果希望在激活或者更新流程中，UNC根据DRA或者PCRF消息触发的PCRF重选，则可将对应的参数使能。

#### [注意事项](#ZH-CN_CONCEPT_0209897077)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ORGHOSTCCAI | ORGHOSTCCAU | ORGHOSTRAR |
| --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0209897077)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897077)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ORGHOSTCCAI | 基于CCA-I Origin-Host AVP触发PCRF重选 | 可选必选说明：可选参数<br>参数含义：该参数用于设置激活流程中，UNC是否支持由CCA-I中的Origin-Host AVP触发的PCRF重选。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| ORGHOSTCCAU | 基于CCA-U Origin-Host AVP触发PCRF重选 | 可选必选说明：可选参数<br>参数含义：该参数用于设置更新流程中，UNC是否支持由CCA-U中的Origin-Host AVP触发的PCRF重选。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| ORGHOSTRAR | 基于RAR Origin-Host AVP触发PCRF重选 | 可选必选说明：可选参数<br>参数含义：该参数用于设置更新流程中，UNC是否支持由RAR中的Origin-Host AVP触发的PCRF重选。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897077)

如果希望UNC在用户激活和更新流程中支持由DRA或者PCRF触发的PCRF重选，则需要配置激活和更新流程中，UNC支持由DRA或PCRF触发的PCRF重选：

```
SET PCCPCRFMSGATTR: ORGHOSTCCAI=ENABLE,ORGHOSTCCAU=ENABLE,ORGHOSTRAR=ENABLE;
```
