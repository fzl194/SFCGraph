---
id: UNC@20.15.2@MMLCommand@DSP SNDCP
type: MMLCommand
name: DSP SNDCP（显示SNDCP参数状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SNDCP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- SNDCP参数
status: active
---

# DSP SNDCP（显示SNDCP参数状态）

## 功能

**适用网元：SGSN**

该命令用于查询当前SNDCP层系统参数状态。系统初始化时会加载数据配置表中的SNDCP层参数配置数据，当使用SET SNDCP修改数据库中的配置后，新修改的数据并不会即时生效，所以此时数据配置表中的配置与当前节点使用的配置不一致，需要重启GBP进程使之生效。该命令的功能为查询进程当前使用的配置。关于数据表中的配置数据，请使用 [**LST SNDCP**](查询SNDCP参数(LST SNDCP)_72225705.md) 命令查询。

## 注意事项

- 无参数，表示查询SGSN系统内所有SNDCP状态信息。
- 输入参数“RUNAME”，表示查询指定RU上所有SNDCP状态信息。
- 只能对GBP进程进行查询。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划。<br>取值范围：0~63 位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SNDCP]] · SNDCP参数状态（SNDCP）

## 使用实例

查询SNDCP参数:

DSP SNDCP:;

```
%%DSP SNDCP:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
RU名称            进程号    操作结果    最大缓冲N-PDU数    每个NSAPI最大缓冲N-PDU数    负流量阈值（KB）

USN_SP_RU_0065    0         成功        20000              5                           10              
USN_SP_RU_0064    1         成功        20000              5                           10              
USN_SP_RU_0065    1         成功        20000              5                           10              
USN_SP_RU_0064    0         成功        20000              5                           10              
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SNDCP参数状态(DSP-SNDCP)_26305836.md`
