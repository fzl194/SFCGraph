---
id: UNC@20.15.2@MMLCommand@DSP NBFCSTAT
type: MMLCommand
name: DSP NBFCSTAT（显示NB流控状态统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NBFCSTAT
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- NB-IoT业务流控管理
status: active
---

# DSP NBFCSTAT（显示NB流控状态统计）

## 功能

**适用网元：MME**

该命令用于显示NB-IoT流控功能的相关状态和统计信息。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NB-IoT流控状态统计信息的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “ALL(整系统查询)”<br>- “PROC(按进程查询)”<br>默认值：<br>“ALL(整系统查询)” |
| RUNAME | RU名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件：该参数在<br>“查询方式”<br>配置为<br>“PROC(按进程查询)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1～63位字符串<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要查看流控状态信息对应SPP进程的进程号。<br>前提条件：该参数在<br>“查询方式”<br>配置为<br>“PROC(按进程查询)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0～20<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NBFCSTAT]] · NB流控状态统计（NBFCSTAT）

## 使用实例

按照“查询方式为ALL(整系统查询)”显示NB-IoT流控状态统计：

DSP NBFCSTAT: QUERYTYPE=ALL;

```
%%DSP NBFCSTAT: QUERYTYPE=ALL;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
RU名称               进程号    流控告警状态  流控速率（个/秒）  通过量（个）  拒绝量（个）

USN_SP_RU_0066       0          正常状态      300                 0             0           
USN_SP_RU_0066       3          正常状态      300                 0             0           
USN_SP_RU_0066       1          正常状态      300                 0             0           
USN_SP_RU_0066       4          正常状态      300                 0             0           
USN_SP_RU_0066       2          正常状态      300                 0             0 
(结果个数 = 5)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NBFCSTAT.md`
