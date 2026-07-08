---
id: UDG@20.15.2@MMLCommand@STP POD
type: MMLCommand
name: STP POD（POD停止）
nf: UDG
version: 20.15.2
verb: STP
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

# STP POD（POD停止）

## 功能

![](POD停止（STP POD）_57196802.assets/notice_3.0-zh-cn.png)

Pod停止运行可能会导致业务受损，请谨慎使用该命令。

该命令用于停止Pod运行。

> **说明**
> - 在第三方场景下不支持该命令。
> - 该命令功能依赖NFV_FusionStage能力，CSP配套NFV_FusionStage 22.1.0及之后的版本，支持该命令，配套其它版本执行该命令不生效或执行失败。

> **说明**
> 无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：当前Pod服务所在的网元ID，即应用ID。<br>取值范围：长度不超过40的字符串。<br>默认值：无。<br>配置原则：可以通过MML命令<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。 |
| PODNAME | Pod名称 | 可选必选说明：必选参数。<br>参数含义：Pod名称。<br>取值范围：字符串类型，字符串长度范围为3~100个字符。<br>默认值：无。<br>配置原则：服务实例所在Pod名称。 |
| FORCEFLAG | 强制停止 | 可选必选说明：必选参数。<br>参数含义：是否强制停止标志位。<br>取值范围：<br>- false(非强制停止)<br>- true(强制停止)<br>默认值：无。<br>配置原则：<br>- 强制停止Pod：只校验Pod是否存在，如果存在则下发Pod停止命令。<br>- 非强制停止Pod：有防呆处理，按照Pod类型分别执行下面操作：- StatefulSet类型：需要保证停止完后该类型Pod有一半以上处于Running状态。<br>- Deployment类型：需要保证停止完后该类型Pod至少有一个处于Running状态。<br>- DaemonSet类型：该类型Pod不支持非强制停止。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@POD]] · POD停止（POD）

## 使用实例

1. 执行停止Pod成功，其中“网元ID”为“0”，“Pod名称”为“zookeeper-0”，非强制停止。
  STP POD: MEID="0", PODNAME="zookeeper-0", FORCEFLAG=false;

  ```
  %%STP POD: MEID="0", PODNAME="zookeeper-0", FORCEFLAG=false;%%
  RETCODE = 0  操作成功

  ---    END
  ```
2. 执行停止Pod失败，其中“网元ID”为“0”，“Pod名称”为“zookeeper-5”，非强制停止。
  STP POD: MEID="0", PODNAME="zookeeper-5", FORCEFLAG=false;

  ```
  %%STP POD: MEID="0", PODNAME="zookeeper-5", FORCEFLAG=false;%%
  RETCODE = 140041  启停Pod不存在。

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/STP-POD.md`
