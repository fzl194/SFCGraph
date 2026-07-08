---
id: UNC@20.15.2@MMLCommand@DSP SCTPBALANCEINFO
type: MMLCommand
name: DSP SCTPBALANCEINFO（查询SCTP均衡信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SCTPBALANCEINFO
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# DSP SCTPBALANCEINFO（查询SCTP均衡信息）

## 功能

**适用NF：SGSN、MME、AMF**

此命令用于查询系统中指定SGP进程上的eNodeB和gNodeB数目。

## 注意事项

- 此命令执行后立即生效。
- 此命令查询的是汇总结果，基站迁移过程中汇总结果可能存在偏差，需要在系统稳定30s后才能查到准确信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询方式。<br>取值范围：<br>- DISTRIBUTED（分布查询）：用于查询相应SGP进程上的eNodeB和gNodeB数目。如果用户只指定RU名称，则查询指定RU所有SGP进程的eNodeB和gNodeB数目；如果用户不指定任何查询条件，则查询系统中所有SGP进程的eNodeB和gNodeB数目。<br>默认值：“DISTRIBUTED（分布查询）” |
| RUNAME | RU名称 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待查询的RU名称。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值 ：无<br>配置原则：“查询方式”参数设置为“DISTRIBUTED（分布查询）”时，该参数为可选参数。 |
| PN | 进程号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定查询的SGP的进程号。<br>取值范围： 0~11<br>默认值 ：无<br>配置原则：“查询方式”参数设置为“DISTRIBUTED（分布查询）”时，该参数为可选参数。<br>说明：如果输入进程号，必须输入RU名称。 |

## 操作的配置对象

- [SCTP均衡信息（SCTPBALANCEINFO）](configobject/UNC/20.15.2/SCTPBALANCEINFO.md)

## 使用实例

查询系统中所有SGP进程的eNodeB和gNodeB数目，可以用如下命令：

DSP SCTPBALANCEINFO: SRT=DISTRIBUTED;

```
%%DSP SCTPBALANCEINFO: SRT=DISTRIBUTED;%%
RETCODE = 0  操作成功

操作结果如下
------------
RU名称           进程号  eNodeB个数  gNodeB个数  单进程基站总个数

LINK_SP_RU_0064  0       1           0           1 
LINK_SP_RU_0064  1       0           1           1     
(结果个数 = 2)

操作结果如下
------------
eNodeB总个数 = 1
gNodeB总个数 = 1
  基站总个数 = 2
(结果个数 = 2)
---    END 
```

查询LINK_SP_RU_0064上0号SGP进程的eNodeB和gNodeB数目，可以用如下命令：

DSP SCTPBALANCEINFO: SRT=DISTRIBUTED, RUNAME="LINK_SP_RU_0064", PN=0;

```
%%DSP SCTPBALANCEINFO: SRT=DISTRIBUTED, RUNAME="LINK_SP_RU_0064", PN=0;%%
RETCODE = 0  操作成功

操作结果如下
------------
          RU名称  =  LINK_SP_RU_0064
          进程号  =  0
      eNodeB个数  =  1
      gNodeB个数  =  0
单进程基站总个数  =  1
(结果个数 = 1)

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCTP均衡信息(DSP-SCTPBALANCEINFO)_16196710.md`
