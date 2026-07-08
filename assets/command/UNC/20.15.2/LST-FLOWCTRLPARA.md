---
id: UNC@20.15.2@MMLCommand@LST FLOWCTRLPARA
type: MMLCommand
name: LST FLOWCTRLPARA（查询流控系统参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FLOWCTRLPARA
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
- 操作维护
- 设备管理
- 流控管理
- 系统流控参数管理
status: active
---

# LST FLOWCTRLPARA（查询流控系统参数）

## 功能

**适用网元：SGSN、MME**

该命令用于显示某个进程上每秒数据流量的接入限制数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的类型。<br>数据来源：整网规划<br>取值范围：<br>- “SPP(SPP)”<br>- “SGP(SGP)”<br>- “GBP(GBP)”<br>- “UPP(UPP)”<br>系统初始设置值：无 |

## 操作的配置对象

- [流控系统参数（FLOWCTRLPARA）](configobject/UNC/20.15.2/FLOWCTRLPARA.md)

## 使用实例

查询某个进程上每秒数据流量的接入限制数，进程类型为GBP：LST FLOWCTRLPARA: PROCTYPE=GBP;

LST FLOWCTRLPARA:;

```
%%LST FLOWCTRLPARA: PROCTYPE=GBP;%% 
RETCODE = 0  操作成功。

查询结果如下
------------------------
                     进程类型  =  GBP
                   窗口最小值  =  30
                   窗口最大值  =  5000
           2G用户面窗口最小值  =  2500
           2G用户面窗口最大值  =  16000
             2G寻呼窗口最大值  =  900
             S1寻呼窗口最小值  =  NULL
             S1寻呼窗口最大值  =  NULL
                丢包率告警阈值 =  5
             业务权重获取方式  =  统计学习
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询流控系统参数(LST-FLOWCTRLPARA)_72345773.md`
