---
id: UNC@20.15.2@MMLCommand@DSP DMLNK
type: MMLCommand
name: DSP DMLNK（显示Diameter链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DMLNK
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
- 信令传输管理
- Diameter管理
- Diameter链路
status: active
---

# DSP DMLNK（显示Diameter链路状态）

## 功能

**适用网元：SGSN、MME**

该命令用于查看Diameter链路状态。

## 注意事项

- 该命令执行后立即生效。
- 如果查询结果中某条链路的状态信息显示为NULL，可以确定该链路所在SGP进程故障。告警台会存在告警ID为1003的“模块故障”告警。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKIDX | 链路索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的Diameter链路的索引。<br>取值范围：0~1279<br>默认值：无<br>说明：如果不输入，表示查询系统内所有Diameter链路的状态。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMLNK]] · Diameter链路配置（DMLNK）

## 使用实例

1. 不输入查询参数，查询所有Diameter链路状态信息：
  DSP DMLNK:;
  ```
  %%DSP DMLNK:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
  链路索引    链路名称     RU名称            进程号        链路状态

  2           noname       USN_SP_RU_0066    1              故障        
  1           noname       USN_SP_RU_0066    3              故障        
  0           noname       USN_SP_RU_0066    4              故障        
  6           noname       USN_SP_RU_0066    2              故障        
  (结果个数 = 4)
  ---    END
  ```
2. 输入Diameter链路索引，查询指定的Diameter链路状态信息：
  DSP DMLNK: LINKIDX=0;
  ```
  %%DSP DMLNK: LINKIDX=0;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------

     链路索引  =  0
     链路名称  =  noname
       RU名称  =  USN_SP_RU_0066
     进程号   =  4
     链路状态  =  故障
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示Diameter链路状态(DSP-DMLNK)_72225955.md`
