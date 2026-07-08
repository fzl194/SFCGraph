---
id: UNC@20.15.2@MMLCommand@DSP OFFLOAD
type: MMLCommand
name: DSP OFFLOAD（显示迁移进度）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OFFLOAD
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
- 网络管理
- 迁移控制
status: active
---

# DSP OFFLOAD（显示迁移进度）

## 功能

**适用网元：SGSN、MME**

此命令用于查询Pool内用户迁移进度信息。

## 注意事项

- 如果当前系统正在执行迁移任务，则显示当前迁移进度信息，否则将显示最近一次的迁移记录信息。
- 此命令对类型为“IMSI(IMSI)”的迁移任务不生效。针对类型为“IMSI(IMSI)”的迁移任务，可通过用户跟踪等手段查看迁移进度。
- 使用迁移命令[**STR OFFLOADBYMME**](启动MME迁移任务（STR OFFLOADBYMME）_72345693.md)启动的MME迁移任务， 当“等待高延迟UE迁移完成”参数配置为“WAIT_EDRX”时，如果系统中存在eDRX用户，可能由于迁移过程中启动eDRX延迟寻呼定时器，导致迁移时长增加。若只迁移WB-SAE用户，最多延长60分钟； 若同时迁移NB-IOT用户，最多延长200分钟。
- 使用迁移命令[**STR NBOFFLOADBYMME**](启动NB-IoT用户的MME迁移任务（STR NBOFFLOADBYMME）_26146094.md)启动NB-IoT用户的MME迁移任务， 当“等待高延迟UE迁移完成”参数配置为“WAIT_EDRX”时，如果系统中存在eDRX用户，可能由于迁移过程中启动eDRX延迟寻呼定时器，导致迁移时长增加，最多延长200分钟。
- 使用迁移命令**[STR OFFLOADBYTA](启动TA迁移任务（STR OFFLOADBYTA）_02884717.md)**启动基于TA的迁移任务，**[DSP OFFLOAD](显示迁移进度(DSP OFFLOAD)_72345691.md)**命令的“需要卸载用户数”参数依赖正确订阅“117494566 指定TAI组的S1模式实时附着用户数”和“117468805 指定TAI组的NB-S1模式实时附着用户数”，这两个指标未订阅时，**[DSP OFFLOAD](显示迁移进度(DSP OFFLOAD)_72345691.md)**命令的“需要卸载用户数”参数显示为0。这两个指标未按照**[STR OFFLOADBYTA](启动TA迁移任务（STR OFFLOADBYTA）_02884717.md)**下发的TA参数分别配置不同的TAI组（一个TA对应配置一个TAI组）时，**[DSP OFFLOAD](显示迁移进度(DSP OFFLOAD)_72345691.md)**命令的“需要卸载用户数”参数显示值不准确。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/OFFLOAD]] · 迁移任务（OFFLOAD）

## 使用实例

1. 由 [**STR OFFLOADBYSGSN**](启动SGSN迁移任务（STR OFFLOADBYSGSN）_26305904.md) 命令启动的SGSN迁移任务进度信息，查询结果如下：
  ```
  %%DSP OFFLOAD:;%%
  RETCODE = 0  执行成功。

  操作结果如下
  ------------
           迁移类型  =  全部flex用户
           迁移状态  =  卸载中
     需要卸载用户数  =  1
     已经卸载用户数  =  0
  剩余卸载时间(min)  =  1
  仍有后续报告输出
  ---   END

  操作结果如下
  ------------
     SGSNNRI  =  4
  迁入百分比  =  100
  迁入用户数  =  0
  (结果个数 = 2)
  共有2个报告
  ---   END
  ```
2. 由 [**STR OFFLOADBYRNC**](启动RNC迁移任务（STR OFFLOADBYRNC）_72225773.md) 命令启动的RNC迁移任务进度信息，查询结果如下：
  ```
  %%DSP OFFLOAD:;%%
  RETCODE = 0  执行成功。

  操作结果如下
  ------------
           迁移类型  =  指定RNC
           迁移状态  =  卸载中
     需要卸载用户数  =  1
     已经卸载用户数  =  0
  剩余卸载时间(min)  =  1
  仍有后续报告输出
  ---   END

  操作结果如下
  ------------
    RNC移动国家代码  =  640
        RNC移动网号  =  03
            RNC标识  =  1151
     已经卸载用户数  =  0		
  仍有后续报告输出
  ---   END

  操作结果如下
  ------------		
     SGSNNRI  =  4
  迁入百分比  =  100
  迁入用户数  =  0
  (结果个数 = 3)
  共有3个报告
  ---   END
  ```
3. 由 [**STR OFFLOADBYBSC**](启动BSC迁移任务（STR OFFLOADBYBSC）_72225771.md) 命令启动的BSC迁移任务进度信息，查询结果如下：
  ```
  %%DSP OFFLOAD:;%%
  RETCODE = 0  执行成功。

  操作结果如下
  ------------
           迁移类型  =  指定BSC
           迁移状态  =  卸载中
     需要卸载用户数  =  1
     已经卸载用户数  =  0
  剩余卸载时间(min)  =  1
  仍有后续报告输出
  ---   END

  操作结果如下
  ------------
         BSS 编号 =  11501
  已经卸载用户数  =  0
  仍有后续报告输出
  ---   END

  操作结果如下
  ------------
     SGSNNRI  =  4
  迁入百分比  =  100
  迁入用户数  =  0
  (结果个数 = 3)
  共有3个报告
  ---   END
  ```
4. 由 [**STR OFFLOADBYMME**](启动MME迁移任务（STR OFFLOADBYMME）_72345693.md) 命令启动的MME迁移任务进度信息，查询结果如下：
  ```
  %%DSP OFFLOAD:;%%
  RETCODE = 0  执行成功。

  操作结果如下
  ------------
           迁移类型  =  全部用户
           迁移状态  =  卸载中
     需要卸载用户数  =  1
     已经卸载用户数  =  0
  剩余卸载时间(min)  =  1
  启动延迟寻呼的eDRX用户数  =  0
  (结果个数 = 1)
  ---   END
  ```
5. 由 [**STR OFFLOADBYENODEB**](启动eNodeB迁移任务(STR OFFLOADBYENODEB)_26305902.md) 命令启动的eNodeB迁移任务进度信息，查询结果如下：
  ```
  %%DSP OFFLOAD:;%%
  RETCODE = 0  执行成功。

  操作结果如下
  ------------
           迁移类型  =  指定eNodeB
           迁移状态  =  卸载中
     需要卸载用户数  =  1
     已经卸载用户数  =  0
  剩余卸载时间(min)  =  1
  仍有后续报告输出
  ---   END

  操作结果如下
  -------------------------
  eNodeB移动国家码  =  123
    eNodeB移动网号  =  03
        eNodeB类型  =  MACRO_ENB
        eNodeB标识  =  204817
      待卸载用户数  =  1
    已经卸载用户数  =  0
  卸载任务启动状态  =  启动
  (结果个数 = 2)
  共有2个报告
  ---   END
  ```
6. 由 [**STR NBOFFLOADBYMME**](启动NB-IoT用户的MME迁移任务（STR NBOFFLOADBYMME）_26146094.md) 命令启动的NB-IoT用户的MME迁移任务进度信息，查询结果如下：
  ```
  %%DSP OFFLOAD:;%%
  RETCODE = 0  执行成功。

  操作结果如下
  ------------
           迁移类型  =  全部用户
           迁移状态  =  卸载中
     需要卸载用户数  =  1
     已经卸载用户数  =  0
  剩余卸载时间(min)  =  1
  启动延迟寻呼的eDRX用户数  =  0
  (结果个数 = 1)
  ---   END
  ```
7. 由**[STR OFFLOADBYTA](启动TA迁移任务（STR OFFLOADBYTA）_02884717.md)**命令启动的TA迁移任务进度信息，查询结果如下：
  ```
  %%DSP OFFLOAD:;%%
  RETCODE = 0  操作成功
  操作结果如下
  ------------
                  迁移类型  =  指定TA
                  迁移状态  =  卸载中
            需要卸载用户数  =  0
            已经卸载用户数  =  0
       剩余卸载时间（min）  =  1
  启动延迟寻呼的eDRX用户数  =  0
  (结果个数 = 1)
  操作结果如下
  ------------
  TA移动国家码  TA移动网号  跟踪区域码  已经卸载用户数  
  123           03          0x3401      0               
  123           03          0x3403      0               
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OFFLOAD.md`
