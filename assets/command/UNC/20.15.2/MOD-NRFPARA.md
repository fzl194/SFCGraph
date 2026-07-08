---
id: UNC@20.15.2@MMLCommand@MOD NRFPARA
type: MMLCommand
name: MOD NRFPARA（修改NRF协议参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NRFPARA
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
- CBCF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF参数管理
- NRF配置参数管理
status: active
---

# MOD NRFPARA（修改NRF协议参数）

## 功能

![](修改NRF协议参数（MOD NRFPARA）_09652973.assets/notice_3.0-zh-cn_2.png)

OAUTH2SWITCH配置为ON时，如果端到端不支持OAUTHTOKEN功能，可能会导致业务呼损，建议配置为OFF。

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF**

该命令用于修改NRF协议相关的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTANCENAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：<br>本参数取值与ADD NRF命令中的“NRF实例名称”参数取值保持一致时，关联关系生效。 |
| WAITINTERVAL | 等待时长 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF向NRF发起请求消息后，等待响应的最大时长。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~60，单位是秒。<br>默认值：无<br>配置原则：无 |
| MAXRETRYTIMES | 最大重传次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF等待NRF响应超时后，重新发起请求消息的最大次数。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| HEARTBEATTIMER | 心跳时长 | 可选必选说明：可选参数<br>参数含义：向NRF建议的心跳时长，实际心跳以NRF决策为准。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535，单位是秒。<br>默认值：无<br>配置原则：<br>如果NRF的response中携带心跳时长，以NRF返回的心跳间隔为准。心跳断开后的快速心跳探测周期以WAITINTERVAL为准。 |
| LOADCARRYINHB | 心跳是否携带Load信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在心跳消息中携带NF的Load信息。<br>数据来源：对端协商<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| SUBSCRISWITCH | 订阅流程开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF是否能发起订阅流程。<br>数据来源：全网规划<br>取值范围：<br>- OFF（OFF）<br>- ON（ON）<br>默认值：无<br>配置原则：无 |
| OAUTH2SWITCH | OAUTH2鉴权开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF是否开启Oauth2鉴权。<br>数据来源：全网规划<br>取值范围：<br>- OFF（OFF）<br>- ON（ON）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFPARA]] · NRF协议参数（NRFPARA）

## 使用实例

修改实例名称为NRF_Instance_0的NRF的等待时长为5秒，最大重传次数为3次，打开订阅开关，打开OAUTH2开关：

```
MOD NRFPARA: NRFINSTANCENAME="NRF_Instance_0", WAITINTERVAL=5, MAXRETRYTIMES=3, SUBSCRISWITCH=ON, OAUTH2SWITCH=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NRFPARA.md`
