---
id: UNC@20.15.2@MMLCommand@DSP HARESULT
type: MMLCommand
name: DSP HARESULT（显示HA选举结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: HARESULT
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 平台调测
- HA选举管理
status: active
---

# DSP HARESULT（显示HA选举结果）

## 功能

**适用网元：SGSN、MME**

该命令用于显示参与HA选举的关键功能模块的主控信息。

HA选举是用于从多个同类进程中选举出主进程和备进程的一套选举机制。

系统管理支持两种控制模式：分布控制模式和全局控制模式。分布控制是指系统内各个进程的资源独立管理，多个进程间松耦合。全局控制是指系统中部署主控模块，同类进程的资源在主控模块中统一管理。

全局控制模式中会将主控模块部署在HA选举的主进程和备进程中，正常运行时只有主进程中的主控模块参与全局管理，备进程作为主进程的备份不参与全局管理。当主进程故障时，备进程中的主控模块接替主进程中的主控模块参与全局管理。

## 注意事项

当选择功能模块为 “ALL（全部）” 时，显示所有HA选举的主控模块的主备信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FUNCMODULE | 功能模块 | 可选必选说明：可选参数<br>参数含义：该参数用于显示HA选举的功能模块。<br>取值范围：<br>- “ALL（全部）”<br>- “HTR（统一HTR功能模块）”<br>- “LICENSE（LICENSE功能模块）”<br>- “SCTP_AM（S1链路接入管理功能模块）”<br>默认值：ALL（全部） |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定待查询的服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HARESULT]] · HA选举结果（HARESULT）

## 使用实例

显示HA选举结果：

DSP HARESULT: SERVICETYPE="USN_VNFC";

```
%%DSP HARESULT: 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
功能模块                   主RU名称            主进程类型     主进程ID      备RU名称           备进程类型    备进程ID  

统一HTR功能模块            USN_SP_RU_0064      LCP            1026          USN_SP_RU_0065     LCP           1089      
LICENSE功能模块            USN_SP_RU_0064      LCP            1026          USN_SP_RU_0065     LCP           1089        
S1链路接入管理功能模块     USN_SP_RU_0064      LCP            1026          USN_SP_RU_0065     LCP           1089        
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-HARESULT.md`
