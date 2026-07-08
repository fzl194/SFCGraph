---
id: UNC@20.15.2@MMLCommand@DSP LINKINFO
type: MMLCommand
name: DSP LINKINFO（显示链路信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LINKINFO
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 链路状态
status: active
---

# DSP LINKINFO（显示链路信息）

## 功能

**适用网元：MME**

此命令用于查询链路历史状态信息。

## 注意事项

此命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待查询链路所在的RU名称。该参数可以通过<br>[DSP RU](../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值 ：无 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路的进程类型。<br>取值范围：<br>- “SGP(SGP)”<br>- “UPP(UPP)”<br>默认值：无<br>配置原则：当前只支持SGP进程查询。 |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：待查询链路所在的进程号。<br>取值范围： 0~4294967295<br>默认值 ：无 |
| LINKTYPE | 链路类型 | 可选必选说明：必选参数<br>参数含义：待查询链路的链路类型<br>取值范围：<br>- DNSLNK(DNSLNK)<br>- DMLNK(DMLNK)<br>- GTPCLNK(GTPCLNK)<br>- GTPULNK(GTPULNK)<br>- LCSLNK(LCSLNK)<br>- M3UALNK(M3UALNK)<br>- NSVCLNK(NSVCLNK)<br>- S1APLNK(S1APLNK)<br>- SBCLNK(SBCLNK)<br>- SGSLNK(SGSLNK)<br>默认值 ：无<br>配置原则：当前只支持查询S1AP链路（S1APLNK）。 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>**LST VNFC**<br>命令查询得到。<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：<br>如果要查询GTPU的链路历史状态，则SERVICETYPE需要填写USN的名称，否则，SERVICETYPE需要填写LINK的名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LINKINFO]] · 链路信息（LINKINFO）

## 使用实例

查询S1AP链路信息，RU名称为LINK_SP_RU_0064，进程类型为SGP，进程号为1，可以用如下命令：

```
DSP LINKINFO: RUNAME="LINK_SP_RU_0064", PROCTYPE=SGP, PROCID=1,LINKTYPE=S1APLNK, SERVICETYPE="LINK_VNFC";
```

```
%%DSP LINKINFO: RUNAME="LINK_SP_RU_0064", PROCTYPE=SGP, PROCID=1, LINKTYPE=S1APLNK, SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
链路类型    IP类型    本端地址1      本端地址2    本端端口号    对端地址1       对端地址2    对端端口号      链路状态变更    变更时间戳             服务名称
S1APLNK     IPv4      192.168.15.1   0.0.0.0      36412         192.168.15.2    0.0.0.0      2011            UP->DOWN        2021-05-25 22:48:45    LINK_VNFC

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LINKINFO.md`
