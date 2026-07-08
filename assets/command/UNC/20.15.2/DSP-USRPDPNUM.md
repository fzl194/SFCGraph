---
id: UNC@20.15.2@MMLCommand@DSP USRPDPNUM
type: MMLCommand
name: DSP USRPDPNUM（显示用户和承载上下文数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: USRPDPNUM
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
- 系统管理
- 用户数据库管理
status: active
---

# DSP USRPDPNUM（显示用户和承载上下文数）

## 功能

**适用网元：SGSN、MME**

该命令用于查看系统内附着的用户数和激活的用户承载数等信息。

## 注意事项

该命令执行后立即生效，如果输入进程号，必须同时输入RU名称。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询方式。<br>取值范围：<br>“PROCESS_NO(进程标识)”<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>SPU<br>资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| PN | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要查看用户信息对应SPP进程的进程号。<br>取值范围：0~20<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRPDPNUM]] · 用户和承载上下文数（USRPDPNUM）

## 使用实例

1. 不输入RU名称和进程号时的显示结果:
  ```
  %%DSP USRPDPNUM:;%%
  RETCODE = 0  操作成功。

  用户数和上下文总计信息:
  -------------------------------
            静态用户数  =  0
       APN签约上下文数  =  0
          2G在线用户数  =  0
          3G在线用户数  =  0
          4G在线用户数  =  0
      NB-IoT在线用户数  =  0
          NR在线用户数  =  0
         2G激活PDP个数  =  0
         3G激活PDP个数  =  0
          4G EPS承载数  =  0
          NB-IoT承载数  =  0
      NB-IoT服务用户数  =  0
              NR承载数  =  0
  HSS Bypass状态用户数  =  0

  仍有后续报告输出
  ---    END

  %%DSP USRPDPNUM:;%%
  RETCODE = 0  操作成功。

  用户数和承载上下文信息：
  -----------------------
  RU名称            进程号    静态用户数    APN签约上下文数    2G在线用户数    3G在线用户数    4G在线用户数    NB-IoT在线用户数    NR在线用户数    2G激活PDP个数    3G激活PDP个数    4G EPS承载数    NB-IoT承载数    NB-IoT服务用户数     NR承载数     HSS Bypass状态用户数  

  USN_SP_RU_0064    0         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  USN_SP_RU_0064    4         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  USN_SP_RU_0065    4         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  USN_SP_RU_0065    1         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  USN_SP_RU_0065    2         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  USN_SP_RU_0065    3         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  USN_SP_RU_0064    2         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  USN_SP_RU_0064    3         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  USN_SP_RU_0065    0         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  USN_SP_RU_0064    1         0             0                  0               0               0               0                   0                0               0                0               0                0                   0                   0
  (结果个数 = 11) 
  共有2个报告
  ---    END
  ```
2. RU名称和进程号都输入时的显示结果:
  ```
  %%DSP USRPDPNUM: DT=PROCESS_NO, RUNAME="USN_SP_RU_0064", PN=1;%%
  RETCODE = 0  操作成功。

  用户数和承载上下文总计信息:
  ---------------------------
            静态用户数  =  0
       APN签约上下文数  =  0
          2G在线用户数  =  0
          3G在线用户数  =  0
          4G在线用户数  =  0
      NB-IoT在线用户数  =  0
          NR在线用户数  =  0
         2G激活PDP个数  =  0
         3G激活PDP个数  =  0
          4G EPS承载数  =  0
          NB-IoT承载数  =  0
     NB-IoT 服务用户数  =  0
              NR承载数  =  0
  HSS Bypass状态用户数  =  0
  仍有后续报告输出
  ---    END

  %%DSP USRPDPNUM: DT=PROCESS_NO, RUNAME="USN_SP_RU_0064 ", PN=1;%%
  RETCODE = 0  操作成功。

  用户数和承载上下文信息:
  -------------------------
                RU名称  =  USN_SP_RU_0064
                进程号  =  1
            静态用户数  =  0
       APN签约上下文数  =  0
          2G在线用户数  =  0
          3G在线用户数  =  0
          4G在线用户数  =  0
      NB-IoT在线用户数  =  0
          NR在线用户数  =  0
         2G激活PDP个数  =  0
         3G激活PDP个数  =  0
          4G EPS承载数  =  0
          NB-IoT承载数  =  0
      NB-IoT服务用户数  =  0
              NR承载数  =  0
  HSS Bypass状态用户数  =  0
  (结果个数 = 2)
  共有2个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示用户和承载上下文数(DSP-USRPDPNUM)_72345955.md`
