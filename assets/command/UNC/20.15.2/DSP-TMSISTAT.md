---
id: UNC@20.15.2@MMLCommand@DSP TMSISTAT
type: MMLCommand
name: DSP TMSISTAT（查询TMSI资源分配状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TMSISTAT
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
- 系统管理
- 用户数据库管理
status: active
---

# DSP TMSISTAT（查询TMSI资源分配状态）

## 功能

**适用网元：SGSN、MME**

该命令用于查询指定SPP进程、指定P-TMSI/M-TMSI或者指定NRI粒度的TMSI资源使用状态。

## 注意事项

该命令查询到的状态仅在 [**SET SYS**](../系统参数管理/设置系统参数(SET SYS)_72345947.md) 命令的 “TMSIALLOC” 参数配置为 “ENHAN：（增强TMSI分配方式）” ，且复位生效之后有意义。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数ID | 参数名称 | 参数说明 |
| --- | --- | --- |
| QTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置查询的方式。<br>取值范围：<br>- SPP：基于SPP进程查询。<br>- TMSI：基于TMSI查询。<br>- NRI：基于NRI查询。<br>默认值：SPP |
| RUNAME | RU名称 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定节点的RU名称。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件：该参数在<br>“查询类型”<br>参数配置为<br>“基于SPP进程查询”<br>后生效。<br>取值范围：0～63位字符串<br>默认值：无 |
| PROCID | 进程号 | 可选必选说明：条件可选参数<br>参数含义：本参数用于指定节点内SPP进程号。<br>前提条件：该参数在<br>“查询类型”<br>参数配置为<br>“基于SPP进程查询”<br>后生效。<br>取值范围：0～20<br>默认值：无 |
| TMSITYPE | TMSI类型 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指定查询TMSI类型为P-TMSI或M-TMSI。<br>前提条件：该参数在<br>“查询类型”<br>参数配置为<br>“基于SPP进程查询”<br>或<br>“基于TMSI查询”<br>后生效。<br>取值范围：<br>- P-TMSI(P-TMSI)<br>- M-TMSI(M-TMSI)<br>默认值：P-TMSI(P-TMSI) |
| TMSI | TMSI | 可选必选说明：条件必选参数<br>参数含义：需要查询的P-TMSI或者M-TMSI值。<br>前提条件：该参数在<br>“查询类型”<br>参数配置为<br>“基于TMSI查询”<br>后生效。<br>取值范围：0～10位16进制码字符串<br>默认值：无 |
| NRI | NRI | 可选必选说明：条件必选参数<br>参数含义：需要查询的NRI值，NRI（Net Resource Identify网络资源标识），用于标识一个CN节点。<br>前提条件：该参数在<br>“查询类型”<br>参数配置为<br>“基于NRI查询”<br>后生效。<br>取值范围：0～1023<br>默认值：无 |

## 操作的配置对象

- [TMSI资源分配状态（TMSISTAT）](configobject/UNC/20.15.2/TMSISTAT.md)

## 使用实例

查询SPP指定RU名称和进程号的M-TMSI分配情况的统计：

```
DSP TMSISTAT: QTYPE=SPP, RUNAME="USN_SP_RU_0064", PROCID=0, TMSITYPE=M-TMSI;
```

```
%%DSP TMSISTAT: QTYPE=SPP, RUNAME="USN_SP_RU_0064", PROCID=0, TMSITYPE=M-TMSI;%%
RETCODE = 0  操作成功。

操作结果如下
------------------------
常用区总个数  =  0
倒换区总个数  =  512
仍有后续报告输出
---    END

%%DSP TMSISTAT: QTYPE=SPP, RUNAME="USN_SP_RU_0064", PROCID=0, TMSITYPE=M-TMSI;%%
RETCODE = 0  操作成功。

操作结果如下
------------------------
RU 名称           进程号        CSDB段号        常用区占用个数          倒换区占用个数          TMSI资源块算数平均偏差          段内静态用户数          分配失败个数
                                                                                                                                                                                               
USN_SP_RU_0064    0             111             0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             107             0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             103             0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             102             0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             101             0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             99              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             96              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             94              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             91              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             90              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             88              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             87              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             84              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             83              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             82              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             80              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             78              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             76              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             74              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             73              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             72              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             69              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             68              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             65              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             62              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             61              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             53              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             49              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             45              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             44              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             29              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             25              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             20              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             18              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             15              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             12              0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             6               0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             2               0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             1               0                       0                       0                               0                       0                       
USN_SP_RU_0064    0             0               0                       0                       0                               0                       0                       
(结果个数 = 40)
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TMSI资源分配状态(DSP-TMSISTAT)_26146356.md`
