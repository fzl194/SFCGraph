# 查询CSLB进程（DSP LBPROC）

- [命令功能](#ZH-CN_CONCEPT_0129627093__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0129627093__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0129627093__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0129627093__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0129627093__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0129627093__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0129627093)

查询CSLB的进程信息。

#### [注意事项](#ZH-CN_CONCEPT_0129627093)

- 需要在CSLB RU拉起后才能使用这个命令。
- 该命令批量下发可能导致执行超时。

#### [操作用户权限](#ZH-CN_CONCEPT_0129627093)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0129627093)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：RU名称<br>默认值：无<br>取值范围：0 ~ 63个字符串 |
| PROCTYPE | 进程类型 | 可选必选说明：必选参数<br>默认值：无<br>取值范围：<br>- “PROC_TYPE_MOMP(PROC_MOMP) ”<br>- “PROC_TYPE_MNCP(PROC_MNCP) ”<br>- “PROC_TYPE_MLBP(PROC_MLBP) ”<br>- “PROC_TYPE_MPEP(PROC_MPEP) ”<br>- “PROC_TYPE_MPCP(PROC_MPCP) ” |

#### [使用实例](#ZH-CN_CONCEPT_0129627093)

查询CSLB的进程信息

%%DSP LBPROC: PROCTYPE=PROC_TYPE_MOMP;%%

```
RETCODE = 0  操作成功

结果如下:

-------------------------
      RU名称  =  CSLB_OM_RU_0001
    进程类型  =  PROC_MOMP
      进程号  =  1
    进程角色  =  主
进程业务状态  =  正常
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0129627093)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RU名称 | 参数含义：RU名称 |
| 进程类型 | 参数含义：该参数用于表示进程的类型<br>取值范围：<br>- “PROC_TYPE_MOMP(PROC_MOMP) ”<br>- “PROC_TYPE_MNCP(PROC_MNCP) ”<br>- “PROC_TYPE_MLBP(PROC_MLBP) ”<br>- “PROC_TYPE_MPEP(PROC_MPEP) ”<br>- “PROC_TYPE_MPCP(PROC_MPCP) ” |
| 进程号 | 参数含义：该参数用于表示进程序号 |
| 进程角色 | 参数含义：该参数用于表示进程的角色<br>取值范围：<br>- “PROC_MASTER(主)”<br>- “PROC_SLAVE(从)”<br>- “PROC_STANDBY(备)” |
| 进程业务状态 | 参数含义：该参数用于表示进程的业务状态，代表当前进程是否可以提供服务<br>取值范围：<br>- “PROC_FAULT(故障)”<br>- “PROC_NORMAL(正常)” |
