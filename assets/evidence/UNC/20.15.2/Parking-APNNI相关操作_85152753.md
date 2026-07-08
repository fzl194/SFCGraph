# Parking APNNI相关操作

- [操作场景](#ZH-CN_OPI_0185152753__1.3.1)
- [必备事项](#ZH-CN_OPI_0185152753__1.3.2)
- [操作步骤](#ZH-CN_OPI_0185152753__1.3.3)
- [验证方法](#ZH-CN_OPI_0185152753__1.3.4)
- [任务示例](#ZH-CN_OPI_0185152753__1.3.5)

## [操作场景](#ZH-CN_OPI_0185152753)

本操作指导介绍在运行网络中为满足不同场景的需求，针对Parking APNNI所进行的操作过程。

- 场景1：设备PDP上下文资源不足
  当设备PDP上下文资源不足时，系统需要暂时释放Parking APN所使用的PDP资源。
- 场景2：尽快恢复使用Parking APN假激活功能的用户的各项业务
  当某应用业务故障（例如whatsapp应用）导致终端反复激活，系统启用Parking APN假激活功能后，在用户恢复业务的过程中，需要使用户尽快恢复业务。
- 场景3：修改Parking APNNI
  当系统打开Parking APN假激活开关并配置相应的Parking APNNI后，运营商可根据需要修改此Parking APNNI。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0185152753)

前提条件

- 请仔细阅读[WSFD-206006 Smartphone异常信令节省特性概述](特性概述_86930572.md)。
- 完成加载License。

- Parking APN假激活开关已经打开，可通过执行[**LST SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/查询激活抑制规则（LST SMARTACT）_26145744.md)命令查询。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md) | Parking APN（PARKINGAPN） | huawei2.com | 全网规划 | 修改<br>UNC<br>的Parking APNNI。 |

## [操作步骤](#ZH-CN_OPI_0185152753)

- 场景1：设备PDP上下文资源不足。
    1. 进入 “MML命令行-UNC” 窗口。
    2. 关闭所有终端类型的Parking APN假激活开关。
      [**MOD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/修改激活抑制规则（MOD SMARTACT）_72345343.md) ： UETYPE=终端类型 ，PARKINGAPNSW=OFF;
      > **说明**
      > 参数 “PARKINGAPNSW” （Parking APN假激活功能开关）固定选择 “OFF” 。
    3. 在GGSN上去激活使用Parking APN的PDP上下文，使Parking APN的PDP上下文数目为零。
    4. **可选：**PDP上下文资源问题（例如完成设备PDP上下文扩容）解决后，开启各终端类型的Parking APN假激活的功能开关。
      > **说明**
      > 如果需要对异常激活用户继续采用Parking APN假激活功能，则执行此步骤。
      [**MOD SMARTACT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制规则管理/修改激活抑制规则（MOD SMARTACT）_72345343.md) ： UETYPE=终端类型 ，PARKINGAPNSW=ON;
      > **说明**
      > 参数 “PARKINGAPNSW” （Parking APN假激活功能开关）固定选择 “ON” 。
- 场景2：尽快恢复使用Parking APN假激活功能的用户的各项业务。
    1. 关闭所有终端类型的Parking APN假激活开关，具体步骤请参考场景1中的 [步骤 2](#ZH-CN_OPI_0185152753__zh-cn_opi_0130429046_step1_1) 。
    2. 在GGSN上去激活使用Parking APN的PDP上下文，使Parking APN的PDP上下文数目为零。
    3. **可选：**大量用户业务恢复正常（例如1小时后）后，开启各终端类型的Parking APN假激活的功能开关，具体步骤请参考场景中1的 [步骤 4](#ZH-CN_OPI_0185152753__zh-cn_opi_0130429046_step1_3) 。
- 场景3：修改Parking APNNI。
    1. 关闭所有终端类型的Parking APN假激活开关，具体步骤请参考场景1中的 [步骤 2](#ZH-CN_OPI_0185152753__zh-cn_opi_0130429046_step1_1) 。
    2. 在GGSN上去激活使用Parking APN的PDP上下文，使Parking APN的PDP上下文数目为零。
    3. 修改 UNC 的Parking APNNI。
      [**SET SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md) ： PARKINGAPN=Parking APN ;
    4. 修改GGSN上的Parking APNNI。
    5. **可选：**开启各终端类型的Parking APN假激活的功能开关，具体步骤请参考场景1中的 [步骤 4](#ZH-CN_OPI_0185152753__zh-cn_opi_0130429046_step1_3) 。

## [验证方法](#ZH-CN_OPI_0185152753)

场景3中的修改Parking APNNI的验证方法如下：

1. 进入 “MML命令行-UNC” 窗口。
2. 查询修改后的Parking APNNI
  [**LST SMARTACTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/激活抑制参数管理/查询激活抑制参数（LST SMARTACTPARA）_72345341.md) :;
  预期结果：查询结果和配置结果一致。

## [任务示例](#ZH-CN_OPI_0185152753)

任务描述

UNC 已经为使用黑莓手机的用户配置了Parking APN假激活功能，避免其终端产生大量异常信令，使用的Parking APN为PARKINGAPNNI。

- 任务1：利用去激活Parking APN功能解决设备PDP上下文资源不足问题，问题解决后用户继续使用Parking APN假激活抑制功能。
- 任务2：Parking APN假激活功能生效，需要帮助用户尽快恢复各项业务，且使用户继续使用Parking APN假激活抑制功能。
- 任务3：将该用户使用的Parking APN更改为huawei2.com，且在更改后使用户继续使用Parking APN假激活抑制功能。

脚本

- 脚本1：
  //关闭黑莓终端的Parking APN假激活开关。

  ```
  MOD SMARTACT: UETYPE=BLACKBERRY, PARKINGAPNSW=OFF;
  ```
  //去激活Parking APN使用的PDP上下文，查询GGSN上此类PDP上下文数为零。
  //PDP资源问题（比如完成设备PDP扩容）解决后，开启Parking APN假激活开关。

  ```
  MOD SMARTACT: UETYPE=BLACKBERRY, PARKINGAPNSW=ON;
  ```
- 脚本2：
  //关闭黑莓终端的Parking APN假激活开关。

  ```
  MOD SMARTACT: UETYPE=BLACKBERRY, PARKINGAPNSW=OFF;
  ```
  //去激活Parking APN使用的PDP上下文，查询GGSN上此类PDP上下文数为零。
  /GGSN上使用Parking APN的PDP上下文数目为零，并且大量用户业务恢复正常（例如1小时后）后，开启Parking APN假激活开关。

  ```
  MOD SMARTACT: UETYPE=BLACKBERRY, PARKINGAPNSW=ON;
  ```
- 脚本3：
  //关闭黑莓终端的Parking APN假激活开关。

  ```
  MOD SMARTACT: UETYPE=BLACKBERRY, PARKINGAPNSW=OFF;
  ```
  //去激活Parking APN使用的PDP上下文，查询GGSN上此类PDP上下文数为零。
  //修改UNC上的Parking APNNI。

  ```
  SET SMARTACTPARA：PARKINGAPN="huawei2.com";
  ```
  //修改GGSN上的Parking APNNI。
  //开启Parking APN假激活开关。

  ```
  MOD SMARTACT: UETYPE=BLACKBERRY, PARKINGAPNSW=ON;
  ```
