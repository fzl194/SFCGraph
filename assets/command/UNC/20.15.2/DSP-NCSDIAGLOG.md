---
id: UNC@20.15.2@MMLCommand@DSP NCSDIAGLOG
type: MMLCommand
name: DSP NCSDIAGLOG（显示会话中NETCONF和其它组件的消息交互信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCSDIAGLOG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议
status: active
---

# DSP NCSDIAGLOG（显示会话中NETCONF和其它组件的消息交互信息）

## 功能

该命令用于显示会话中NETCONF和其它组件的消息交互信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SESSIONHISTORY：历史信息。<br>- STCOVERTIME：超时信息。<br>- MESSAGE：消息信息。<br>- SESSIONFSM：状态机信息。<br>- STCPERFORMANCE：性能信息。<br>- ERRORMESSAGE：错误信息。<br>- INNERMESSAGE：内部信息。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCSDIAGLOG]] · 会话中NETCONF和其它组件的消息交互信息（NCSDIAGLOG）

## 使用实例

显示会话中NETCONF和其它组件的消息交互信息：

```
DSP NCSDIAGLOG:DATATYPE=SESSIONHISTORY
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
输出字符串                                                                                       

---------------------------------------------------------------------------------------------------
Time            SessionState         ChannelID  SessionID User           Terminal                  
---------------------------------------------------------------------------------------------------
21/17:19:37:213 create-session       0x00020c81 0x0000    admin          192.168.0.1   
21/17:19:37:213 session-updated      0x00020c81 0x0057    admin          192.168.0.1  
21/17:29:39:297 caml-forced-close    0x00020c81 0x0057    admin          192.168.0.1   
21/17:55:39:635 create-session       0x00020c8c 0x0000    admin          192.168.0.1   
21/17:55:39:635 session-updated      0x00020c8c 0x014f    admin          192.168.0.1   
21/17:56:04:589 caml-forced-close    0x00020c8c 0x014f    admin          192.168.0.1   
21/17:56:08:822 create-session       0x00020c8e 0x0000    admin          192.168.0.1  
21/17:56:08:822 session-updated      0x00020c8e 0x0157    admin          192.168.0.1   
 
(结果个数 = 11)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示会话中NETCONF和其它组件的消息交互信息（DSP-NCSDIAGLOG）_59103623.md`
