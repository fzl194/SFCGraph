---
id: UDG@20.15.2@MMLCommand@SET SYSLOGCONTENTCFG
type: MMLCommand
name: SET SYSLOGCONTENTCFG（设置日志内容配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SYSLOGCONTENTCFG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# SET SYSLOGCONTENTCFG（设置日志内容配置）

## 功能

本命令用于设置上报给第三方Syslog服务器的日志内容配置。

> **说明**
> 无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| LOGCONTENTCFG | Syslog报文内容配置 | 可选必选说明：必选参数。<br>参数含义：用于设置上报给第三方Syslog服务器的日志内容配置。<br>取值范围：<br>- CONTENT_APP_NAME(报文头APP-NAME)<br>- CONTENT_IP(报文头IP)<br>默认值：无。<br>配置原则：无。 |
| LOGCONTENTAPPNAME | 报文头APP-NAME | 可选必选说明：该参数在<br>“Syslog报文内容配置”<br>配置为<br>“CONTENT_APP_NAME(报文头APP-NAME)”<br>时为条件必选参数。<br>参数含义：Syslog日志报文头中APP-NAME属性的类型。<br>取值范围：<br>- “LOG_TYPE(日志类型)”：APP-NAME属性显示为具体的日志类型。<br>- “APP_INFO(综合应用信息)”：当日志类型为操作日志、安全日志、OS日志、OS安全日志、事件日志、系统日志时，APP-NAME属性显示为详细应用信息；当日志类型为Web日志、DB日志时，APP-NAME属性显示为“-”；当日志类型为运行日志时，APP-NAME属性不受该参数控制。<br>默认值：APP_INFO(综合应用信息)<br>配置原则：参见<br>[参考信息](#ZH-CN_MMLREF_0000001924521974__relatedinformation30562042172748)<br>进行配置。 |
| LOGCONTENTIPTYPE | 报文头IP | 可选必选说明：该参数在<br>“Syslog报文内容配置”<br>配置为<br>“CONTENT_IP(报文头IP)”<br>时为条件必选参数。<br>参数含义：Syslog日志报文头中IP属性的类型。<br>取值范围：<br>- “NONE(-)”：IP属性显示为“-”。<br>- “VIRTUAL_IP(网元浮动IP)”：IP属性显示为网元浮动IP地址。<br>默认值：VIRTUAL_IP(网元浮动IP)<br>配置原则：参见<br>[参考信息](#ZH-CN_MMLREF_0000001924521974__relatedinformation30562042172748)<br>进行配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SYSLOGCONTENTCFG]] · 日志内容配置（SYSLOGCONTENTCFG）

## 使用实例

```
%%SET SYSLOGCONTENTCFG: LOGCONTENTCFG=CONTENT_IP, LOGCONTENTIPTYPE=VIRTUAL_IP;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置日志内容配置（SET-SYSLOGCONTENTCFG）_24521974.md`
