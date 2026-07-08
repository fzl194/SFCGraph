# 停止迁移任务(STP OFFLOAD)

- [命令功能](#ZH-CN_MMLREF_0000001126146092__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146092__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146092__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146092__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146092__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146092__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146092)

**适用网元：SGSN、MME**

此命令用于停止当前正在进行的迁移任务。

#### [注意事项](#ZH-CN_MMLREF_0000001126146092)

- 当由[**STR OFFLOADBYMME**](启动MME迁移任务（STR OFFLOADBYMME）_72345693.md)命令启动的迁移任务结束后，如果需要MME继续接入新用户，则需通过[**SET SYS**](../../系统管理/系统参数管理/设置系统参数(SET SYS)_72345947.md)命令将MME的“设备能力”设置成对应的值。
- 当由[**STR OFFLOADBYSGSN**](启动SGSN迁移任务（STR OFFLOADBYSGSN）_26305904.md)、[**STR OFFLOADBYRNC**](启动RNC迁移任务（STR OFFLOADBYRNC）_72225773.md)、[**STR OFFLOADBYBSC**](启动BSC迁移任务（STR OFFLOADBYBSC）_72225771.md)命令启动的迁移任务结束后，如果需要本SGSN通过指定RNC/BSC继续接入新用户，则需在相应RNC/BSC上将本SGSN的状态恢复为“Normal”。
- 此命令对类型为“IMSI(IMSI)”的迁移任务不生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146092)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146092)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146092)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001126146092)

停止迁移任务：

STP OFFLOAD:;
