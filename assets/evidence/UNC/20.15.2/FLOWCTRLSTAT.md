# 显示流控统计信息(DSP FLOWCTRLSTAT)

- [命令功能](#ZH-CN_MMLREF_0000001126145868__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145868__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145868__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145868__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145868__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145868__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145868__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145868)

**适用网元：SGSN、MME**

该命令用于查询流控统计。

#### [注意事项](#ZH-CN_MMLREF_0000001126145868)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145868)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145868)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145868)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要查询的SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1-63位字符串。<br>默认值：无 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于要查询的进程类型。<br>取值范围：<br>- “SPP(SPP)”<br>- “SGP(SGP)”<br>- “GBP(GBP)”<br>- “CDP(CDP)”<br>- “UPP(UPP)”<br>- “LCP(LCP)”<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要查询的进程序号。<br>取值范围：0~20<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145868)

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

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145868)

| 输出项名称 | 输出项解释 |
| --- | --- |
| msg type | 显示参与流控的消息类型。<br>说明：以下类型的消息流控根据流程控制，报文统计结果中self protect与自保流控无关，仅做数字统计。<br>- get auth set req(Gr HTR)<br>- upd loc req(Gr HTR)<br>- get auth set req(Gr softpara)<br>- upd loc req(Gr softpara)<br>- SCTPADAPT Choose SGP Init Msg<br>- SCTPADAPT Choose SGP Tbit Msg<br>- auth info req(S6x)<br>- upd loc req(S6x) |
