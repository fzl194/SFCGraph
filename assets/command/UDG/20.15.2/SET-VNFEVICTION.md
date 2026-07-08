---
id: UDG@20.15.2@MMLCommand@SET VNFEVICTION
type: MMLCommand
name: SET VNFEVICTION（设置网元重调度开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: VNFEVICTION
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 网元管理
status: active
---

# SET VNFEVICTION（设置网元重调度开关）

## 功能

![](设置网元重调度开关（SET VNFEVICTION）_26089552.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当可能会导致业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于设置网元的重调度开关。

开启重调度开关，在虚拟机故障、升级、资源不足等场景下，该虚拟机上的容器会被调度到其他虚拟机节点上。

在I层分批升级时，通过关闭网元的重调度开关，在升级完成后，重新打开网元的重调度开关，保证升级前后的容器仍在原虚拟机节点。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

## 注意事项

- 该命令在执行后立即生效。
- 网元ID必须在系统中存在。

- 该命令中参数“重调度开关”的初始设定值为“On(开启)”。
- 通过该命令设定参数“On(开启)”打开网元的重调度开关，在虚拟机故障、升级、资源不足等场景下，该虚拟机上的容器会被调度到其他虚拟机节点上，可能导致业务受损。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNFID | 网元ID | 可选必选说明：必选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |
| EVICTION | 重调度开关 | 可选必选说明：必选参数。<br>参数含义：网元重调度开关。<br>取值范围：<br>- On(开启)：开启网元重调度开关。<br>- Off(关闭)：关闭网元重调度开关。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [网元重调度策略（VNFEVICTION）](configobject/UDG/20.15.2/VNFEVICTION.md)

## 使用实例

修改网元ID为0的重调度开关为开启。

```
%%SET VNFEVICTION: VNFID=0, EVICTION=On;%%
RETCODE = 0  操作成功
 
操作结果如下
------------
网元ID  节点名称        节点IP          虚拟机ID                          重调度开关  
 
0       10.113.112.79   10.113.112.79   070b9dad6fd94a43af459db9754       开启        
0       10.113.112.197  10.113.112.197  d9524ba42dcf4d8fac2943666c3       开启        
0       10.113.112.222  10.113.112.222  8cde48ddba05482bb0d03d01f82       开启        
(结果个数 = 3)
 
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置网元重调度开关（SET-VNFEVICTION）_26089552.md`
