---
id: UNC@20.15.2@MMLCommand@SET SCTPBUFFERMODE
type: MMLCommand
name: SET SCTPBUFFERMODE（设置SCTP缓冲区模式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SCTPBUFFERMODE
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# SET SCTPBUFFERMODE（设置SCTP缓冲区模式）

## 功能

![](设置SCTP缓冲区模式(SET SCTPBUFFERMODE)_04252670.assets/notice_3.0-zh-cn_2.png)

该命令会改变SCTP通信缓存的使用方式，触发SGP进程内存占用率变化，影响S1接口和N2接口链路的接入。系统稳定运行场景下请慎用本功能。

**适用NF：SGSN、MME、AMF**

该命令用于设置系统中SCTP缓冲区的模式。当前模式支持共享模式和私有模式。私有模式表示每个偶联有自己单独的缓冲区，共享模式表示单个SGP进程内的偶联共用一块内存。共享模式相比私有模式可以减少内存开销。

## 注意事项

- 该命令执行后需要重启SGP进程才能生效。
- 该命令会影响SCTP内存分布，配置参数不合理可能导致SGP进程异常。
- 当将此命令中接收端缓冲区模式或发送端缓冲区模式设置为私有时，单SGP进程可容纳的SCTP偶联数量会减少至1000。请先通过[DSP SCTPBALANCEINFO](查询SCTP均衡信息(DSP SCTPBALANCEINFO)_16196710.md)查询每个进程上的“单进程基站总个数”，确认基站数均小于1000时方可使用私有模式。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RXMODE | 接收端缓冲区模式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SCTP接收端缓冲区模式。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- SHARE（共享模式）：所有偶联将使用进程共享的SCTP缓冲区。<br>- PRIVATE（私有模式）：所有偶联将使用各自私有的SCTP缓冲区。<br>系统初始设置值：SHARE |
| TXMODE | 发送端缓冲区模式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SCTP发送端缓冲区模式。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- SHARE（共享模式）：所有偶联将使用进程共享的SCTP缓冲区。<br>- PRIVATE（私有模式）：所有偶联将使用各自私有的SCTP缓冲区。<br>系统初始设置值：SHARE |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPBUFFERMODE]] · SCTP缓冲区模式（SCTPBUFFERMODE）

## 使用实例

设置SCTP发送端缓冲区模式为私有模式、接收端缓冲区模式为共享模式：

```
SET SCTPBUFFERMODE: RXMODE=SHARE, TXMODE=PRIVATE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SCTPBUFFERMODE.md`
