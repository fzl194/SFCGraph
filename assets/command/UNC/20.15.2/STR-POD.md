---
id: UNC@20.15.2@MMLCommand@STR POD
type: MMLCommand
name: STR POD（POD启动）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: POD
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Pod管理
status: active
---

# STR POD（POD启动）

## 功能

该命令用于启动Pod运行。

> **说明**
> - 在第三方场景下不支持该命令。
> - 该命令功能依赖NFV_FusionStage能力，CSP配套NFV_FusionStage 22.1.0及之后的版本，支持该命令，配套其它版本执行该命令不生效或执行失败。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：当前Pod服务所在的网元ID，即应用ID。<br>取值范围：长度不超过40的字符串。<br>默认值：无。<br>配置原则：可以通过MML命令<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。 |
| PODNAME | Pod名称 | 可选必选说明：必选参数。<br>参数含义：Pod名称。<br>取值范围：字符串类型，字符串长度范围为3~100个字符。<br>默认值：无。<br>配置原则：服务实例所在Pod名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@POD]] · POD停止（POD）

## 使用实例

1. 执行启动Pod成功，其中“网元ID”为“0”，“Pod名称”为“zookeeper-0”。
  STR POD: MEID="0", PODNAME="zookeeper-0";

  ```
  %%STR POD: MEID="0", PODNAME="zookeeper-0";%%
  RETCODE = 0  操作成功

  ---    END
  ```
2. 执行启动Pod失败，其中“网元ID”为“0”，“Pod名称”为“zookeeper-5”。
  STR POD: MEID="0", PODNAME="zookeeper-5";

  ```
  %%STR POD: MEID="0", PODNAME="zookeeper-5";%%
  RETCODE = 140041  启停Pod不存在。

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-POD.md`
