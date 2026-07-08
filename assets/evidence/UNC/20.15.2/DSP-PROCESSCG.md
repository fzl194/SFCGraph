# 查询CG进程信息（DSP PROCESSCG）

- [命令功能](#ZH-CN_CONCEPT_0252418146__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0252418146__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0252418146__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0252418146__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0252418146__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0252418146__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0252418146__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0252418146)

该命令用于请求系统显示CG_VNFC下进程的状态信息和静态配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0252418146)

- 该命令只适用于业务进程范围，不能查询VNFP和VNRS的进程信息。
- 系统在执行该命令时需要消耗主机一定的CPU资源，这种CPU资源的消耗与操作员需要查询的进程数成正比，为尽量减少查询大量进程状态时对主机CPU资源的消耗，建议操作员输入具体的“进程类型”

#### [本地用户权限](#ZH-CN_CONCEPT_0252418146)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0252418146)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0252418146)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：进程所在资源单元的名称<br>数据来源：通过<br>[**DSP RU**](../../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令可以查询资源单元名称。<br>取值范围：字符串形式，不支持空格和符号'?'，区分大小写，字符串长度为1～63<br>默认值：无<br>配置原则：无 |
| PROCESSTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：进程类型<br>默认值：无<br>数据来源：整网规划<br>取值范围：<br>- “UNIPLT_MPU_SMU(UNIPLT_MPU_SMU) ”<br>- “UNIPLT_LPU_SMU(UNIPLT_LPU_SMU) ”<br>- “GBP(GBP) ”<br>- “LCP(LCP) ”<br>- “OMP(OMP) ”<br>- “UPP(UPP) ” |
| SAMEPROCTYPEINS | 同类进程实例号 | 可选必选说明：可选参数<br>参数含义：同类进程在资源单元上的实例ID<br>默认值：无<br>数据来源：无<br>取值范围：0-63<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0252418146)

```
查询资源单元CG_OM_RU_0001的UNIPLT_MPU_SMU进程的信息:
DSP PROCESSCG:RUNAME="CG_OM_RU_0001",PROCESSTYPE=UNIPLT_MPU_SMU;
%%/*445*/DSP PROCESSGB:RUNAME="CG_OM_RU_0001",PROCESSTYPE=UNIPLT_MPU_SMU,SERVICETYPE="CG_VNFC";%%
RETCODE = 0  操作成功。

结果如下
--------
          进程类型  =  UNIPLT_MPU_SMU
            进程ID  =  1001
            RU名称  =  CG_OM_RU_0001
  进程在RU的实例ID  =  0
          进程状态  =  正常
    同类进程实例号  =  0
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0252418146)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 进程类型 | 查询的进程类型 |
| 进程ID | 查询的进程ID |
| RU名称 | 查询的进程所在的资源单元名称 |
| 进程在Ru的实例ID | 查询的进程在资源单元上的实例ID |
| 进程状态 | 查询的进程可用状态<br>- 正常：表示进程状态可用<br>- 异常：表示进程状态不可用 |
| 同类进程实例号 | 查询的进程对应同类进程在资源单元上的实例号 |
