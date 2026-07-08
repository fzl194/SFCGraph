# 激活MSC Pool内的用户迁移（Gs接口）特性

- [操作场景](#ZH-CN_OPI_0186818610__1.3.1)
- [必备事项](#ZH-CN_OPI_0186818610__1.3.2)
- [操作步骤](#ZH-CN_OPI_0186818610__1.3.3)
- [任务示例](#ZH-CN_OPI_0186818610__1.3.4)

## [操作场景](#ZH-CN_OPI_0186818610)

本操作指导介绍在运行网络中激活 MSC Pool 内的用户迁移（Gs接口）特性的操作过程。

MSC Pool 内的用户迁移（Gs接口）特性是Gs接口的一个增强型功能，当MSC Pool中某个MSC不可用时（如发生故障、升级等）， SGSN 可以下发启动用户迁移命令，将该MSC的状态信息标识为不可用，然后将该MSC上的用户迁移到MSC Pool中的其他MSC上。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0186818610)

前提条件

- 请仔细阅读[WSFD-110001 MSC Pool内的用户迁移（Gs接口）特性概述](特性概述_86818608.md)。
- MSC Pool特性已经正常开通。
- 需要对端网元MSC/ VLR 激活 MSC Pool内的用户迁移（Gs接口）特性。
- 系统支持 Gs接口 ，且接口功能已打开。
- MSC Pool内MSC不唯一。MSC Pool中分配给每个MSC/VLR的V值范围必须是连续的。
- 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 命令 |
| --- | --- | --- | --- | --- |
| [**SET VLROFFLOADINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/MSC POOL管理/VLR迁移配置信息/设置VLR迁移配置信息(SET VLROFFLOADINF)_72345023.md) | 第一阶段迁移时长（FIRSTTM） | 40 | 全网规划 | VLR信息 |
| [**SET VLROFFLOADINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/MSC POOL管理/VLR迁移配置信息/设置VLR迁移配置信息(SET VLROFFLOADINF)_72345023.md) | 第二阶段迁移速度（VLROFFLODSPD） | 30 | 全网规划 | VLR信息 |
| [**STR VLROFFLOAD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/MSC POOL管理/VLR迁移任务/启动VLR迁移任务(STR VLROFFLOAD)_26145420.md) | VLR号（VN） | 8613901205 | 全网规划 | VLR信息 |

## [操作步骤](#ZH-CN_OPI_0186818610)

- 激活特性
    1. 进入 “MML命令行-UNC” 窗口。
    2. 打开本特性的License配置开关。
      [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    3. **可选：**配置迁移第一阶段时长和迁移第二阶段迁移速度。
      [**SET VLROFFLOADINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/MSC POOL管理/VLR迁移配置信息/设置VLR迁移配置信息(SET VLROFFLOADINF)_72345023.md)
      > **说明**
      > 该步骤可选，用户若不设置该参数，则默认第一阶段迁移时长为58分钟，第二阶段迁移速度为20个用户/秒。
- 启动迁移命令
    1. 对需要迁移的MSC/VLR下发启动迁移命令。
      [**STR VLROFFLOAD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/MSC POOL管理/VLR迁移任务/启动VLR迁移任务(STR VLROFFLOAD)_26145420.md)
- 停止迁移命令
    1. 对已经启动迁移命令的MSC/VLR，如果需要停止迁移，下发终止迁移命令。
      [**STP VLROFFLOAD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/MSC POOL管理/VLR迁移任务/停止VLR迁移任务(STP VLROFFLOAD)_72225103.md)
      > **说明**
      > 终止迁移命令只能对迁移状态为“迁移中”的MSC/VLR进行，可以通过执行 [**DSP VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/显示VLR迁移进度(DSP VLR)_26305256.md) 先查看MSC的迁移状态，然后下发终止迁移命令。

## [任务示例](#ZH-CN_OPI_0186818610)

任务描述

启动与本局 SGSN 相连的MSC Pool中一个VLR的迁移，VLR号码为“8613901205”，VLR迁移第一阶段时长为40分钟，VLR迁移速度为30个/秒。在启动一段时间后，停止该VLR的迁移。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2MSCMG02", SWITCH=ENABLE;
```

//配置迁移第一阶段时长和迁移第二阶段迁移速度。

```
SET VLROFFLOADINF: FIRSTTM=40, VLROFFLODSPD=30;
```

//对需要迁移的MSC/VLR下发启动迁移命令。

```
STR VLROFFLOAD: VN="8613901205";
```

//对需要停止迁移的MSC/VLR下发停止迁移命令。

```
STP VLROFFLOAD: VN="8613901205";
```
