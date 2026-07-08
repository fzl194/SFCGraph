# 修改DDoS Check是否使能

- [操作场景](#ZH-CN_OPI_0124082264__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0124082264__1.3.2)
- [必备事项](#ZH-CN_OPI_0124082264__1.3.3)
- [操作步骤](#ZH-CN_OPI_0124082264__1.3.4)
- [任务示例](#ZH-CN_OPI_0124082264__1.3.5)

## [操作场景](#ZH-CN_OPI_0124082264)

需要修改DDoS Check是否使能。

> **说明**
> 适用于SGW-U、PGW-U、UPF。

## [对系统的影响](#ZH-CN_OPI_0124082264)

该操作对系统正常运行没有影响。

## [必备事项](#ZH-CN_OPI_0124082264)

前提条件

请仔细阅读 [GWFD-010253 防DDoS功能](../../GWFD-010253 防DDoS功能_67574063.md) 。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**MOD USERPROFILE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/用户模板/修改用户模板（MOD USERPROFILE）_82837280.md) | 用户模板名称（USERPROFILENAME） | up_test | 本端规划 | - |
| [**MOD USERPROFILE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/用户模板/修改用户模板（MOD USERPROFILE）_82837280.md) | 防DDoS攻击标记（DDOSCHECK） | ENABLE | 本端规划 | - |

## [操作步骤](#ZH-CN_OPI_0124082264)

修改UserProfile的DDoS Check使能。

[**MOD USERPROFILE**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务规则管理/用户模板/修改用户模板（MOD USERPROFILE）_82837280.md)

## [任务示例](#ZH-CN_OPI_0124082264)

任务描述

修改用户模板的DDoS Check使能。

脚本

//修改UserProfile的DDoS Check使能。

```
MOD USERPROFILE:USERPROFILENAME="up_test",DDOSCHECK=ENABLE;
```
