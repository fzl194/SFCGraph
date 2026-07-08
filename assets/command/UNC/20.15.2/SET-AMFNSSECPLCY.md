---
id: UNC@20.15.2@MMLCommand@SET AMFNSSECPLCY
type: MMLCommand
name: SET AMFNSSECPLCY（设置AMF切片安全策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFNSSECPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 5G接入业务管理
- 业务安全管理
- 切片安全策略管理
status: active
---

# SET AMFNSSECPLCY（设置AMF切片安全策略）

## 功能

![](设置AMF切片安全策略（SET AMFNSSECPLCY）_97735773.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，在使用该命令后，AMF将开启跨切片访问保护，需要周边NF都开启该功能，否则业务流程失败，请谨慎使用。

**适用NF：AMF**

该命令用于设置AMF切片安全策略。

## 注意事项

- 该命令执行后立即生效。

- 该命令生效依赖于ADD NRFPARA "OAUTH2鉴权开关"打开，同时对端NRF支持Token授权。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CRONSSECSW |
| --- |
| OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CRONSSECSW | 跨切片访问保护开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否开启AMF跨切片保护功能。开关为"ON"时，作为Consumer，AMF在NF服务发现请求将携带切片向NRF申请Token，并且在后续服务化接口消息中携带获取到的Token。作为Producer，AMF收到服务化接口消息时，将对请求消息进行切片合法性校验，检查不通过时，AMF响应HTTP错误码"400"，原因值"UNSPECIFIED_MSG_FAILURE"。开关为"OFF"时，不进行跨切片保护。AMF进行SMF发现时是否携带切片同时受SET NFSELPLCY命令"请求者网络切片开关"控制，该开关设置为“是”，以SET NFSELPLCY为准，开关设置为“否”时，以本命令为准。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFNSSECPLCY查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFNSSECPLCY]] · AMF切片安全策略（AMFNSSECPLCY）

## 使用实例

打开AMF跨切片访问保护开关，执行如下命令：

```
SET AMFNSSECPLCY: CRONSSECSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置AMF切片安全策略（SET-AMFNSSECPLCY）_97735773.md`
