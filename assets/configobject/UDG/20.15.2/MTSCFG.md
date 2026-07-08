---
id: UDG@20.15.2@ConfigObject@MTSCFG
type: ConfigObject
name: MTSCFG（消息跟踪配置参数）
nf: UDG
version: 20.15.2
object_name: MTSCFG
object_kind: global_setting
status: active
---

# MTSCFG（消息跟踪配置参数）

## 说明

![](设置消息跟踪配置参数（SET MTSCFG）_75263640.assets/notice_3.0-zh-cn.png)

执行该命令会改变消息跟踪的配置，会对消息跟踪造成影响：当选择 “FLOW_CONTROL_SWITCH” 类型并执行时，可能会影响到跟踪任务的消息上报；当选择 “BASE_SUBHEALTH_SWITCH” 类型并执行时，可能会影响跟踪任务创建与任务运行，请慎重执行。

本命令用于设置消息跟踪的配置参数。

> **说明**
> - 当参数“TYPE”选择“FLOW_CONTROL_SWITCH”类型并执行时，会返回成功与失败的实例个数，如果存在失败的实例，可以选择重试或者联系华为技术支持处理。
> - 当参数“TYPE”选择“BASE_SUBHEALTH_SWITCH”类型将“开关”设置为“开启”，环境上存在“ALM-221257862 资源单元Base平面亚健康告警”，告警定位信息中本端不含OM_RU，对端为主OM_RU，平面ID=0，且运行中的大颗粒接口跟踪任务对应的跟踪类型配置了资源单元Base平面亚健康告警检测，10分钟后该任务会自动停止，并且不允许创建修改该类型的跟踪任务。
> - 该命令存在系统初始值，系统初始值如下：
>   *表1 初始值列表*
>
>   | 类型 | 开关 |
>   | --- | --- |
>   | FLOW_CONTROL_SWITCH(跟踪服务资源流控开关) | ON(开启) |
>   | BASE_SUBHEALTH_SWITCH(跟踪服务base亚健康消减开关) | OFF(关闭) |

## 操作本对象的命令

- [LST MTSCFG](command/UDG/20.15.2/LST-MTSCFG.md)
- [SET MTSCFG](command/UDG/20.15.2/SET-MTSCFG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询消息跟踪配置参数（LST-MTSCFG）_11983805.md`
- 原始手册：`evidence/UDG/20.15.2/设置消息跟踪配置参数（SET-MTSCFG）_75263640.md`
