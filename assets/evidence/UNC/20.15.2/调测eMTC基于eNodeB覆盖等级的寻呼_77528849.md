# 调测 eMTC基于eNodeB覆盖等级的寻呼

- [操作场景](#ZH-CN_OPI_0277528849__1.3.1)
- [必备事项](#ZH-CN_OPI_0277528849__1.3.2)
- [操作步骤](#ZH-CN_OPI_0277528849__1.3.3)

## [操作场景](#ZH-CN_OPI_0277528849)

本操作指导介绍在运行网络中调测 eMTC基于eNodeB覆盖等级的寻呼 的操作过程。

## [必备事项](#ZH-CN_OPI_0277528849)

前提条件

- 请仔细阅读[WSFD-216102 eMTC基于eNodeB覆盖等级的寻呼特性概述](特性概述_75993415.md)。
- 完成[激活eMTC基于eNodeB覆盖等级的寻呼](激活eMTC基于eNodeB覆盖等级的寻呼_77396885.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2CELP01 | 本端规划 | 确认license已经打开 |
| [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 确认license已经打开 |
| [**SET NBEMM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/NB-MM协议参数管理/设置NB-S1模式MM协议参数（SET NBEMM）_26305584.md) | N3413（times）（N3413） | 1 | 全网规划 | 设置重发寻呼的最大次数 |
| [**ADD S1PAGINGRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1寻呼规则管理/增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md) | 用户群类型（GRPTYPE） | ALL_USER | 全网规划 | 设置精准寻呼动作为邻接eNodeB。 |
| [**ADD S1PAGINGRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1寻呼规则管理/增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md) | 业务类型（SVRTYPE） | S11_DOWNLINK | 全网规划 | 设置精准寻呼动作为邻接eNodeB。 |
| [**ADD S1PAGINGRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1寻呼规则管理/增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md) | APN指示（APNIND） | ALL_APN | 全网规划 | 设置精准寻呼动作为邻接eNodeB。 |
| [**ADD S1PAGINGRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1寻呼规则管理/增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md) | 寻呼动作组合（ACTGRP） | NEIGH_ENODEB-1 | 全网规划 | 设置精准寻呼动作为邻接eNodeB。 |
| [**ADD S1PAGINGRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1寻呼规则管理/增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md) | 规则描述（DESC） | data | 全网规划 | 设置精准寻呼动作为邻接eNodeB。 |
| [**SET M2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M控制参数/设置M2M控制参数(SET M2MCTRL)_72345369.md) | eNodeB覆盖增强检查开关（CHK_ENB_CE_SW） | OFF | 全网规划 | 设置“eNodeB覆盖增强检查开关”为“OFF(关闭)” |
| [**SET M2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M控制参数/设置M2M控制参数(SET M2MCTRL)_72345369.md) | 查询方式（QUERYOPT） | BYIMSI | 本端规划 | 设置“eNodeB覆盖增强检查开关”为“OFF(关闭)” |
| [**DSP COMMMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) | IMSI | 123036901000001 | 测试终端自带 | 观察终端的MM上下文 |

工具

- 测试终端
- OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0277528849)

在相关网元均完成本特性的配置后，可以采用以下步骤检查特性工作是否正常：

1. 进入 “MML命令行-UNC” 窗口。
2. 在UNC上[创建用户跟踪任务](../../../../../网络运维/日常维护/UNC基础运维操作/创建消息跟踪/创建用户跟踪/用户跟踪_72467812.md)，假设终端的IMSI为“123036901000001”。
3. 设置重发寻呼的最大次数 “N3413” 为 “1” 。
  [**SET EMM**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM协议参数管理/S1模式MM协议参数/设置S1模式MM协议参数(SET EMM)_72225207.md) : N3413=1;
4. 设置精准寻呼动作为邻接eNodeB。
  [**ADD S1PAGINGRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1寻呼规则管理/增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md) : GRPTYPE=ALL_USER, SVRTYPE=S11_DOWNLINK, APNIND=ALL_APN, ACTGRP=NEIGH_ENODEB-1, DESC="data";
5. 设置“eNodeB覆盖增强检查开关”为“OFF(关闭)”。
  [**SET M2MCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/M2M管理/M2M控制参数/设置M2M控制参数(SET M2MCTRL)_72345369.md) : CHK_ENB_CE_SW=OFF;
6. 终端在覆盖等级为2的小区下开机通过eNodeB1附着到网络（eNodeB1支持在UE Context Release Complete消息中携带寻呼辅助信息）。
7. 终端移出eNodeB1到覆盖等级为3的eNodeB2下的小区。
8. 执行下述命令，观察终端的MM上下文。
  [**DSP COMMMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) : QUERYOPT=BYIMSI, IMSI="123036901000001";
  ```
  %%DSP COMMMCTX: QUERYOPT=BYIMSI, IMSI="123036901000001";%%
  RETCODE = 0  操作成功

  MM上下文信息：
  ----------------
             ............

                          推荐的小区数目  =  2
                          推荐的小区列表  =  2143650000000; 2143650000005
                        推荐的eNodeB数目  =  2
                        推荐的eNodeB列表  =  21436500000; 21436500001
                          上次驻留的ECGI  =  2143650000005
                      上次驻留的覆盖等级  =  101F
             ............

  ---    END
  ```
  预期结果：观察到 “推荐的小区数目” ， “推荐的小区列表” ， “推荐的eNodeB数目” ， “推荐的eNodeB列表” ， “上次驻留的ECGI” ， “上次驻留的覆盖等级” 与eNodeB1通过UE Context Release Complete消息上报的值相同。
  > **说明**
  > 小区的覆盖等级（如上文eNodeB1下的小区覆盖等级2）与eNodeB上报MME的CE level（MME上查询到的101F）之间的关系由eNodeB决定。
9. 网关发起下行数据触发 UNC 寻呼用户。
  预期结果： UNC 下发的寻呼消息中携带了寻呼辅助信息，Paging Attempt Count为1。
  **图1** 首次发送的Paging消息

  <br>![](调测eMTC基于eNodeB覆盖等级的寻呼_77528849.assets/zh-cn_image_0000002414699240_2.png)<br>
10. 观察 UNC 重新下发的寻呼消息。
  预期结果：寻呼消息中寻呼辅助信息的Paging Attempt Count为2。
  **图2** 重发的Paging消息

  <br>![](调测eMTC基于eNodeB覆盖等级的寻呼_77528849.assets/zh-cn_image_0000002448018413_2.png)<br>
