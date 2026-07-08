---
id: UNC@20.15.2@MMLCommand@CLR ACSDATA
type: MMLCommand
name: CLR ACSDATA（清除ACS管理服务数据）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: ACSDATA
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 维护管理
status: active
---

# CLR ACSDATA（清除ACS管理服务数据）

## 功能

![](清除ACS管理服务数据(CLR ACSDATA)_98165797.assets/notice_3.0-zh-cn_2.png)

该命令将清除ACS管理服务的数据并导致业务中断，需谨慎执行。

该命令用于清除ACS管理服务数据。

## 注意事项

- 该命令执行后，对应的服务会在3分钟内无法通过ACS进行配置管理，3分钟后服务开始向ACS进行注册，注册成功后恢复该服务的配置管理业务。
- 当执行该命令删除服务数据后，若对应的服务发生重启，则会重新向ACS注册，注册成功后恢复该服务的配置管理业务。
- 当执行该命令后，若ACS发生重启、主备倒换等操作，所有服务重新向ACS进行注册，注册成功后恢复所有服务的配置管理业务。
- 该命令在清除ACS管理服务的数据时，仅清除微服务在ACS中的数据。
- 命令执行后，需要通过**DSP ACSSYNCINFO**查询对应微服务是否清理完成。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| CLEARTYPE | 清除模式 | 可选必选说明：可选参数。<br>参数含义：用于指定清除相应服务在ACS数据的清除模式。<br>取值范围：枚举类型。<br>- all(全部)：清除所有服务数据。<br>- podName(Pod名称)：根据Pod名称匹配服务，并清除相应服务在ACS中的数据。<br>- podType(Pod类型)：根据Pod类型匹配服务，并清除相应服务在ACS中的数据。<br>默认值：all(全部)。 |
| PODNAME | Pod名称 | 可选必选说明：条件可选参数。当参数<br>“清除模式(CLEARTYPE)”<br>选择<br>“podName(Pod名称)”<br>时，该参数有效。<br>参数含义：用于指定需要清除ACS数据的服务所在Pod的Pod名称（可通过<br>**DSP POD**<br>查询获得该参数）。<br>取值范围：长度不超过100的字符串。<br>默认值：无。 |
| PODTYPE | Pod类型 | 可选必选说明：条件可选参数。当参数<br>“清除模式(CLEARTYPE)”<br>选择<br>“podType(Pod类型)”<br>时，该参数有效。<br>参数含义：用于指定需要清除ACS数据的服务所在Pod的Pod类型（可通过<br>**DSP POD**<br>查询获得该参数）。<br>取值范围：长度不超过100的字符串。<br>默认值：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ACSDATA]] · ACS管理服务数据（ACSDATA）

## 使用实例

清除所有服务数据场景，执行以下命令：

```
CLR ACSDATA: CLEARTYPE=all;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-ACSDATA.md`
