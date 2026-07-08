---
id: UNC@20.15.2@MMLCommand@DSP FLOWCTRLSTAT
type: MMLCommand
name: DSP FLOWCTRLSTAT（显示流控统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FLOWCTRLSTAT
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
- 通信调测
status: active
---

# DSP FLOWCTRLSTAT（显示流控统计信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询流控统计。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要查询的SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1-63位字符串。<br>默认值：无 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于要查询的进程类型。<br>取值范围：<br>- “SPP(SPP)”<br>- “SGP(SGP)”<br>- “GBP(GBP)”<br>- “CDP(CDP)”<br>- “UPP(UPP)”<br>- “LCP(LCP)”<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要查询的进程序号。<br>取值范围：0~20<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FLOWCTRLSTAT]] · 流控统计信息（FLOWCTRLSTAT）

## 使用实例

查询LINK_SP_RU_0064上0号SGP进程：

DSP FLOWCTRLSTAT: RUNAME="LINK_SP_RU_0064", PROCTYPE=SGP, PROCNO=0, SERVICETYPE="LINK_VNFC";

```
%%DSP FLOWCTRLSTAT: RUNAME="LINK_SP_RU_0064", PROCTYPE=SGP, PROCNO=0, 
SERVICETYPE="LINK_VNFC"
;%%
RETCODE = 0  操作成功

查询结果如下
------------
输出结果  =  	RU CPU:47 	Proc Cpu:36 	WAL_Sig:15000 	PreMsgCount_Sig:0
	WAL_Data:10000 	PreMsgCount_Data:0 	WAL_NS:500 	PreMsgCount_NS:0
--------------------------------------
	msg type                                 self protect pass    self protect reject  queue pass           queue reject
	SCTPADAPT Choose SGP Init Msg            31542                31                   0                    0                   
	SCTPADAPT Choose SGP Tbit Msg            394                  4                    0                    0                   

服务名称  =  LINK_VNFC
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-FLOWCTRLSTAT.md`
