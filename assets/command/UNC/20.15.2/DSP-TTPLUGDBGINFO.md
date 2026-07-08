---
id: UNC@20.15.2@MMLCommand@DSP TTPLUGDBGINFO
type: MMLCommand
name: DSP TTPLUGDBGINFO（查询扩展VNFC插件调试信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TTPLUGDBGINFO
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
- 业务调测
- 插件信息查询
- 显示插件调试信息
status: active
---

# DSP TTPLUGDBGINFO（查询扩展VNFC插件调试信息）

## 功能

**适用网元：SGSN、MME**

该命令用以查询USN_VNFC业务进程上扩展VNFC插件的调试信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RU | RU名称 | 可选必选说明：必选参数。<br>参数含义：该参数表示USN_VNFC上待查询的RU的名称。<br>数据来源：本端规划。<br>取值范围：0~63位字符串。<br>默认值：无。 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数。<br>参数含义：该参数表示USN_VNFC上待查询的进程类型。<br>数据来源：本端规划。<br>取值范围：<br>- “SPP(SPP) ”<br>- “UPP(UPP) ”<br>默认值：无。 |
| PROCNO | 进程号 | 可选必选说明：必选参数。<br>参数含义：该参数表示USN_VNFC上待查询的进程编号。<br>数据来源：本端规划。<br>取值范围：0~20。<br>默认值：无。 |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数。<br>参数含义：该参数表示待查询的调试信息类型。<br>数据来源：本端规划。<br>取值范围：<br>- “KEY(KEY信息)”<br>- “TOPO(拓扑信息)”<br>- “COUNT(计数信息)”<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数。<br>此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：SERVICETYPE需要填写LINK、USN或者GB的名称。 |

## 操作的配置对象

- [扩展VNFC插件调试信息（TTPLUGDBGINFO）](configobject/UNC/20.15.2/TTPLUGDBGINFO.md)

## 使用实例

当需要查询USN_SP_RU_0066上0号SPP进程的KEY信息时，可以使用如下命令：

```
DSP TTPLUGDBGINFO: RU="USN_SP_RU_0066", PROCTYPE=SPP, PROCNO=0, QUERYTYPE=KEY, 
SERVICETYPE="USN_VNFC"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询扩展VNFC插件调试信息（DSP-TTPLUGDBGINFO）_26145864.md`
