---
id: UDG@20.15.2@MMLCommand@RMV MTSPOLICY
type: MMLCommand
name: RMV MTSPOLICY（删除消息跟踪限制）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MTSPOLICY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 消息跟踪
status: active
---

# RMV MTSPOLICY（删除消息跟踪限制）

## 功能

![](删除消息跟踪限制（RMV MTSPOLICY）_19414949.assets/notice_3.0-zh-cn.png)

执行该命令后，会删除对消息跟踪能力的限制，请谨慎使用该命令。

本命令用于删除对消息跟踪能力的限制。

> **说明**
> - 请勿同时执行本命令和批量删除任务，否则可能会导致本次批量删除部分任务失败。请在批量删除任务流程结束后再执行本命令。
> - 当用户执行本命令时，若仅选择“网元ID”与“规则类型”，将删除当前“规则类型”下的所有策略限制，请谨慎操作。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535<br>默认值：无。<br>配置原则：无。 |
| POLICYTYPE | 规则类型 | 可选必选说明：必选参数。<br>参数含义：限制消息跟踪的规则类型。<br>取值范围：<br>- DISABLE_BY_TYPE(限制跟踪类型)<br>- DISABLE_BY_SERVICE(限制服务名称)<br>默认值：无。<br>配置原则：无。 |
| TRACETYPE | 跟踪类型 | 可选必选说明：该参数在<br>“规则类型”<br>配置为<br>“DISABLE_BY_TYPE(限制跟踪类型)”<br>或<br>“DISABLE_BY_SERVICE(限制服务名称)”<br>时为条件可选参数。<br>参数含义：跟踪类型，可以通过<br>[**DSP MTSMODEL**](查询消息跟踪模型（DSP MTSMODEL）_83186620.md)<br>命令查询获取。<br>取值范围：整数类型，取值范围0~2147483647。<br>默认值：无。<br>配置原则：<br>- 当“规则类型”配置为“DISABLE_BY_TYPE(限制跟踪类型)”时，本参数需要与[**DSP MTSMODEL**](查询消息跟踪模型（DSP MTSMODEL）_83186620.md)命令的“跟踪类型”输出项保持一致。如果不填写本参数，执行命令时将删除所有跟踪类型的策略限制。<br>- “规则类型”配置为“DISABLE_BY_SERVICE(限制服务名称)”时，本参数需要与[**DSP MTSMODEL**](查询消息跟踪模型（DSP MTSMODEL）_83186620.md)命令的“拓展跟踪类型”输出项保持一致。如果不填写“跟踪类型”与“服务名称”，执行命令时将删除当前“规则类型”下的所有策略限制。 |
| SERVICENAME | 服务名称 | 可选必选说明：该参数在<br>“规则类型”<br>配置为<br>“DISABLE_BY_SERVICE(限制服务名称)”<br>时为条件可选参数。<br>参数含义：跟踪类型，可以通过<br>[**DSP MTSMODEL**](查询消息跟踪模型（DSP MTSMODEL）_83186620.md)<br>命令查询获取。<br>取值范围：字符串类型，长度为0~512。<br>默认值：无。<br>配置原则：一次配置仅支持单个服务。如果不填写<br>“跟踪类型”<br>与<br>“服务名称”<br>，执行命令时将删除当前<br>“规则类型”<br>下的所有策略限制。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MTSPOLICY]] · 消息跟踪限制（MTSPOLICY）

## 使用实例

1. 删除跟踪类型消息限制：
  ```
  %%RMV MTSPOLICY: MEID=10, POLICYTYPE=DISABLE_BY_TYPE, TRACETYPE=1005;%%
  RETCODE = 0  操作成功
  ---    END
  ```
2. 删除指定服务消息限制：
  ```
  %%RMV MTSPOLICY: MEID=12, POLICYTYPE=DISABLE_BY_SERVICE, SERVICENAME="A";%%
  RETCODE = 0  操作成功
  ---    END
  ```
3. 删除指定跟踪类型下某个服务的消息限制：
  ```
  %%RMV MTSPOLICY: MEID=12, POLICYTYPE=DISABLE_BY_SERVICE, SERVICENAME="A", TRACETYPE=1;%%
  RETCODE = 0  操作成功
  ---    END
  ```
4. 删除指定跟踪类型下全部订阅服务的消息限制：
  ```
  %%RMV MTSPOLICY: MEID=12, POLICYTYPE=DISABLE_BY_SERVICE, TRACETYPE=60904;%%
  RETCODE = 0  操作成功
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-MTSPOLICY.md`
