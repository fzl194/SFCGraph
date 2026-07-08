# 激活基于APN的NB-IoT终端接入速率控制（PGW-C）

- [操作场景](#ZH-CN_OPI_0277673129__1.3.1)
- [必备事项](#ZH-CN_OPI_0277673129__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277673129__1.3.3)
- [任务示例](#ZH-CN_OPI_0277673129__1.3.4)

## [操作场景](#ZH-CN_OPI_0277673129)

在 UNC 上激活基于APN的NB-IoT终端接入速率控制，用于控制该UE的某PDN连接单位时间内上行和下行数据包的数目。

> **说明**
> 适用于PGW-C。

## [必备事项](#ZH-CN_OPI_0277673129)

前提条件

- 请仔细阅读[WSFD-215204 基于APN的NB-IoT终端接入速率控制特性概述（PGW-C）](特性概述_77673128.md)。
- 已完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md) | APN（APN） | apn-op | 已配置数据中获取 | 开启基于APN的APN速率控制功能。 |
| [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md) | APN速率控制开关（APNRATECTRLSW） | ENABLE | 本端规划 | 开启基于APN的APN速率控制功能。 |
| [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md) | 上行时间单位（ULTIMEUNIT） | HOUR | 本端规划 | 开启基于APN的APN速率控制功能。 |
| [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md) | 最大上行速率（MAXULRATE） | 50 | 本端规划 | 开启基于APN的APN速率控制功能。 |
| [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md) | 下行时间单位（DLTIMEUNIT） | HOUR | 本端规划 | 开启基于APN的APN速率控制功能。 |
| [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md) | 最大下行速率（MAXDLRATE） | 100 | 本端规划 | 开启基于APN的APN速率控制功能。 |

## [操作步骤](#ZH-CN_OPI_0277673129)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 开启基于APN的APN速率控制功能。
  [**SET APNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/APN速率控制/APN速率控制配置/设置APN速率控制配置（SET APNRATECTRL）_64343913.md)
4. **可选：**配置APN Rate Control改变时发送CCR消息。
  [**ADD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
5. **可选：**配置CDR话单中携带APN Rate Control字段。
  [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
6. **可选：**配置PGW-CDR中携带APN Rate Control字段。
  [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)

## [任务示例](#ZH-CN_OPI_0277673129)

任务描述

开启基于APN的NB-IoT终端接入速率控制功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WNBARC11",SWITCH=ENABLE;
```

//开启基于APN的APN速率控制功能。

```
SET APNRATECTRL:APN="apn-op",APNRATECTRLSW=ENABLE,ULTIMEUNIT=HOUR,MAXULRATE=50,DLTIMEUNIT=HOUR,MAXDLRATE=100;
```
