# 删除SA指纹识别配置（RMV FINGERIDENT）

- [命令功能](#ZH-CN_CONCEPT_0000202386523551__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202386523551__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202386523551__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202386523551__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202386523551__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202386523551)

**适用NF：PGW-U、UPF**

该命令用来删除SA指纹识别功能配置。

#### [注意事项](#ZH-CN_CONCEPT_0000202386523551)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202386523551)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202386523551)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CFGPROTMODE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于设置协议名称。<br>数据来源：本端规划<br>取值范围：不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGPROTMODE | 协议配置方式 | 可选必选说明：必选参数<br>参数含义：该参数用于设置SA指纹识别功能协议的配置方式。<br>数据来源：本端规划<br>取值范围：<br>- ALL：所有协议。<br>- SPECIFIC：指定协议。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000202386523551)

- 删除所有协议SA指纹识别功能配置，如下：
  ```
  RMV FINGERIDENT: CFGPROTMODE=ALL;
  ```
- 删除Facebook协议SA指纹识别功能配置，如下：
  ```
  RMV FINGERIDENT: CFGPROTMODE=SPECIFIC, PROTOCOLNAME="facebook";
  ```
