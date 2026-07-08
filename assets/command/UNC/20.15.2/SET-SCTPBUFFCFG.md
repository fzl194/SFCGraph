---
id: UNC@20.15.2@MMLCommand@SET SCTPBUFFCFG
type: MMLCommand
name: SET SCTPBUFFCFG（设置SCTP缓冲区参数源）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SCTPBUFFCFG
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

# SET SCTPBUFFCFG（设置SCTP缓冲区参数源）

## 功能

![](设置SCTP缓冲区参数源(SET SCTPBUFFCFG)_03932862.assets/notice_3.0-zh-cn_2.png)

该命令会改变SCTP通信缓存的使用方式，触发SGP进程内存占用率变化，影响S1接口和N2接口链路的接入。系统稳定运行场景下请慎用本功能。

**适用NF：SGSN、MME、AMF**

该命令用于设置在SCTP初始化时分配缓冲区的参数来源。当前参数来源支持系统内置和用户自定义。系统内置参数源不可更改，用户自定义参数源可以通过 [SET SCTPRXBUFFER](设置SCTP接收缓冲区参数(SET SCTPRXBUFFER)_50932653.md) 和 [SET SCTPTXBUFFER](设置SCTP发送缓冲区参数(SET SCTPTXBUFFER)_81290310.md) 控制。

## 注意事项

- 该命令执行后需要重启SGP进程才能生效。
- 该命令会影响SCTP内存分布。
- 当将此命令中SCTP缓冲区参数源类型设置为“CUSTOM（自定义）”时，系统会使用[SET SCTPRXBUFFER](设置SCTP接收缓冲区参数(SET SCTPRXBUFFER)_50932653.md)和[SET SCTPTXBUFFER](设置SCTP发送缓冲区参数(SET SCTPTXBUFFER)_81290310.md)配置SCTP缓冲区相关参数。
- 当将此命令中SCTP缓冲区参数源类型设置为“SYSTEM（系统内置）”时，系统会使用[**SET BIGSCTPRXNUM**](设置大端模式SCTP接收缓冲区参数(SET BIGSCTPRXNUM)_26238016.md)配置SCTP接收缓冲区相关参数。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | SCTP缓冲区参数源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP缓冲区初始化时使用的参数来源。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- SYSTEM（系统内置）：SCTP缓冲区将使用系统内置参数进行初始化，用户自行设置的参数不会生效。<br>- CUSTOM（自定义）：SCTP缓冲区将使用用户设置的参数进行初始化，用户自定义参数源可以通过[SET SCTPRXBUFFER](设置SCTP接收缓冲区参数(SET SCTPRXBUFFER)_50932653.md)和[SET SCTPTXBUFFER](设置SCTP发送缓冲区参数(SET SCTPTXBUFFER)_81290310.md)进行设置。<br>系统初始设置值：SYSTEM |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCTPBUFFCFG]] · SCTP缓冲区参数源（SCTPBUFFCFG）

## 使用实例

修改SCTP缓冲区参数源为自定义：

```
SET SCTPBUFFCFG: TYPE=CUSTOM;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SCTPBUFFCFG.md`
