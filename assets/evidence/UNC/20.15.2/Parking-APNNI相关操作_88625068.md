# Parking APNNI相关操作

- [操作场景](#ZH-CN_OPI_0188625068__1.3.1)
- [必备事项](#ZH-CN_OPI_0188625068__1.3.2)
- [操作步骤](#ZH-CN_OPI_0188625068__1.3.3)
- [任务示例](#ZH-CN_OPI_0188625068__1.3.4)

## [操作场景](#ZH-CN_OPI_0188625068)

本操作指导介绍在运行网络中为满足不同场景的需求，针对Parking APN所进行的操作过程。

- 场景1：设备PDN连接资源不足
  当设备PDN连接资源不足时，系统需要暂时释放Parking APN所使用的PDN连接资源。
- 场景2：尽快恢复使用Parking APN激活功能的用户的各项业务。
  当终端反复发送Attach Request、PDN Connectivity Request消息时，系统启用了Parking APN激活抑制措施。由于Parking APN不能进行数据业务，当用户需要使用Parking APN激活功能的各项业务时，需要帮助用户尽快恢复业务。
- 场景3：修改Parking APN
  当系统Parking APN激活抑制措施已经开启并配置相应的Parking APN后，运营商可根据需要修改此Parking APN。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0188625068)

前提条件

- 已经加载支持Parking APN激活功能的License，对应的License项为“LTE UE信令控制”。
- Parking APN激活抑制措施已经开启，可调用 **[**LST S1SMARTRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/S1模式信令抑制规则管理/查询S1模式信令抑制规则(LST S1SMARTRULE)_72345347.md)** 命令查询“ATTACHCTRLRULE（附着抑制措施）”、“PDNCONNCTRLRULE（PDN连接抑制措施）”参数的配置。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[**SET S1SMARTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)** | Parking APN（PARKINGAPN） | huawei2.com | 全网规划 | Parking APN |

## [操作步骤](#ZH-CN_OPI_0188625068)

- 进入 “MML命令行-UNC” 窗口。
- **场景1：设备PDN连接资源不足。**
    1. 关闭所有终端类型的Parking APN激活抑制措施。
      **[**MOD S1SMARTRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/S1模式信令抑制规则管理/修改S1模式信令抑制规则(MOD S1SMARTRULE)_72225425.md)**

      > **说明**
      > 只有“ATTACHCTRLRULE（附着抑制措施）”和“PDNCONNCTRLRULE（PDN连接抑制措施）”可以配置“Parking APN激活”抑制措施。
    2. 在UDG上去激活使用Parking APN的PDN连接，使Parking APN的PDN连接数目为零。
    3. **[MOD S1SMARTRULE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/S1模式信令抑制规则管理/修改S1模式信令抑制规则(MOD S1SMARTRULE)_72225425.md)**
      **可选：** PDN连接资源问题（例如完成设备PDN连接扩容）解决后，可以开启Parking APN激活抑制措施。

      > **说明**
      > 如果需要对发送异常Attach Request、PDN Connectivity Request消息的终端继续采用Parking APN激活抑制措施，则执行此步骤。
- **场景2：尽快恢复使用Parking APN激活功能的用户的各项业务。**
    1. 关闭所有终端类型的Parking APN激活抑制措施，具体步骤请参考场景1中的 [步骤 1](#ZH-CN_OPI_0188625068__li1856473264820) 。
    2. 在 UDG 上去激活使用Parking APN的PDN连接，使Parking APN的PDN连接数目为零。
    3. **可选：** 大量用户业务恢复正常（例如1小时后）后，开启各终端类型Attach Request、PDN Connectivity Request消息的Parking APN激活抑制措施，具体步骤请参考场景中1的 [步骤 3](#ZH-CN_OPI_0188625068__li1048674220515) 。
- **场景3：修改Parking APN。**
    1. 关闭所有终端类型的Parking APN激活抑制措施，具体步骤请参考场景1中的 [步骤 1](#ZH-CN_OPI_0188625068__li1856473264820) 。
    2. 在 UDG 上去激活使用Parking APN的PDN连接，使Parking APN的PDN连接数目为零。
    3. 修改 UNC 的Parking APN。
      **[**SET S1SMARTPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/Smartphone管理/异常信令节省/S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)**
    4. 修改 UDG 的Parking APN。
    5. **可选：** 开启各终端类型的Parking APN激活抑制措施，具体步骤请参考场景1中的 [步骤 3](#ZH-CN_OPI_0188625068__li1048674220515) 。

## [任务示例](#ZH-CN_OPI_0188625068)

任务描述

UNC 已经为使用安卓手机的用户配置了Parking APN激活功能，抑制其终端产生大量Attach Request、PDN Connectivity Request异常信令，使用的Parking APN为huawei2.com。

- 任务1：利用去激活Parking APN功能解决设备PDN连接资源不足问题，问题解决后用户继续使用Parking APN激活抑制功能。
- 任务2：Parking APN激活抑制措施生效，需要帮助用户尽快恢复各项业务，且使用户继续使用Parking APN激活抑制功能。
- 任务3：将该用户使用的Parking APN更改为huawei2.com，且在更改后使用户继续使用Parking APN激活抑制功能。

脚本

- 脚本1：
  //关闭安卓终端的Parking APN激活抑制措施。
  ```
  MOD S1SMARTRULE: UETYPE=ANDROID, ATTACHCTRLRULE=PARKAPNACT-0, PDNCONNCTRLRULE=PARKAPNACT-0; 
  ```
  //去激活Parking APN使用的PDN连接，查询 UDG 上此类PDN连接数为零。
  //PDN连接资源问题（比如完成设备PDN扩容）解决后，开启Parking APN激活抑制措施。
  ```
  MOD S1SMARTRULE: UETYPE=ANDROID, ATTACHCTRLRULE=PARKAPNACT-1, PDNCONNCTRLRULE=PARKAPNACT-1;
  ```
- 脚本2：
  //关闭安卓终端的Parking APN激活抑制措施。
  ```
  MOD S1SMARTRULE: UETYPE=ANDROID, ATTACHCTRLRULE=PARKAPNACT-0, PDNCONNCTRLRULE=PARKAPNACT-0; 
  ```
  //去激活Parking APN使用的PDN连接，查询 UDG 上此类PDN连接数为零。
  // UDG 上使用Parking APN的PDN连接数目为零，并且大量用户业务恢复正常（例如1小时后）后，开启Parking APN激活抑制措施。
  ```
  MOD S1SMARTRULE: UETYPE=ANDROID, ATTACHCTRLRULE=PARKAPNACT-1, PDNCONNCTRLRULE=PARKAPNACT-1;
  ```
- 脚本3：
  //关闭安卓终端的Parking APN激活抑制措施。
  ```
  MOD S1SMARTRULE: UETYPE=ANDROID, ATTACHCTRLRULE=PARKAPNACT-0, PDNCONNCTRLRULE=PARKAPNACT-0;
  ```
  //去激活Parking APN使用的PDN连接，查询 UDG 上此类PDN连接数为零。
  //修改 UNC 上的Parking APN。 UDG 上的Parking APN配置请参考UDG产品文档进行配置。
  ```
  SET S1SMARTPARA: PARKINGAPN="huawei2.com";
  ```
  //开启Parking APN激活抑制措施。
  ```
  MOD S1SMARTRULE: UETYPE=ANDROID, ATTACHCTRLRULE=PARKAPNACT-1, PDNCONNCTRLRULE=PARKAPNACT-1;
  ```
