---
id: UNC@20.15.2@MMLCommand@ADD MTSPOLICY
type: MMLCommand
name: ADD MTSPOLICY（添加消息跟踪限制）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD MTSPOLICY（添加消息跟踪限制）

## 功能

![](添加消息跟踪限制（ADD MTSPOLICY）_82775284.assets/notice_3.0-zh-cn_2.png)

执行该命令后，可能会影响到跟踪任务的创建以及消息上报，请谨慎使用该命令。

本命令用于添加对消息跟踪能力的限制，例如限制消息跟踪任务的创建。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535<br>默认值：无。<br>配置原则：无。 |
| POLICYTYPE | 规则类型 | 可选必选说明：必选参数。<br>参数含义：限制消息跟踪的规则类型。<br>取值范围：<br>- DISABLE_BY_TYPE(限制跟踪类型)<br>- DISABLE_BY_SERVICE(限制服务名称)<br>默认值：无。<br>配置原则：<br>- 当配置“DISABLE_BY_TYPE(限制跟踪类型)”，此跟踪类型对应的拓展跟踪类型任务会同步限制，已经创建的任务不受影响。<br>- 当配置“DISABLE_BY_SERVICE(限制服务名称)”后，如果系统已存在该服务的消息跟踪任务， 处理建议如下：用户自行决定是否需要提前删除，如果不删除对应任务，跟踪任务校验将会在配置限制后最长6分钟内通知对应服务自动删除任务；并在解除限制后最长6分钟内通知对应服务创建任务。 |
| TRACETYPE | 跟踪类型 | 可选必选说明：<br>- 该参数在“规则类型”配置为“DISABLE_BY_TYPE(限制跟踪类型)”时为条件必选参数。<br>- 该参数在“规则类型”配置为“DISABLE_BY_SERVICE(限制服务名称)”时为条件可选参数。<br>参数含义：跟踪类型，可以通过<br>[**DSP MTSMODEL**](查询消息跟踪模型（DSP MTSMODEL）_83186620.md)<br>命令查询获取。<br>取值范围：整数类型，取值范围0~2147483647<br>默认值：无。<br>配置原则：<br>- 当“规则类型”配置为“DISABLE_BY_TYPE(限制跟踪类型)”时，本参数需要与[**DSP MTSMODEL**](查询消息跟踪模型（DSP MTSMODEL）_83186620.md)命令的“跟踪类型”输出项保持一致。<br>- 当“规则类型”配置为“DISABLE_BY_SERVICE(限制服务名称)”时，本参数需要与[**DSP MTSMODEL**](查询消息跟踪模型（DSP MTSMODEL）_83186620.md)命令的“拓展跟踪类型”输出项保持一致。如果不填写本参数，当前“服务名称”订阅的所有跟踪类型的任务，都将被禁止下发给对应服务。 |
| SERVICENAME | 服务名称 | 可选必选说明：该参数在<br>“规则类型”<br>配置为<br>“DISABLE_BY_SERVICE(限制服务名称)”<br>时为条件必选参数。<br>参数含义：跟踪类型订阅的服务名称，可以通过<br>[**DSP MTSMODEL**](查询消息跟踪模型（DSP MTSMODEL）_83186620.md)<br>命令查询获取。<br>取值范围：字符串类型，长度为0~512。<br>默认值：无。<br>配置原则：一次配置仅支持单个服务。 |

## 操作的配置对象

- [消息跟踪限制（MTSPOLICY）](configobject/UNC/20.15.2/MTSPOLICY.md)

## 使用实例

1. 添加指定跟踪类型的跟踪消息限制：
  ```
  %%ADD MTSPOLICY: MEID=10, POLICYTYPE=DISABLE_BY_TYPE, TRACETYPE=1005;%%
  RETCODE = 0  操作成功
  ---    END
  ```
2. 添加指定跟踪类型下某个订阅服务的跟踪消息限制：
  ```
  %%ADD MTSPOLICY: MEID=12, POLICYTYPE=DISABLE_BY_SERVICE, SERVICENAME="A", TRACETYPE=1;%%
  RETCODE = 0  操作成功
  ---    END
  ```
3. 添加指定某个订阅服务的跟踪消息限制：
  ```
  %%ADD MTSPOLICY: MEID=12, POLICYTYPE=DISABLE_BY_SERVICE, SERVICENAME="A";%%
  RETCODE = 0  操作成功
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/添加消息跟踪限制（ADD-MTSPOLICY）_82775284.md`
