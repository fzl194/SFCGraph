# 修改本端NF和对端NRF实例的注册关系（MOD NFREGNRF）

- [命令功能](#ZH-CN_MMLREF_0209651371__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651371__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651371__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651371__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651371)

**适用NF：AMF、SMF、NRF、NSSF、NCG、CBCF**

该命令用于修改本端NF和对端NRF实例的注册关系。

## [注意事项](#ZH-CN_MMLREF_0209651371)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209651371)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651371)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 本端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网元所部署的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NRF（NRF）”：NRF类型<br>- “NON_NRF（non-NRF）”：非NRF类型<br>默认值：无<br>配置原则：<br>该参数需要与ADD NFPROFILE命令配置的本端NF类型一致。 |
| NRFINSTANCENAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端NF所注册的对端NRF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：<br>该参数取自ADD NRF命令配置的NRF实例名称。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于配置本端NF选择指定的NRF实例进行注册的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>该参数值越小，本端NF选择指定NRF实例进行注册的优先级越高。 |
| CAPACITY | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于配置本端NF选择指定的NRF实例进行注册的权重。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>该参数值越大，本端NF选择指定NRF实例进行注册的概率越高。 |

## [使用实例](#ZH-CN_MMLREF_0209651371)

假设本网元仅部署NRF，并且使用ADD NRF配置多个对端NRF实例。本端NRF注册到其中的NRF_Instance_0和NRF_Instance_1，前者的注册优先级高，后者的注册优先级低。如果要调低NRF_Instance_0的注册优先级，则执行如下命令：

```
MOD NFREGNRF: NFTYPE=NRF, NRFINSTANCENAME="NRF_Instance_0", PRIORITY=50;
```
