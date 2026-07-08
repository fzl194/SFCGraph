# 显示业务资源部署位置(DSP SERRESLOC)

- [命令功能](#ZH-CN_MMLREF_0000001126306176__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126306176__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126306176__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126306176__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126306176__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126306176__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126306176__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126306176)

**适用网元：SGSN、MME**

该命令用于查询业务资源在整系统各进程上的部署情况。

#### [注意事项](#ZH-CN_MMLREF_0000001126306176)

- 该命令执行后立即生效。

- 该命令输入参数(除了业务资源类型)不作为过滤参数，执行该命令后，会查询系统所有保存结果。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126306176)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126306176)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126306176)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERRESTYPE | 业务资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的资源类型。<br>取值范围：<br>- “RM_TYPE_USER(USER)”<br>- “RM_TYPE_DMLNK(DMLNK)”<br>- “RM_TYPE_S1ECMCONN(S1ECMCONN)”<br>- “RM_TYPE_S1UCMCONN(S1UCMCONN)”<br>- “RM_TYPE_GTPCPATH(GTPCPATH)”<br>- “RM_TYPE_GTPUPATH(GTPUPATH)”<br>- “RM_TYPE_DNSCONN(DNSCONN)”<br>- “RM_TYPE_M3UALNK(M3UALNK)”<br>- “RM_TYPE_GTPUPDP(GTPUPDP)”<br>- “RM_TYPE_SGSVLRLNK(SGSVLRLNK)”<br>- “RM_TYPE_IUUSRCONN(IUUSRCONN)”<br>- “RM_TYPE_GBCELL(GBCELL)”<br>- “RM_TYPE_GBUSER(GBUSER)”<br>- “RM_TYPE_GACONN(GACONN)”<br>- “RM_TYPE_NSE(NSE)”<br>- “RM_TYPE_LCSAPLNK(LCSAPLNK)”<br>- “RM_TYPE_SBCAPLNK(SBCAPLNK)”<br>- “RM_TYPE_NGAPLNK(NGAPLNK)”<br>默认值：无<br>说明：目前暂不支持RM_TYPE_LCSAPLNK和RM_TYPE_SBCAPLNK。 |
| RUNAME | RU名称 | 参数含义：该参数用于指定<br>SPU<br>资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| SPECPROCTYPE | 进程类型 | 参数含义：该参数用于指定查询进程的类型。<br>取值范围：<br>- “SPP(SPP)”<br>- “SGP(SGP)”<br>- “GBP(GBP)”<br>- “LCP(LCP)”<br>- “UPP(UPP)”<br>- “CDP(CDP)”<br>- “OMP(OMP)”<br>默认值：无 |
| SPECPROCID | 进程序列号 | 参数含义：该参数用于指定查询进程的序列号。<br>取值范围：0~254<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过<br>**LST VNFC**<br>命令查询得到。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126306176)

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

#### [输出结果说明](#ZH-CN_MMLREF_0000001126306176)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 业务资源类型 | 查询的资源类型 |
| 业务资源逻辑标识 | 业务资源逻辑标识 |
| RU名称 | 该参数用于指定<br>SPU<br>资源单元名。 |
| 进程类型 | 资源所在的进程类型 |
| 进程序列号 | 资源所在的进程序列号 |
