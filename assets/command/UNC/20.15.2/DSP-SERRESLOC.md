---
id: UNC@20.15.2@MMLCommand@DSP SERRESLOC
type: MMLCommand
name: DSP SERRESLOC（显示业务资源部署位置）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SERRESLOC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 虚拟化和弹性伸缩
- 业务资源部署位置
status: active
---

# DSP SERRESLOC（显示业务资源部署位置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询业务资源在整系统各进程上的部署情况。

## 注意事项

- 该命令执行后立即生效。

- 该命令输入参数(除了业务资源类型)不作为过滤参数，执行该命令后，会查询系统所有保存结果。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERRESTYPE | 业务资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的资源类型。<br>取值范围：<br>- “RM_TYPE_USER(USER)”<br>- “RM_TYPE_DMLNK(DMLNK)”<br>- “RM_TYPE_S1ECMCONN(S1ECMCONN)”<br>- “RM_TYPE_S1UCMCONN(S1UCMCONN)”<br>- “RM_TYPE_GTPCPATH(GTPCPATH)”<br>- “RM_TYPE_GTPUPATH(GTPUPATH)”<br>- “RM_TYPE_DNSCONN(DNSCONN)”<br>- “RM_TYPE_M3UALNK(M3UALNK)”<br>- “RM_TYPE_GTPUPDP(GTPUPDP)”<br>- “RM_TYPE_SGSVLRLNK(SGSVLRLNK)”<br>- “RM_TYPE_IUUSRCONN(IUUSRCONN)”<br>- “RM_TYPE_GBCELL(GBCELL)”<br>- “RM_TYPE_GBUSER(GBUSER)”<br>- “RM_TYPE_GACONN(GACONN)”<br>- “RM_TYPE_NSE(NSE)”<br>- “RM_TYPE_LCSAPLNK(LCSAPLNK)”<br>- “RM_TYPE_SBCAPLNK(SBCAPLNK)”<br>- “RM_TYPE_NGAPLNK(NGAPLNK)”<br>默认值：无<br>说明：目前暂不支持RM_TYPE_LCSAPLNK和RM_TYPE_SBCAPLNK。 |
| RUNAME | RU名称 | 参数含义：该参数用于指定<br>SPU<br>资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| SPECPROCTYPE | 进程类型 | 参数含义：该参数用于指定查询进程的类型。<br>取值范围：<br>- “SPP(SPP)”<br>- “SGP(SGP)”<br>- “GBP(GBP)”<br>- “LCP(LCP)”<br>- “UPP(UPP)”<br>- “CDP(CDP)”<br>- “OMP(OMP)”<br>默认值：无 |
| SPECPROCID | 进程序列号 | 参数含义：该参数用于指定查询进程的序列号。<br>取值范围：0~254<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过<br>**LST VNFC**<br>命令查询得到。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SERRESLOC]] · 业务资源部署位置（SERRESLOC）

## 使用实例

查询“USER”资源部署情况：DSP SERRESLOC: SERRESTYPE=RM_TYPE_USER, SERVICETYPE="USN_VNFC" ;

```
%%DSP SERRESLOC:SERRESTYPE=RM_TYPE_USER, SERVICETYPE="USN_VNFC";%%
RETCODE = 0  执行成功。

输出结果如下
------------------
        业务资源类型             业务资源逻辑标识       RU名称      进程类型        进程序列号 
        USER                     16                     SPU1        SPP             0                  
        USER                     15                     SPU1        SPP             0                  
        USER                     14                     SPU1        SPP             0                  
        USER                     13                     SPU1        SPP             0                  
        USER                     12                     SPU1        SPP             0                  
        USER                     11                     SPU1        SPP             0                  
        USER                     10                     SPU1        SPP             0                  
        USER                     9                      SPU1        SPP             0                  
        USER                     8                      SPU1        SPP             0                  
        USER                     7                      SPU1        SPP             0                  
        USER                     6                      SPU1        SPP             0                  
        USER                     5                      SPU1        SPP             0                  
        USER                     4                      SPU1        SPP             0                  
        USER                     3                      SPU1        SPP             0                  
        USER                     2                      SPU1        SPP             0                  
        USER                     1                      SPU1        SPP             0                  
        USER                     0                      SPU1        SPP             0                  
        (Number of results = 17)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SERRESLOC.md`
