---
id: UDG@20.15.2@MMLCommand@RST POD
type: MMLCommand
name: RST POD（POD复位）
nf: UDG
version: 20.15.2
verb: RST
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

# RST POD（POD复位）

## 功能

![](POD复位（RST POD）_69830278.assets/notice_3.0-zh-cn.png)

- Pod复位命令会删除并重建Pod，可能会导致业务受损，请确认是否继续操作。
- 下文所有的“复位”，表示对Pod进行重建。
- 按照Pod名称进行非强制复位时，建议同类型下的Pod需要间隔一分钟再执行，否则上次执行创建的POD未Running导致本次可能不生效。
- 在5G中心裸机场景，按照Pod名称进行Super Pod复位时，该Super Pod下的所有Mini Pod都会被复位。
- 在5G中心裸机场景，按照Pod类型进行强制复位时，当类型是"vnode"时，该网元下属于vnode类型的Super Pod都会被复位，即该网元下的所有Mini Pod都会被复位。

本命令用于对指定的Pod进行复位。

## 注意事项

- 根据Pod类型进行复位操作时，只支持强制复位；复位向此微服务注册的Pod（此类型Pod复位时需要先回调Pod注册的URL）时无此限制。
- RST POD是异步操作，实际复位结果可能存在一定时间的延迟，延迟时间小于2分钟。
- 执行RST POD命令后，等待不超过5分钟，再执行DSP POD命令，可以查看Pod状态，当“Pod状态”为“Running”时，表示POD复位成功。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数<br>参数含义：复位Pod服务所在的网元ID，即应用ID。<br>取值范围：长度不超过40的字符串。<br>默认值：无。<br>配置原则：可以通过MML命令“LST ME”获取。 |
| TYPE | Pod复位类型 | 可选必选说明：必选参数<br>参数含义：复位Pod的方式。<br>取值范围：<br>- byId(Pod名称)<br>- byType(Pod类型)<br>默认值：无。<br>配置原则：无。 |
| PODNAME | Pod名称 | 可选必选说明：该参数在<br>“Pod复位类型”<br>取值为<br>“Pod名称”<br>时为必选参数。<br>参数含义：Pod名称。<br>取值范围：字符串类型，字符串长度范围为3~100个字符。<br>默认值：无。<br>配置原则：<br>- 服务实例所在Pod名称，该参数仅在“Pod复位类型”取值为“Pod名称”时有效。<br>- 可以通过执行MML命令[**DSP POD**](POD查询（DSP POD）_69830277.md)时不输入“网元ID”且不选择“Pod查询类型”获取所有的“Pod名称”列表。<br>- 该参数不支持在“Pod名称”列表中模糊匹配复位。 |
| PODTYPE | Pod类型 | 可选必选说明：该参数在<br>“Pod复位类型”<br>取值为<br>“Pod类型”<br>时为必选参数。<br>参数含义：Pod类型。<br>取值范围：字符串类型，字符串长度范围为3~100个字符。<br>默认值：无。<br>配置原则：<br>- 该参数仅在“Pod复位类型”取值为“Pod类型”时有效。<br>- 可以通过执行MML命令[**DSP POD**](POD查询（DSP POD）_69830277.md)时不输入“网元ID”且不选择“Pod查询类型”获取所有的“Pod类型”列表。<br>- 该参数不支持在“Pod类型”列表中模糊匹配复位。 |
| FORCEFLAG | 强制复位 | 可选必选说明：必选参数<br>参数含义：强制复位标识。<br>取值范围：<br>- false(非强制复位)<br>- true(强制复位)<br>默认值：无。<br>配置原则：<br>- 强制复位：适合于任何场景，可能会影响到业务。<br>- 非强制复位：- 不支持根据pod类型复位<br>- 根据pod名称的非强制复位，会有提示信息说明。防呆分为3种情况，解释如下：<br>（1）StatefulSet：需要保证复位完后该类型pod有一半以上处于Running状态。<br>（2）Deployment：需要保证复位完后该类型pod至少有一个处于Running状态。<br>（3）DaemonSet：该类型pod不支持非强制复位。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@POD]] · POD停止（POD）

## 使用实例

1. 根据Pod名称复位Pod。
  ```
  %%RST POD:MEID="0", TYPE=byId, PODNAME="runlog-676d4f665c-qrmz6", FORCEFLAG=true;%% 
  RETCODE = 0 操作成功，RST POD是异步操作，实际复位结果可能存在一定时间的延迟，延迟时间小于2分钟。
  ---    END
  ```
2. 根据Pod类型复位Pod。
  ```
  %%RST POD:MEID="0", TYPE=byType, PODTYPE="runlog", FORCEFLAG=true;%% 
  RETCODE = 0 操作成功，RST POD是异步操作，实际复位结果可能存在一定时间的延迟，延迟时间小于2分钟。
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RST-POD.md`
