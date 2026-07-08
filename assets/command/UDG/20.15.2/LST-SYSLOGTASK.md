---
id: UDG@20.15.2@MMLCommand@LST SYSLOGTASK
type: MMLCommand
name: LST SYSLOGTASK（查询上报任务）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SYSLOGTASK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# LST SYSLOGTASK（查询上报任务）

## 功能

本命令用于请求系统显示已创建的Syslog上报任务信息以及连接状态。

Syslog上报任务可以在 OM Portal 界面 “ 系统>Syslog管理 ” 或者执行 **SET SYSLOGTASK** 命令进行操作。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SYSLOGTASK]] · 上报任务（SYSLOGTASK）

## 使用实例

- 当前仅存在一个开启的Syslog任务时，获取当前上报的任务信息：

```
%%LST SYSLOGTASK:;%%
RETCODE = 0  操作成功
 
结果信息
--------
             服务器IP  =  10.119.178.152
           服务器端口  =  6514
             日志类型  =  操作日志
             连接状态  =  连接
             启用状态  =  启用
             协议类型  =  TLS
Syslog服务器端SAN校验  =  开启
       不安全加密算法  =  启用
                 描述  =  Test
(结果个数 = 1)
 
---    END
```

- 当前存在多个开启的Syslog任务时，获取当前上报的任务信息：

```
%%LST SYSLOGTASK:;%%
RETCODE = 0  操作成功

结果信息
--------
服务器IP        服务器端口  日志类型                    连接状态  启用状态  协议类型  Syslog服务器端SAN校验  不安全加密算法  描述    

10.110.205.7    29924       操作日志&安全日志&系统日志  断开      启用      TCP       开启                   启用            NULL   
10.110.98.253   6514        操作日志&安全日志           连接      启用      TLS       关闭                   停用            NULL   
10.119.178.152  4399        操作日志&安全日志           断开      启用      TLS       开启                   启用            Test  
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SYSLOGTASK.md`
