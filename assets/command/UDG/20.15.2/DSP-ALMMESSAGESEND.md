---
id: UDG@20.15.2@MMLCommand@DSP ALMMESSAGESEND
type: MMLCommand
name: DSP ALMMESSAGESEND（查询告警发送的信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ALMMESSAGESEND
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 告警管理
- 告警发送
status: active
---

# DSP ALMMESSAGESEND（查询告警发送的信息）

## 功能

该命令用于查询告警发送的信息，可以据此定位告警信息是否发送或查询告警信息发送的时间点等其他信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TARGET | 目标 | 可选必选说明：必选参数<br>参数含义：目标组件。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NETCONF：NETCONF组件。<br>默认值：无 |
| TYPE | 消息类型 | 可选必选说明：必选参数<br>参数含义：告警信息的消息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- REPORT-ALARM：告警上报。<br>- GET-ALARM：告警同步。<br>默认值：无 |
| BOARDTYPE | 主控类型 | 可选必选说明：可选参数<br>参数含义：指定主控类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- master：主主控。<br>- slave：备主控。<br>默认值：master |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ALMMESSAGESEND]] · 告警发送的信息（ALMMESSAGESEND）

## 使用实例

- 查询告警上报Notification的信息：
  ```
  DSP ALMMESSAGESEND:TARGET=NETCONF,TYPE=REPORT-ALARM
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
  告警流水号    告警实例号    告警ID     告警状态    告警类别    发送结果    告警产生时间           告警清除时间    告警更新时间   发送时间              会话ID 

  67            428           15794301   活动        故障告警    成功        2022-04-25 09:05:14    NULL            NULL           2022-04-25 09:05:19   63
  68            429           15794301   活动        故障告警    成功        2022-04-25 09:08:14    NULL            NULL           2022-04-25 09:08:19   63
  69            430           15794301   活动        故障告警    成功        2022-04-25 09:11:14    NULL            NULL           2022-04-25 09:11:19   63
  (结果个数 = 3)
  --- END
  ```
- 查询告警同步Notification的信息：
  ```
  DSP ALMMESSAGESEND:TARGET=NETCONF,TYPE=GET-ALARM
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
  发送时间              传输序列号    传输标志位    告警同步流水号        

  2016-05-29 17:53:57   92864591      中间报文      6215,6216,6217,6218,6219,6220,6221,6222,6223,6224,6225,6226,6227,6228      
  2016-05-29 17:53:57   92864592      中间报文      6171,6172,6173,6174,6175,6176,6177,6178,6179,6180,6181,6182,6183,6184,6185 
  (结果个数 = 2)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询告警发送的信息（DSP-ALMMESSAGESEND）_59104023.md`
