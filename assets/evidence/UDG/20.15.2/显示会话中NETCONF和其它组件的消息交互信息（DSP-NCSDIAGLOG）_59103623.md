# 显示会话中NETCONF和其它组件的消息交互信息（DSP NCSDIAGLOG）

- [命令功能](#ZH-CN_CONCEPT_0259103623__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0259103623__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0259103623__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0259103623__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0259103623__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0259103623__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0259103623)

该命令用于显示会话中NETCONF和其它组件的消息交互信息。

#### [注意事项](#ZH-CN_CONCEPT_0259103623)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0259103623)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0259103623)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SESSIONHISTORY：历史信息。<br>- STCOVERTIME：超时信息。<br>- MESSAGE：消息信息。<br>- SESSIONFSM：状态机信息。<br>- STCPERFORMANCE：性能信息。<br>- ERRORMESSAGE：错误信息。<br>- INNERMESSAGE：内部信息。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0259103623)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0259103623)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 输出字符串 | NETCONF会话历史。 |
