---
id: UDG@20.15.2@MMLCommand@SET MTSCFG
type: MMLCommand
name: SET MTSCFG（设置消息跟踪配置参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: MTSCFG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 消息跟踪
status: active
---

# SET MTSCFG（设置消息跟踪配置参数）

## 功能

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

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 类型 | 可选必选说明：必选参数。<br>参数含义：消息跟踪配置参数的类型。<br>取值范围：<br>- FLOW_CONTROL_SWITCH(跟踪服务资源流控开关)<br>- BASE_SUBHEALTH_SWITCH(跟踪服务Base亚健康消减开关)<br>默认值：无。<br>配置原则：无。 |
| MEID | 网元ID | 可选必选说明：该参数在<br>“类型”<br>配置为<br>“FLOW_CONTROL_SWITCH(跟踪服务资源流控开关)或者BASE_SUBHEALTH_SWITCH(跟踪服务Base亚健康消减开关)”<br>时为条件必选参数。<br>参数含义：标识网元ID。<br>取值范围：0~65535<br>默认值：无。<br>配置原则：可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。 |
| SWITCH | 开关 | 可选必选说明：该参数在<br>“类型”<br>配置为<br>“FLOW_CONTROL_SWITCH(跟踪服务资源流控开关)”<br>或者<br>“BASE_SUBHEALTH_SWITCH(跟踪服务Base亚健康消减开关)”<br>时为条件必选参数。<br>参数含义：跟踪服务配置开关。<br>取值范围：<br>- ON(开启)<br>- OFF(关闭)<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MTSCFG]] · 消息跟踪配置参数（MTSCFG）

## 使用实例

- 设置跟踪服务资源流控状态：
  ```
  SET MTSCFG: TYPE=FLOW_CONTROL_SWITCH, MEID=10, SWITCH=ON;
  ```
  ```
  %%SET MTSCFG: TYPE=FLOW_CONTROL_SWITCH, MEID=10, SWITCH=ON;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  下发成功实例个数  =  2
  下发失败实例个数  =  4
  (结果个数 = 1)

  ---    END
  ```
- 设置base亚健康消减状态：
  ```
  SET MTSCFG: TYPE=BASE_SUBHEALTH_SWITCH, MEID=0, SWITCH=ON;
  ```
  ```
  %%SET MTSCFG: TYPE=BASE_SUBHEALTH_SWITCH, MEID=0, SWITCH=ON;%% 
  RETCODE = 0  操作成功  

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-MTSCFG.md`
