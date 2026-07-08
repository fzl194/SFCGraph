---
id: UDG@20.15.2@MMLCommand@DSP DEACTIVESTATE
type: MMLCommand
name: DSP DEACTIVESTATE（显示去活操作状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DEACTIVESTATE
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 查询会话去活状态
status: active
---

# DSP DEACTIVESTATE（显示去活操作状态）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询手动批量去激活命令的执行情况。指定IMSI、MSISDN、或IMEI的用户去激活无法被查询。

执行该命令时，Remain Time (hour)实际时间受CPU占用率影响。CPU占用率越高，实际Remain Time可能会比预期的计算时间长。

## 注意事项

该命令执行后需要关闭已经创建了数据面跟踪的所有跟踪任务，重新创建新的跟踪任务才能生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DEACTIVESTATE]] · 去活操作状态（DEACTIVESTATE）

## 使用实例

执行DEA SESSION命令后，使用DSP DEACTIVESTATE命令查询执行结果：

```
DSP DEACTIVESTATE:;
```

```

RETCODE = 0 操作成功。

Deactivation Info:
------------------
Result  =  
       Deactivation parameter setting = NF
                      Execution stage = Deleting
            To delete sessions number = 516168
              Deleted sessions number = 516157
                   Remain Time (hour) = 0.1
            Deactivation rate-setting = 2000
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DEACTIVESTATE.md`
