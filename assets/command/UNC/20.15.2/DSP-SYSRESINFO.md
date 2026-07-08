---
id: UNC@20.15.2@MMLCommand@DSP SYSRESINFO
type: MMLCommand
name: DSP SYSRESINFO（显示系统资源使用信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SYSRESINFO
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
- 公共信令调测
- 系统资源
status: active
---

# DSP SYSRESINFO（显示系统资源使用信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询系统资源使用信息。当前仅支持查询UE Radio Capability信元内存使用信息。

## 注意事项

该命令在查询UE Radio Capability信元内存使用信息时，仅用于查询UE Radio Capability信元超过132字节时的内存使用信息。UE Radio Capability信元不超过132字节时，系统会将该信元直接保存在用户上下文中，不需要额外占用内存进行保存。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESTYPE | 资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要查询的资源类型<br>数据来源：本端规划<br>取值范围：<br>- “E_SYSRESINFO_UERADIOCAP”：UE Radio Capability信元内存使用信息。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件：该参数在<br>“资源类型”<br>配置为<br>“UE Radio Capability信元内存使用信息”<br>后生效。<br>数据来源：本端规划<br>取值范围：1～63位字符串<br>默认值：无 |
| PROCTYPE | 进程类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定需要查询的进程类型<br>前提条件：该参数在<br>“资源类型”<br>配置为<br>“UE Radio Capability信元内存使用信息”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “SPP(SPP)”<br>- “SGP(SGP)”<br>- “GBP(GBP)”<br>- “CDP(CDP)”<br>- “LCP(LCP)”<br>- “OMP(OMP)”<br>- “UPP(UPP)”<br>默认值：无<br>说明：进程类型和进程号必须同时输入或同时不输入。 |
| PRON | 进程号 | 可选必选说明：条件可选参数<br>参数含义：参数用于指定需要查询的进程号<br>前提条件：该参数在<br>“资源类型”<br>配置为<br>“UE Radio Capability信元内存使用信息”<br>后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~20。<br>默认值：无<br>说明：当需要按进程号查询时，必须要输入对应的RU名称。 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过VNFP上的<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SYSRESINFO]] · 系统资源使用信息（SYSRESINFO）

## 使用实例

按照“E_SYSRESINFO_UERADIOCAP”显示UE Radio Capability信元内存使用信息：

DSP SYSRESINFO: RESTYPE=E_SYSRESINFO_UERADIOCAP, SERVICETYPE="USN_VNFC";

```
%%DSP SYSRESINFO: RESTYPE=E_SYSRESINFO_UERADIOCAP
, SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功

查询结果如下
--------------
资源类型                                RU名称            进程类型     进程号     资源总量     资源已使用量     资源使用率

UE Radio Capability信元内存使用信息     USN_SP_RU_0064    SPP          0          6375000      0                0             
UE Radio Capability信元内存使用信息     USN_SP_RU_0065    SPP          0          6375000      0                0 
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示系统资源使用信息(DSP-SYSRESINFO)_72225559.md`
