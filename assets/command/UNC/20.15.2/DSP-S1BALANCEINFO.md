---
id: UNC@20.15.2@MMLCommand@DSP S1BALANCEINFO
type: MMLCommand
name: DSP S1BALANCEINFO（查询S1接口均衡操作信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: S1BALANCEINFO
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1接口均衡管理
status: active
---

# DSP S1BALANCEINFO（查询S1接口均衡操作信息）

## 功能

**适用网元：MME**

此命令用于查询系统中指定SGP进程上的eNodeB数目或系统中总的eNodeB数目。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYSCE | 查询场景 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB均衡信息查询场景。<br>数据来源：本端规划<br>取值范围：<br>- “DISTRIBUTED(分布查询)”：用于查询相应SGP进程上的eNodeB数目。如果用户只指定RU名称，则查询指定RU所有SGP进程的eNodeB数目；如果用户不指定任何查询条件，则查询系统中所有SGP进程的eNodeB数目。<br>- “TOTAL(总数查询)”：用于查询系统总的eNodeB数目。<br>默认值：<br>“TOTAL(总数查询)” |
| RUNAME | RU名称 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前置条件：该参数在<br>“查询场景”<br>为<br>“DISTRIBUTED(分布查询)”<br>时才生效。<br>数据来源：本端规划<br>取值范围：0~63 位字符串<br>默认值：无 |
| PRON | 进程号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定到eNodeB的S1链路所在的SGP进程的进程号。<br>前置条件：该参数在<br>“查询场景”<br>为<br>“DISTRIBUTED(分布查询)”<br>时才生效。<br>数据来源：本端规划<br>取值范围：0~20<br>默认值：无<br>说明：- 如果输入进程号，必须输入RU名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1BALANCEINFO]] · S1接口均衡操作信息（S1BALANCEINFO）

## 使用实例

1. 查询系统所有eNodeB数目命令如下：DSP S1BALANCEINFO: QUERYSCE=TOTAL;
  ```
  %%DSP S1BALANCEINFO: QUERYSCE=TOTAL;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
  总的eNodeB数目  =  0
  (结果个数 = 1)
  ---    END
  ```
2. 查询USN_VSU1 0号SGP进程的eNodeB数目命令如下：DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN_VSU1", PRON=0;
  ```
  %%DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN_VSU1", PRON=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------------------
            RU名称   =  USN_VSU1
             进程号  =  0
         eNodeB个数  =  0
  (结果个数 = 1)
  ---    END
  ```
3. 查询USN_VSU1上的所有SGP进程的eNodeB数目命令如下：DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN_VSU1";
  ```
  %%DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN_VSU1";%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------------------
  RU名称      进程号         eNodeB个数 
  USN_VSU1    0              0                 
  USN_VSU1    3              0                 
  USN_VSU1    2              0                 
  USN_VSU1    1              0                 
  仍有后续报告输出
  ---    END
  ```
  ```
  %%DSP S1BALANCEINFO: QUERYSCE=DISTRIBUTED, RUNAME="USN_VSU1";%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  总的eNodeB数目  =  0
  (结果个数 = 5)
  共有2个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-S1BALANCEINFO.md`
