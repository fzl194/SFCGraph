---
id: UNC@20.15.2@MMLCommand@DSP BTRUNCSTATUS
type: MMLCommand
name: DSP BTRUNCSTATUS（显示宽带集群系统TSN状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BTRUNCSTATUS
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 用户数据库管理
status: active
---

# DSP BTRUNCSTATUS（显示宽带集群系统TSN状态）

## 功能

**适用NF：MME**

该命令用于查看宽带集群系统的容灾状态。当宽带集群系统启用异地容灾功能时，MME在Tm1接口与一或多个TSN进行双向的定时探测，TSN侧通过探测消息下发自身状态给MME，指示MME自身的状态发生了变更；MME侧通过TSN的通知或者自己探测的结果来变更自身保存的TSN状态。当宽带集群系统处于容灾主或者单站主状态时，允许接入业务；当系统处于容灾备或检测备状态时，不允许接入业务。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数ID | 参数名称 | 参数说明 |
| --- | --- | --- |
| SHOWDETAILINFO | 显示详细信息 | 可选必选说明：必选参数 。<br>参数含义：用于请求系统是否需要显示详细信息。显示详细信息指每个进程上本地表的信息，非详细信息直接取主进程DDB表信息。<br>数据来源：本端规划。<br>取值范围：枚举类型<br>- “NO(否)”<br>- “YES(是)”<br>默认值：“NO(否)”。 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数 。<br>参数含义：进程类型。<br>数据来源：本端规划。<br>取值范围：枚举类型<br>- “SPP(SPP)”<br>- “SGP(SGP)”<br>默认值：“SPP(SPP)”。 |
| SERVICETYPE | VNFC名称 | 可选必选说明：必选参数<br>参数含义：指定VNFC名称，可以通过UNC MML页面执行<br>**[LST VNFC](../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：SPP配置USN_VNFC的对应名称，SGP配置LINK_VNFC的对应名称 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BTRUNCSTATUS]] · 宽带集群系统TSN状态（BTRUNCSTATUS）

## 使用实例

1. 获取主SPP进程DDB表上的容灾信息：
  ```
  DSP BTRUNCSTATUS: SHOWDETAILINFO=NO, PROCTYPE=SPP, SERVICETYPE="USN_VNFC";
  ```
2. 获取所有SPP进程本地表上的容灾信息：
  ```
  DSP BTRUNCSTATUS: SHOWDETAILINFO=YES, PROCTYPE=SPP, SERVICETYPE="USN_VNFC";
  ```
3. 获取主SGP进程DDB表上的容灾信息：
  ```
  DSP BTRUNCSTATUS: SHOWDETAILINFO=YES, PROCTYPE=SGP, SERVICETYPE="LINK_VNFC";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-BTRUNCSTATUS.md`
