# 激活NB-IoT eDRX模式

- [操作场景](#ZH-CN_OPI_0267487577__1.3.1)
- [必备事项](#ZH-CN_OPI_0267487577__1.3.2)
- [操作步骤](#ZH-CN_OPI_0267487577__1.3.3)
- [任务示例](#ZH-CN_OPI_0267487577__1.3.4)

## [操作场景](#ZH-CN_OPI_0267487577)

本操作指导介绍在4G网络下激活NB-IoT eDRX模式特性的操作过程。

> **说明**
> 适用于SGW-U。

## [必备事项](#ZH-CN_OPI_0267487577)

前提条件

- 请仔细阅读[GWFD-110601 NB-IoT eDRX模式](../GWFD-110601 NB-IoT eDRX模式_67378801.md)。
- 已开启NB-IoT基本接入功能（详见[激活NB-IoT终端标准接入](../GWFD-010296 NB-IoT终端标准接入/激活NB-IoT终端标准接入_74275194.md)）。
- 完成加载License（如果有需求，请联系华为技术支持工程师处理）。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[ADD APN](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)** | APN名称（APN） | apnnb | 本端规划 | eDRX模式所使用的APN。 |
| **[SET GLBDLBUFTIME](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/全局下行数据缓存时长/设置全局下行数据缓存时长（SET GLBDLBUFTIME）_82837186.md)** | NB-IoT用户下行数据缓存时长（NBIOTUSER） | 20 | 本端规划 | - |
| **[SET APNDLBUFTIME](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/APN的下行数据缓存时长/设置基于APN的下行数据缓存时长（SET APNDLBUFTIME）_82837189.md)** | APN（APN） | apnnb | 已配置数据中获取 | 已通过<br>**[ADD APN](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)**<br>命令配置，可以使用<br>**[LST APN](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/查询APN配置（LST APN）_82837017.md)**<br>命令查询。 |
| **[SET APNDLBUFTIME](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/APN的下行数据缓存时长/设置基于APN的下行数据缓存时长（SET APNDLBUFTIME）_82837189.md)** | NB-IoT用户下行数据缓存时长（NBIOTUSER） | 10 | 本端规划 | - |
| **[SET GLBDLLTBUFFER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/全局下行数据长时间缓存/设置全局下行数据长时间缓存个数（SET GLBDLLTBUFFER）_86530268.md)** | 最大缓存个数（MAXBUFFERNUM） | 16 | 本端规划 | 该参数与DDN Ack消息携带的缓存个数取最小值作为系统实际缓存的最大个数; 如果DDN Ack消息没有携带缓存个数，使用该参数配置作为系统实际缓存的最大个数。 |
| **[SET GLBDLLTBUFFER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/全局下行数据长时间缓存/设置全局下行数据长时间缓存个数（SET GLBDLLTBUFFER）_86530268.md)** | 储存方式（BUFFERMODE） | BUFF_MODE_RING | 本端规划 | - |
| **[SET APNDLLTBUFFER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/APN下行数据长时间缓存/设置基于APN的下行数据长时间缓存配置（SET APNDLLTBUFFER）_86530338.md)** | APN（APN） | apnnb | 已配置数据中获取 | 已通过<br>**[ADD APN](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)**<br>命令配置，可以使用<br>**[LST APN](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/查询APN配置（LST APN）_82837017.md)**<br>命令查询。 |
| **[SET APNDLLTBUFFER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/APN下行数据长时间缓存/设置基于APN的下行数据长时间缓存配置（SET APNDLLTBUFFER）_86530338.md)** | 最大缓存个数（MAXBUFFERNUM） | 4 | 本端规划 | - |
| **[SET APNDLLTBUFFER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/APN下行数据长时间缓存/设置基于APN的下行数据长时间缓存配置（SET APNDLLTBUFFER）_86530338.md)** | 储存方式（BUFFERMODE） | BUFF_MODE_RING | 本端规划 | - |

## [操作步骤](#ZH-CN_OPI_0267487577)

1. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)
2. 配置eDRX模式所使用的APN。
  **[ADD APN](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)**
3. **可选：** 配置APN下的NB-IoT eDRX参数。
    a. 配置APN的下行数据缓存时长。
      **[SET APNDLBUFTIME](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/APN的下行数据缓存时长/设置基于APN的下行数据缓存时长（SET APNDLBUFTIME）_82837189.md)**
    b. 配置APN的下行数据长时间缓存配置。
      **[SET APNDLLTBUFFER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/APN下行数据长时间缓存/设置基于APN的下行数据长时间缓存配置（SET APNDLLTBUFFER）_86530338.md)**
4. **可选：** 配置全局的NB-IoT eDRX参数。
    a. 配置全局下行数据缓存时长。
      **[SET GLBDLBUFTIME](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/全局下行数据缓存时长/设置全局下行数据缓存时长（SET GLBDLBUFTIME）_82837186.md)**
    b. 配置全局下行数据长时间缓存配置。
      **[SET GLBDLLTBUFFER](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/GTP隧道管理/全局下行数据长时间缓存/设置全局下行数据长时间缓存个数（SET GLBDLLTBUFFER）_86530268.md)**
      > **说明**
      > 对于缓存时长和长时间缓存配置：
      >
      > - 如果SGW-U/PGW-U和MME上都配置了缓存时长和长时间缓存配置参数，当MME通过DDN ACK下发这些参数时，最大缓存个数取两者最小值，NB-IoT用户下行数据缓存时长取MME下发值。
      > - 如果全局和APN下同时配置了缓存时长和长时间缓存配置参数，生效优先级：APN>全局。

## [任务示例](#ZH-CN_OPI_0267487577)

任务描述

在本实例中，在 UDG 上开启eDRX模式，并且配置APN、全局的下行数据缓存时长和长时间缓存配置。

脚本

//开启NB-IoT基本功能后，打开本特性License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV3G5NDRX01", SWITCH=ENABLE;
```

//配置eDRX模式所使用的APN。

```
ADD APN: APN="apnnb";
```

//配置APN的下行数据缓存时长。

```
SET APNDLBUFTIME: APN="apnnb", NBIOTUSER=10;
```

//配置APN的下行数据长时间缓存配置。

```
SET APNDLLTBUFFER: APN="apnnb", MAXBUFFERNUM=4, BUFFERMODE=BUFF_MODE_RING;
```

//配置全局下行数据缓存时长。

```
SET GLBDLBUFTIME: NBIOTUSER=20;
```

//配置全局下行数据长时间缓存配置。

```
SET GLBDLLTBUFFER: MAXBUFFERNUM=16, BUFFERMODE=BUFF_MODE_RING;
```
