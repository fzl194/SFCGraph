---
id: UNC@20.15.2@MMLCommand@DSP SIGSUPPRESS
type: MMLCommand
name: DSP SIGSUPPRESS（显示S11接口信令风暴抑制功能的控制与统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SIGSUPPRESS
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
- 信令抑制管理
- S11接口故障场景信令抑制管理
status: active
---

# DSP SIGSUPPRESS（显示S11接口信令风暴抑制功能的控制与统计信息）

## 功能

**适用网元：MME**

该命令用于查询S11接口信令风暴抑制功能的控制与统计信息，控制信息包括：抑制用户数控制值、抑制分离速率（个/秒）、抑制功能启控状态，统计信息包括：流程未抑制的次数、流程被抑制的次数、抑制用户数、抑制用户被分离的次数、抑制用户被恢复的次数。

## 注意事项

当 [**SET SIGSUPPRESS**](设置S11接口信令风暴抑制功能参数(SET SIGSUPPRESS)_72345767.md) 命令中的 “S11接口信令抑制开关” 从 “OFF(关闭)” 修改为 “ON(开启)” 时，统计信息中的 “流程未抑制的次数” 、 “流程被抑制的次数” 、 “抑制用户被分离的次数” 和 “抑制用户被恢复的次数” 会清零。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是查询S11接口信令风暴抑制功能的控制信息或统计信息。<br>数据来源：本端规划<br>取值范围：<br>- “CTRL(控制信息)”<br>- “PERF(统计信息)”<br>- “ALL(所有信息)”<br>默认值：<br>“ALL(所有信息)” |
| QUERYSCOPE | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是按进程方式查询或整系统方式查询S11接口信令风暴抑制功能的控制信息和统计信息。<br>数据来源：本端规划<br>取值范围：<br>- “SUMMARY(整系统查询)”<br>- “PROC(按进程查询)”<br>默认值：<br>“SUMMARY(整系统查询)” |
| RUNAME | RU名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件：该参数在<br>“查询方式”<br>配置为<br>“PROC(按进程查询)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1～63位字符串<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于显示业务进程所属的SPP进程序号。<br>前提条件：该参数在<br>“查询方式”<br>配置为<br>“PROC(按进程查询)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0～20<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SIGSUPPRESS]] · S11接口信令风暴抑制功能的控制与统计信息（SIGSUPPRESS）

## 使用实例

按照“查询类型为ALL(所有信息)、查询方式为SUMMRY(整系统查询)”显示S11接口信令风暴抑制功能的控制信息与统计信息：

DSP SIGSUPPRESS: QUERYTYPE=ALL,QUERYSCOPE=SUMMARY;

```
%%DSP SIGSUPPRESS: QUERYTYPE=ALL,QUERYSCOPE=SUMMARY;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 RU名称               进程号  抑制用户数控制值  抑制分离速率（个/秒）  抑制功能启控状态  流程未抑制的次数  流程被抑制的次数  抑制用户数  抑制用户被分离的次数  抑制用户被恢复的次数

 USN_SP_RU_0065       2       40625             45                     未启控状态        0                 0                 0           0                     0                   
 USN_SP_RU_0065       0       40625             45                     未启控状态        0                 0                 0           0                     0                   
 USN_SP_RU_0064       0       40625             45                     未启控状态        0                 0                 0           0                     0                   
 USN_SP_RU_0064       1       40625             45                     未启控状态        0                 0                 0           0                     0                   
 USN_SP_RU_0064       4       40625             45                     未启控状态        0                 0                 0           0                     0                   
 USN_SP_RU_0064       2       40625             45                     未启控状态        0                 0                 0           0                     0                   
 USN_SP_RU_0065       3       40625             45                     未启控状态        0                 0                 0           0                     0                   
 USN_SP_RU_0065       1       40625             45                     未启控状态        0                 0                 0           0                     0                   
 USN_SP_RU_0064       3       40625             45                     未启控状态        0                 0                 0           0                     0                   
 USN_SP_RU_0065       4       40625             45                     未启控状态        0                 0                 0           0                     0                   

仍有后续报告输出
---    END

+++    USN/*MEID:9 MENAME:USN34*/        2016-01-04 15:04:46+08:00
O&M    #45
%%DSP SIGSUPPRESS: QUERYTYPE=ALL,QUERYSCOPE=SUMMARY;%%
RETCODE = 0  操作成功。

汇总信息如下
--------------
    流程未抑制的次数  =  0
    流程被抑制的次数  =  0
          抑制用户数  =  0
抑制用户被分离的次数  =  0
抑制用户被恢复的次数  =  0
(结果个数 = 11)

共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SIGSUPPRESS.md`
