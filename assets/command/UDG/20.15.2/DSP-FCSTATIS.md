---
id: UDG@20.15.2@MMLCommand@DSP FCSTATIS
type: MMLCommand
name: DSP FCSTATIS（显示流控统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FCSTATIS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 流控管理
status: active
---

# DSP FCSTATIS（显示流控统计）

## 功能

该命令用于查询进程运行中的调试信息。当管理员需要查询流控功能当前的统计信息时，可以使用本命令查询。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPRCOND | 调试类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询消息发送对象类型。<br>数据来源：本端规划<br>取值范围：<br>- “CELLID（进程标识）”：进程标识<br>- “CELLTYPE（进程类型标识）”：进程类型标识<br>默认值：无<br>配置原则：无 |
| CELLID | 进程标识 | 可选必选说明：该参数在"OPRCOND"配置为"CELLID"时为条件必选参数。<br>参数含义：该参数用于表示流控查询消息发给某一个进程，进程标识可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |
| CELLTYPE | 进程类型 | 可选必选说明：该参数在"OPRCOND"配置为"CELLTYPE"时为条件必选参数。<br>参数含义：该参数用于表示流控查询消息发给某一类进程，进程标识可以通过使用命令<br>[**DSP MSPROCTYPE**](../../可靠性管理/微服务可靠性管理/显示微服务进程类型（DSP MSPROCTYPE）_09587905.md)<br>获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| QUERYCOND | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询对象类型。<br>数据来源：本端规划<br>取值范围：<br>- “QUERYALL（查询全部套餐）”：查询全部套餐<br>- “QUERYONE（查询指定套餐）”：查询指定套餐<br>默认值：无<br>配置原则：无 |
| SERVICENAME | 服务名称 | 可选必选说明：该参数在"QUERYCOND"配置为"QUERYONE"时为条件必选参数。该参数在"QUERYCOND"配置为"QUERYALL"时为条件可选参数。<br>参数含义：该参数用于表示服务名称，根据服务名称来查询对应的套餐信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |
| SERVICETYPE | 服务类型 | 可选必选说明：该参数在"QUERYCOND"配置为"QUERYONE"时为条件必选参数。<br>参数含义：该参数用于表示服务类型，根据服务类型来查询对应的套餐信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| GROUPID | 服务组标识 | 可选必选说明：该参数在"QUERYCOND"配置为"QUERYONE"时为条件必选参数。<br>参数含义：该参数用于表示服务组标识，根据服务组标识来查询对应的套餐信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| CASEID | 套餐标识 | 可选必选说明：该参数在"QUERYCOND"配置为"QUERYONE"时为条件必选参数。<br>参数含义：该参数用于表示套餐标识，根据套餐标识来查询对应的套餐信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FCSTATIS]] · 流控统计（FCSTATIS）

## 使用实例

DSP FCSTATIS: OPRCOND=CELLID, CELLID="vsm-pod-6b8d786c57-kkrm710-111-1-187__1006__0", QUERYCOND=QUERYALL;

```
%%DSP FCSTATIS: OPRCOND=CELLID, CELLID="vsm-pod-6b8d786c57-kkrm710-111-1-187__1006__0", QUERYCOND=QUERYALL;%%
RETCODE = 0  操作成功
 
结果如下
--------
输出0        输出1        输出2     输出3     输出4     输出5                                            输出6     输出7     输出8     输出9

ServiceName  ServiceType  GroupId   CaseId    ProcId    CellId   
SmcExecSvc   1003         999       0         0         vsm-pod-6b8d786c57-kkrm710-111-1-187__1006__0   -         -         -         -
NodeCpu      CtnCpu       -         -         -         -                                                -         -         -         -
22           5            -         -         -         -                                                -         -         -         -
FcState      WAL          -         -         -         -                                                -         -         -         -
0            0            -         -         -         -                                                -         -         -         -
Priority     Quota        Pass      Pass1s    Reject    Reject1s                                         -         -         -         -
1            0            47443     46        0         0                                                -         -         -         -
2            0            45586     40        0         0                                                -         -         -         -
-            -            -         -         -         -                                                -         -         -         -
(结果个数 = 10)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-FCSTATIS.md`
