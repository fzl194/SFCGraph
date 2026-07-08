---
id: UNC@20.15.2@MMLCommand@DSP GTPPDPNUM
type: MMLCommand
name: DSP GTPPDPNUM（显示用户面PDP上下文数目）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPPDPNUM
command_category: 查询类
applicable_nf:
- SGSN
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

# DSP GTPPDPNUM（显示用户面PDP上下文数目）

## 功能

**适用网元：SGSN**

该命令用于查询系统内的PDP数目。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源单元名称。该参数可以通过<br>**DSP RU**<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| GTPSN | 进程序号 | 可选必选说明：条件可选参数<br>输入该参数需要指定RU名称。<br>参数含义：资源单元上的UPP进程号。<br>取值范围：0~20<br>默认值：无 |
| PDPTYPE | 上下文主备状态 | 可选必选说明：可选参数<br>参数含义：上下文主备状态<br>取值范围：<br>- “MASTER（主用状态）”<br>- “STANDBY（备用状态）”<br>默认值：MASTER（主用状态） |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPPDPNUM]] · 用户面PDP上下文数目（GTPPDPNUM）

## 使用实例

1. 查询系统内所有资源单元上的PDP上下文数。
  DSP GTPPDPNUM:;
  ```
  %%DSP GTPPDPNUM:;%%
  RETCODE = 0  操作成功。

  查询结果如下
  --------------
   RU名称              进程序号         PDP 上下文数           2G PDP 上下文数             3G PDP 上下文数             NB-IoT PDP 上下文数

   USN_SP_RU_0065      0                0                      0                           0                           0
   USN_SP_RU_0064      0                0                      0                           0                           0
   TOTAL               0                0                      0                           0                           0

  (结果个数 = 3)

  ---    END
  ```
2. 查询指定资源单元上的PDP上下文数：
  DSP GTPPDPNUM: RUNAME="USN_SP_RU_0065";
  ```
  %%DSP GTPPDPNUM: RUNAME="USN_SP_RU_0065";%%
  RETCODE = 0  操作成功。

  查询结果如下
  --------------
               RU名称  =  USN_SP_RU_0065
             进程序号  =  0
         PDP 上下文数  =  0
      2G PDP 上下文数  =  0
      3G PDP 上下文数  =  0
  NB-IoT PDP 上下文数  =  0
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示用户面PDP上下文数目(DSP-GTPPDPNUM)_72226029.md`
