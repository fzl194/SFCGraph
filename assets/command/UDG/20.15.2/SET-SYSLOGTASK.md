---
id: UDG@20.15.2@MMLCommand@SET SYSLOGTASK
type: MMLCommand
name: SET SYSLOGTASK（设置上报任务）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SYSLOGTASK
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# SET SYSLOGTASK（设置上报任务）

## 功能

![](设置上报任务（SET SYSLOGTASK）_36611107.assets/notice_3.0-zh-cn.png)

该命令为高危命令，设置Syslog任务参数，可能存在安全风险及影响Syslog服务器通信，具体参考参数说明，请谨慎执行。

本命令用于增加或者修改向Syslog服务端上报任务。

与 OM Portal 界面 “ 系统 > Syslog管理 ” 中配置作用相同。

> **说明**
> - 该命令存在系统初始记录，参数“ENABLE”的初始设置值为“DISABLE”。
> - 该命令下发时，如果命令携带的“SysLog服务器IP地址”参数对应的配置不存在，且当前已有的非网管Syslog配置记录数小于3，则会直接新增相关配置；否则返回错误码“101115 任务数量达到上限3个”。
> - 该命令不允许对网管Syslog日志收集服务器的配置进行变更。
> - 配置Syslog任务生效需要一定时间，建议执行该命令操作时间间隔1分钟。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| ENABLE | 启用状态 | 可选必选说明：必选参数。<br>参数含义：用于设置上报日志的启用状态。<br>取值范围：<br>- DISABLE(停用)<br>- ENABLE(启用)<br>默认值：无。<br>配置原则：如果配置为<br>“DISABLE(停用)”<br>，仅对非网管的Syslog日志收集服务器生效。 |
| IPTYPE | IP类型 | 可选必选说明：该参数在<br>“ENABLE(启用状态)”<br>为<br>“ENABLE(启用)”<br>时，为条件必选参数。<br>参数含义：接收日志的Syslog服务器IP类型。<br>数据来源：用户输入。<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无。<br>配置原则：无。 |
| IPV4 | SysLog服务器IP地址 | 可选必选说明：该参数在<br>“ENABLE(启用状态)”<br>为<br>“ENABLE(启用)”<br>且<br>“IPTYPE（IP类型）”<br>为<br>“IPV4(IPV4)”<br>时，为条件必选参数。<br>参数含义：接收日志的Syslog服务器IP地址。<br>取值范围：IPV4。<br>默认值：无。<br>配置原则：无。 |
| IPV6 | SysLog服务器IP地址 | 可选必选说明：该参数在<br>“ENABLE(启用状态)”<br>为<br>“ENABLE(启用)”<br>且<br>“IPTYPE（IP类型）”<br>为<br>“IPV6(IPV6)”<br>时，为条件必选参数。<br>参数含义：接收日志的Syslog服务器IP地址。<br>取值范围：IPV6。<br>默认值：无。<br>配置原则：无。 |
| SERVERPORT | 服务器端口 | 可选必选说明：该参数在<br>“ENABLE(启用状态)”<br>为<br>“ENABLE(启用)”<br>时，为条件必选参数。<br>参数含义：接收日志的Syslog服务器端口。<br>取值范围：1~65535之间的整数值。<br>默认值：无。<br>配置原则：无。 |
| LOGTYPE | 日志类型 | 可选必选说明：该参数在<br>“ENABLE(启用状态)”<br>为<br>“ENABLE(启用)”<br>时，为条件必选参数。<br>参数含义：上报的日志类型。<br>取值范围：<br>- DB_LOG(DB日志)<br>- OPERATING_LOG(操作日志)<br>- WEB_LOG(Web日志)<br>- SECURITY_LOG(安全日志)<br>- OS_LOG(OS日志)<br>- RUN_LOG(运行日志)<br>- EVENT_LOG(事件日志)<br>- OS_SECURITY_LOG(OS安全日志)<br>- SYSTEM_LOG(系统日志)<br>默认值：无。<br>配置原则：<br>- 上报任务时，至少选择一种日志类型。<br>- 仅在Full-stack虚机场景下支持收集OS日志、OS安全日志、系统日志。 |
| PROTOCOL | 协议类型 | 可选必选说明：该参数在<br>“ENABLE(启用状态)”<br>为<br>“ENABLE(启用)”<br>时，为条件可选参数。<br>参数含义：表示OM Portal与Syslog日志收集服务器的对接协议。<br>说明：TCP为不安全协议，存在安全风险，请谨慎使用。<br>UDP为不可靠通信协议，请谨慎使用。<br>取值范围：<br>- TLS(TLS)<br>- TCP(TCP)<br>- UDP(UDP)<br>默认值：TLS(TLS)<br>配置原则：无。 |
| CHECKSAN | Syslog服务器端SAN校验 | 可选必选说明：该参数在<br>“ENABLE(启用状态)”<br>为<br>“ENABLE(启用)”<br>时，为条件可选参数。<br>参数含义：表示OM Portal是否对Syslog日志收集服务器证书的SAN（Subject Alternative Names）校验。<br>说明：开启OM Portal对Syslog日志收集服务器证书的SAN校验时，若Syslog日志收集服务器侧证书的SAN不合法，则SAN校验不通过 ，可能会导致OM Portal与Syslog日志收集服务器通信异常。<br>取值范围：<br>- DISABLE(关闭)<br>- ENABLE(开启)<br>默认值：DISABLE(关闭)<br>配置原则：无。 |
| UNSECURECIPHER | 不安全加密算法 | 可选必选说明：该参数在<br>“ENABLE(启用状态)”<br>为<br>“ENABLE(启用)”<br>且<br>“PROTOCOL（协议类型）”<br>为<br>“TLS(TLS)”<br>时，为条件可选参数。<br>参数含义：表示AuditLog是否使用不安全加密算法与对端建立连接。<br>说明：若启用不安全加密算法，可能会存在安全风险，若停用不安全加密算法，对端Syslog服务器必须支持使用安全加密算法进行对接，否则会导致对接失败。<br>取值范围：<br>- DISABLE(停用)<br>- ENABLE(启用)<br>默认值：DISABLE(停用)<br>配置原则：无。 |
| DESC | 描述 | 可选必选说明：该参数在<br>“ENABLE(启用状态)”<br>为<br>“ENABLE(启用)”<br>时，为条件可选参数。<br>参数含义：表示Syslog配置的描述信息。<br>取值范围：不超过100字符。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SYSLOGTASK]] · 上报任务（SYSLOGTASK）

## 使用实例

- 停用当前所有任务：

```
%%SET SYSLOGTASK: ENABLE=DISABLE;%%
RETCODE = 0  操作成功
 
---    END
```

- 增加一个上报任务，“IP类型”为“IPV4”，“SysLog服务器IP地址”为“10.119.178.152”，“服务器端口”为“4399”，“日志类型”为“操作日志&安全日志”，“协议类型”为“TLS”，“Syslog服务器端SAN校验”为“开启”，“不安全加密算法”为“启用”，“描述”为“TEST”：

```
%%SET SYSLOGTASK: ENABLE=ENABLE, IPTYPE=IPV4, IPV4="10.119.178.152", SERVERPORT=4399, LOGTYPE=OPERATING_LOG-1&SECURITY_LOG-1, PROTOCOL=TLS, CHECKSAN=ENABLE, UNSECURECIPHER=ENABLE, DESC="Test";%%
RETCODE = 0  操作成功
 
---    END
```

- 增加一个上报任务，“IP类型”为“IPV6”，“SysLog服务器IP地址”为“fc00:0:0:0:0:0:0:1”，“服务器端口”为“6514”，“日志类型”为“操作日志&安全日志”，“协议类型”为“TCP”，“Syslog服务器端SAN校验”为“关闭”：

```
%%SET SYSLOGTASK: ENABLE=ENABLE, IPTYPE=IPV6, IPV6="fc00:0:0:0:0:0:0:1", SERVERPORT=6514, LOGTYPE=OPERATING_LOG-1&SECURITY_LOG-1, PROTOCOL=TCP, CHECKSAN=DISABLE;%%
RETCODE = 0  操作成功 

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SYSLOGTASK.md`
