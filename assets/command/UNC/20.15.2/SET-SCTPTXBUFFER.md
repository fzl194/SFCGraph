---
id: UNC@20.15.2@MMLCommand@SET SCTPTXBUFFER
type: MMLCommand
name: SET SCTPTXBUFFER（设置SCTP发送缓冲区参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SCTPTXBUFFER
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

# SET SCTPTXBUFFER（设置SCTP发送缓冲区参数）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于设置系统中SCTP发送端缓冲区参数。

## 注意事项

- 该命令执行后需要重启SGP进程才能生效。
- 该命令会影响SCTP内存分布。
- 该命令可以分别设置共享模式、私有模式下的发送端缓冲区参数。
- 该命令配置的参数仅在[SET SCTPBUFFCFG](设置SCTP缓冲区参数源(SET SCTPBUFFCFG)_03932862.md)的参数源类型设置为自定义时才会生效。正常情况下，系统内置参数保证业务正常。如果使用自定义参数请联系华为。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODE | 模式选项 | 可选必选说明：必选参数<br>参数含义：该参数用于区分共享模式、私有模式下的参数配置。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- SHARE（共享模式）<br>- PRIVATE（私有模式）<br>系统初始设置值：无<br>配置原则：<br>- 在[SET SCTPBUFFCFG](设置SCTP缓冲区参数源(SET SCTPBUFFCFG)_03932862.md)的参数源类型设置为自定义，且[SET SCTPBUFFERMODE](设置SCTP缓冲区模式(SET SCTPBUFFERMODE)_04252670.md)中发送缓冲区模式为共享模式时，SHARE对应的参数将生效。<br>- 在[SET SCTPBUFFCFG](设置SCTP缓冲区参数源(SET SCTPBUFFCFG)_03932862.md)的参数源类型设置为自定义，且[SET SCTPBUFFERMODE](设置SCTP缓冲区模式(SET SCTPBUFFERMODE)_04252670.md)中发送缓冲区模式为私有模式时，PRIVATE对应的参数将生效。 |
| MINTXSIZE | 迷你端私有缓冲区大小 | 可选必选说明：可选参数<br>参数含义：<br>- 在共享模式下，该参数表示迷你端缓冲区发送缓冲区的总大小。<br>- 在私有模式下，该参数表示迷你端缓冲区私有发送缓冲区的大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~70000。<br>系统初始设置值：<br>- 共享模式：20000<br>- 私有模式：70000<br>配置原则：不建议超过70000。 |
| MINEXTXSIZE | 迷你端共享缓冲区大小 | 可选必选说明：可选参数<br>参数含义：<br>- 在共享模式下，该参数表示迷你端缓冲区自有缓冲区的总大小。<br>- 在私有模式下，该参数不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~70000。<br>系统初始设置值：<br>- 共享模式：50000<br>配置原则： 不建议超过50000。 |
| MINEXTXNUM | 迷你端共享缓冲区个数 | 可选必选说明：可选参数<br>参数含义：<br>- 在共享模式下，该参数表示迷你端共享缓冲区个数。<br>- 在私有模式下，该参数不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~3000。<br>系统初始设置值：<br>- 共享模式：600<br>配置原则：不建议超过600。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCTPTXBUFFER]] · SCTP发送缓冲区参数（SCTPTXBUFFER）

## 使用实例

设置共享模式下的发送缓冲区参数，指定迷你端私有缓冲区大小为100、迷你端共享缓冲区大小为2048字节、迷你端共享缓冲区个数为30：

```
SET SCTPTXBUFFER: MODE=SHARE, MINTXSIZE=100, MINEXTXSIZE=2048, MINEXTXNUM=30;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SCTPTXBUFFER.md`
