---
id: UNC@20.15.2@MMLCommand@DSP DEASMCTXSTATUS
type: MMLCommand
name: DSP DEASMCTXSTATUS（显示去活操作状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DEASMCTXSTATUS
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 查询去活SM上下文状态
status: active
---

# DSP DEASMCTXSTATUS（显示去活操作状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来查询手动批量去激活命令的执行情况。指定IMSI、MSISDN的用户去激活无法被查询。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DEASMCTXSTATUS]] · 去活操作状态（DEASMCTXSTATUS）

## 使用实例

当前未执行DEASMCTX且ActionType为START_DEA的去活会话命令，使用DSP DEASMCTXSTATUS命令查询执行结果： 2.执行DEASMCTX且ActionType为START_DEA的去活会话命令后，正常执行过程中，使用DSP DEASMCTXSTATUS命令查询执行结果： 3.执行DEASMCTX且ActionType为START_DEA的去活会话命令后，有POD复位或者扩缩容，使用DSP DEASMCTXSTATUS命令查询执行结果： 4.执行DEASMCTX且ActionType为START_DEA的去活会话命令后，执行STOP DEASMCTX，使用DSP DEASMCTXSTATUS命令查询执行结果：

```
%%DSP DEASMCTXSTATUS:;%%
RETCODE = 0  操作成功

结果如下
--------
                  执行阶段  =  Invalid
               去活进度(%)  =  0
                  异常标识  =  否
              已去活会话数  =  0
        去活任务的开始时间  =  NULL
        去活任务的完成时间  =  NULL
        任务强制结束的时间  =  NULL
任务所在Ctrl进程的启动时间  =  XXYYZZ
   任务所在Ctrl进程的PODID  =  XXXX
最近一次批量去活命令的内容  =  NULL

(结果个数 = 1)

---    END
2.
%%DSP DEASMCTXSTATUS:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                  执行阶段  =  Deactivation
               去活进度(%)  =  25
                  异常标识  =  否
              已去活会话数  =  100
        去活任务的开始时间  =  XXYYZZ
        去活任务的完成时间  =  NULL
        任务强制结束的时间  =  NULL
任务所在Ctrl进程的启动时间  =  XXYYZZ
   任务所在Ctrl进程的PODID  =  XXXX
最近一次批量去活命令的内容  =  XXX

(结果个数 = 1)

---    END
3.
%%DSP DEASMCTXSTATUS:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                  执行阶段  =  Deactivation
               去活进度(%)  =  35
                  异常标识  =  是
              已去活会话数  =  135
        去活任务的开始时间  =  XXYYZZ
        去活任务的完成时间  =  NULL
        任务强制结束的时间  =  NULL
任务所在Ctrl进程的启动时间  =  XXYYZZ
   任务所在Ctrl进程的PODID  =  XXXX
最近一次批量去活命令的内容  =  XXX

(结果个数 = 1)

---    END
4.
%%DSP DEASMCTXSTATUS:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                  执行阶段  =  Stop
               去活进度(%)  =  35
                  异常标识  =  否
              已去活会话数  =  135
        去活任务的开始时间  =  XXYYZZ
        去活任务的完成时间  =  NULL
        任务强制结束的时间  =  XXYYZZ
任务所在Ctrl进程的启动时间  =  XXYYZZ
   任务所在Ctrl进程的PODID  =  XXXX
最近一次批量去活命令的内容  =  XXX

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DEASMCTXSTATUS.md`
