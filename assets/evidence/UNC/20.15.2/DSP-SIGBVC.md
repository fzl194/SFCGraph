# 显示SigBvc上下文信息(DSP SIGBVC)

- [命令功能](#ZH-CN_MMLREF_0000001172225709__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225709__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225709__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225709__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225709__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225709__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225709__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225709)

**适用网元：SGSN**

该命令用于查询NSE实体对应的SIGBVC上下文基本信息；每一个NSE网络服务实体对应一个SIGBVC实体。

#### [注意事项](#ZH-CN_MMLREF_0000001172225709)

查询方式包括：

- 输入参数“MULTI_SIGBVC”，表示查询所有SIGBVC上下文状态信息。
- 输入参数“MULTI_SIGBVC”和“RUNAME”，表示查询指定RU上所有SIGBVC上下文状态信息。
- 输入参数“SINGLE_SIGBVC”，表示查询单个SIGBVC上下文基本信息。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225709)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225709)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225709)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OUTPUTTYPE | 输出类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定输出类型。<br>取值范围：<br>- “MULTI_SIGBVC（所有SIGBVC上下文信息）”<br>- “SINGLE_SIGBVC（单个SIGBVC上下文信息）”<br>默认值：<br>“MULTI_SIGBVC（所有SIGBVC上下文信息）” |
| RUNAME | RU名称 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件：该参数在当“输出类型”为指定“MULTI_SIGBVC（所有SIGBVC上下文信息）”时生效。<br>数据来源：整网规划。<br>取值范围：0~63 位字符串<br>默认值：无 |
| NSEI | NSE标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>前提条件：该参数在当“输出类型”为指定“SINGLE_SIGBVC（单个SIGBVC上下文信息）”时生效。<br>数据来源：整网规划。<br>取值范围：0~65535<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225709)

1. 查询USN_SP_RU_0066上所有SIGBVC上下文的状态信息：
  DSP SIGBVC: OUTPUTTYPE=MULTI_SIGBVC, RUNAME="USN_SP_RU_0066";
  ```
  %%DSP SIGBVC: OUTPUTTYPE=MULTI_SIGBVC, RUNAME="USN_SP_RU_0066";%% 
  RETCODE = 0  操作成功。  
  输出结果如下
  --------------
  RU名称            NSE标识   SIG实体状态
  USN_SP_RU_0066    14902     等待NS层状态正常 
  USN_SP_RU_0066    14904     等待NS层状态正常 
  USN_SP_RU_0066    14905     等待NS层状态正常 
  USN_SP_RU_0066    14906     等待NS层状态正常 
  USN_SP_RU_0066    14901     等待NS层状态正常 
  USN_SP_RU_0066    14908     等待NS层状态正常 
  USN_SP_RU_0066    14907     等待NS层状态正常 
  (结果个数 = 7)
  ---    END
  ```
2. 查询单个SIGBVC上下文状态信息，NSEI为14902：
  DSP SIGBVC: OUTPUTTYPE=SINGLE_SIGBVC, NSEI=14902;
  ```
  %%DSP SIGBVC: OUTPUTTYPE=SINGLE_SIGBVC, NSEI=14902;%%
  RETCODE = 0  操作成功。     
  输出结果如下
  --------------
    上下文是否已被分配  =  已分配
          NS层是否失败  =  故障
          NS层是否阻塞  =  未阻塞
           SIG实体状态  =  等待NS层状态正常
               NSE标识  =  14902
  SIG实体RESET重发次数  =  0
  SIG实体RESET定时器ID  =  255
  (结果个数 = 1)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225709)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NSE标识 | 网络服务实体标识。<br>说明：和PCU侧取值保持一致，此标识符在SGSN范围内唯一，不能重复。 |
| RU名称 | 该参数用于指定SPU资源单元名。 |
| 上下文是否已被分配 | 上下文是否已被分配。<br>取值说明：<br>- “未分配”<br>- “已分配” |
| NS是否故障 | NS层业务故障。<br>取值说明：<br>- “正常”<br>- “故障”<br>说明：NS故障时，请查看对应NSE下的链路状态，参考ALM 80638告警帮助进行处理。 |
| NS是否阻塞 | NS层是否阻塞。<br>取值说明：<br>- “未阻塞”<br>- “阻塞”<br>说明：阻塞状态的可能原因有：<br>- 产品侧NS故障，请参考ALM 80638告警帮助进行处理；<br>- PCU要求将小区闭塞，则与PCU联系。 |
| SIG实体状态 | SIG实体状态，可能状态为正常或等待NS层恢复，一般为正常。<br>取值说明：<br>- “正常”<br>- “等待复位响应”<br>- “等待NS层状态正常” |
| SIG实体RESET重发次数 | SIG实体RESET消息的重发次数。 |
| SIG实体RESET定时器ID | SIG实体RESET流程的定时器标识。 |
