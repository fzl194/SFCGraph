# 激活网络共享（GWCN）场景二：SGSN共享给MVNO

- [操作场景](#ZH-CN_OPI_0185152764__1.3.1)
- [必备事项](#ZH-CN_OPI_0185152764__1.3.2)
- [操作步骤](#ZH-CN_OPI_0185152764__1.3.3)
- [任务示例](#ZH-CN_OPI_0185152764__1.3.4)

## [操作场景](#ZH-CN_OPI_0185152764)

本操作指导介绍在运行网络中激活网络共享（GWCN）特性的操作过程。

网络共享（GWCN）（Gateway Core Network），指GW核心网方式的网络共享。本特性在 UNC 支持了多HPLMN功能或MVNO功能的前提下，完成无线网络的共享，即不仅共享 无线接入网 ，而且共享核心网的SGSN设备。

本操作的应用场景组网图如 [图1](#ZH-CN_OPI_0185152764__zh-cn_opi_0130429087_fig1) 所示，MNO将Shared SGSN 共享给 MVNO ，MVNO拥有自己的 GGSN 、 CG 等网络设备。

**图1** GWCN场景二组网示例

<br>

![](激活网络共享（GWCN）场景二：SGSN共享给MVNO_85152764.assets/zh-cn_image_0185156670_2.png)

<br>

## [必备事项](#ZH-CN_OPI_0185152764)

前提条件

- 操作人员已经登录U2020。
- RNC需要支持网络共享。
- 当UNC被多PLMN共享时，UNC需要和多个PLMN的核心网设备（例如GGSN、MSC、HLR、CG等）连接，故在部署本特性之前，需要完成和其他核心网网元的对接配置。
- 到RNC的基本数据已经配置完成，配置方法见[配置到RNC的数据](../../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置SGSN/配置到RNC的数据_82626756.md)。
  > **说明**
  > 当RNC支持多HPLMN功能时，已经在SGSN上完成每个PLMN对应的RNC信息的配置（ [**ADD RNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md) ）。例如RNC的LAC和RAC分别是0x2301和0x21，支持46100和46101两个PLMN，则SGSN需要完成的RNC信息配置为：
  >
  > ```
  > ADD RNC: RNCX=1, RNCN="RNC_SHARE", RNCMCC="461", RNCMNC="00", RNCID=0, NI=NATB, SPC="0xb01", RNCVER=R6;
  > ADD RNC: RNCX=2, RNCN="RNC_SHARE", RNCMCC="461", RNCMNC="01", RNCID=0, NI=NATB, SPC="0xb01", RNCVER=R6;
  > ```
- 本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82207708 LKV2GWCN02 网络共享(GWCN)” 。

数据

| 类别 | 参数名 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD IUPAGING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口寻呼数据/增加Iu接口寻呼数据(ADD IUPAGING)_26305844.md) | 位置区标识（LAI） | 123002301、660002301、123002302、660002302、123002303、660002303 | 全网规划 | 3G寻呼参数 |
| [**ADD IUPAGING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口寻呼数据/增加Iu接口寻呼数据(ADD IUPAGING)_26305844.md) | 位置区编码（RAC） | 0x21 | 全网规划 | 3G寻呼参数 |
| [**ADD IUPAGING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口寻呼数据/增加Iu接口寻呼数据(ADD IUPAGING)_26305844.md) | RNC索引（RNCINDEX） | 1、3、5 | 全网规划 | 3G寻呼参数 |
| [**ADD HNOSRVPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络Serving PLMN管理/增加归属网络Serving PLMN信息(ADD HNOSRVPLMN)_72345655.md) | 运营商标识（NOID） | 0 | 全网规划 | 归属网络Serving PLMN信息 |
| [**ADD HNOSRVPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络Serving PLMN管理/增加归属网络Serving PLMN信息(ADD HNOSRVPLMN)_72345655.md) | 移动国家码（MCC） | 461 | 全网规划 | 归属网络Serving PLMN信息 |
| [**ADD HNOSRVPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络Serving PLMN管理/增加归属网络Serving PLMN信息(ADD HNOSRVPLMN)_72345655.md) | 移动网号（MNC） | 00 | 全网规划 | 归属网络Serving PLMN信息 |

## [操作步骤](#ZH-CN_OPI_0185152764)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开GWCN功能开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 配置 UNC 支持MVNO，请参见 [激活MVNO](../../WSFD-207005 MVNO/激活MVNO_85152767.md) 。
4. **可选：**增加Gs接口配置，为每个PLMN（LAI）配置对应的VLR。
  [**ADD LAIVLR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md)
  > **说明**
  > 当RNC支持多HPLMN时，SGSN上需要配置每个PLMN对应LAI与VLR的关系。例如RNC的LAC和RAC分别是0x2301和0x21，支持46100和46101两个PLMN，VLR号码为86139015201，则SGSN需要增加的LAI与VLR的对应关系如下:
  >
  > - LAI：461002301，VLR号码：86139015201
  > - LAI：461012301，VLR号码：86139015201
5. **可选：**增加3G寻呼数据，针对每个PLMN配置对应的3G寻呼数据。
  [**ADD IUPAGING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口寻呼数据/增加Iu接口寻呼数据(ADD IUPAGING)_26305844.md)
  > **说明**
  > 当RNC支持多HPLMN时，SGSN上需要配置每个PLMN对应的3G寻呼数据。例如RNC的LAC和RAC分别是0x2301和0x21，支持46100和46101两个PLMN，则SGSN需要增加的3G寻呼数据如下：
  >
  > - LAI：461002301，RAC：21
  > - LAI：461012301，RAC：21
6. **可选：**增加COMMON PLMN对应的寻呼信息。
  [**ADD IUPAGING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口寻呼数据/增加Iu接口寻呼数据(ADD IUPAGING)_26305844.md)
  > **说明**
  > 对于Non-supporting UE，SGSN只能看到COMMON PLMN。如果UE接入的无线网络的PLMN和无线侧指定的COMMON PLMN不是同一个，则需要执行本步骤，保证SGSN可以成功寻呼到该用户。
7. **可选：**为Non-supporting UE指定Serving PLMN。
  [**ADD HNOSRVPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络Serving PLMN管理/增加归属网络Serving PLMN信息(ADD HNOSRVPLMN)_72345655.md)
  > **说明**
  > 当MVNO拥有多个PLMN时，需要执行本步骤。

## [任务示例](#ZH-CN_OPI_0185152764)

任务描述

Operator B为通过租用Operator A的SGSN和无线设备提供业务。Operator A的HPLMN为12300，Operator B的HPLMN为66000，运营商标识为1，国家代码为“86139”。

脚本

1. 开启MVNO功能。
  //打开MVNO的License开关。
  ```
  SET LICENSESWITCH: LICITEM="LKV2MVNO02", SWITCH=ENABLE;
  ```
  //增加MVNO标识。
  ```
  ADD MVNO: MVNOID=1, MVNON="Operator B";
  ```
  //增加MVNO网络配置信息。
  ```
  ADD MVNONET: MVNOMCC="660", MVNOMNC="00", MVNOCC="86139", MVNOID=1; 
  ```
  //增加MVNO用户资源，最大的2G用户数为50000，最大的2G的PDP激活个数为50000，最大的3G用户数为50000，最大的3G的PDP激活个数为50000，其他的值使用缺省值。
  ```
  ADD MVNORES: MVNOID=1, GMSNUM=50000, UMSNUM=50000, GPDPNUM=50000, UPDPNUM=50000;
  ```
  //增加MVNO功能配置信息。
  ```
  ADD MVNOFUN: MVNOID=1, SMS=YES, LCS=NO;
  ```
2. 开启GWCN功能。
  //开启GWCN功能开关。
  ```
  SET LICENSESWITCH: LICITEM="LKV2GWCN02", SWITCH=ENABLE;
  ```
  //增加A、B和C三个RNC，MNC+MCC分别为12300和66000，RNC的标识分别为0、1、2，网络指示语为国内备网，信令点编码分别是0xb01、0xb02及0xb03，RNC协议版本为R6，其余参数采用缺省值。
  ```
  ADD RNC: RNCX=1, RNCN="A", RNCMCC="123", RNCMNC="00", RNCID=0, NI=NATB, SPC="0xb01", RNCVER=R6;
  ```
  ```
  ADD RNC: RNCX=2, RNCN="A", RNCMCC="660", RNCMNC="00", RNCID=0, NI=NATB, SPC="0xb01", RNCVER=R6;
  ```
  ```
  ADD RNC: RNCX=3, RNCN="B", RNCMCC="123", RNCMNC="00", RNCID=1, NI=NATB, SPC="0xb02", RNCVER=R6;
  ```
  ```
  ADD RNC: RNCX=4, RNCN="B", RNCMCC="660", RNCMNC="00", RNCID=1, NI=NATB, SPC="0xb02", RNCVER=R6;
  ```
  ```
  ADD RNC: RNCX=5, RNCN="C", RNCMCC="123", RNCMNC="00", RNCID=2, NI=NATB, SPC="0xb03", RNCVER=R6;
  ```
  ```
  ADD RNC: RNCX=6, RNCN="C", RNCMCC="660", RNCMNC="00", RNCID=2, NI=NATB, SPC="0xb03", RNCVER=R6;
  ```
  //增加Gs接口配置，为每个PLMN（LAI）配置对应的VLR。
  ```
  ADD LAIVLR: BGNLAI="123002301", ENDLAI="123002301", VLRNO="86139015201";
  ```
  ```
  ADD LAIVLR: BGNLAI="660002301", ENDLAI="660002301", VLRNO="86139015201";
  ```
  ```
  ADD LAIVLR: BGNLAI="123002302", ENDLAI="123002302", VLRNO="86139015201";
  ```
  ```
  ADD LAIVLR: BGNLAI="660002302", ENDLAI="660002302", VLRNO="86139015201";
  ```
  ```
  ADD LAIVLR: BGNLAI="123002303", ENDLAI="123002303", VLRNO="86139015201";
  ```
  ```
  ADD LAIVLR: BGNLAI="660002303", ENDLAI="660002303", VLRNO="86139015201";
  ```
  //增加LAI分别为123002301、660002301、123002302、660002302、123002303、660002303，RAC为0x21，RNC INDEX分别为1、3和5的3G寻呼信息。
  ```
  ADD IUPAGING: LAI="123002301", RAC="0x21", RNCINDEX=1;
  ```
  ```
  ADD IUPAGING: LAI="660002301", RAC="0x21", RNCINDEX=1;
  ```
  ```
  ADD IUPAGING: LAI="123002302", RAC="0x21", RNCINDEX=3;
  ```
  ```
  ADD IUPAGING: LAI="660002302", RAC="0x21", RNCINDEX=3;
  ```
  ```
  ADD IUPAGING: LAI="123002303", RAC="0x21", RNCINDEX=5;
  ```
  ```
  ADD IUPAGING: LAI="660002303", RAC="0x21", RNCINDEX=5;
  ```
  > **说明**
  > [**ADD IUPAGING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口寻呼数据/增加Iu接口寻呼数据(ADD IUPAGING)_26305844.md) 脚本中的 “RNCINDEX” 用于查找RNC ID。 [**ADD RNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md) 脚本中，RNC索引1、2对应RNC ID 0，RNC索引3、4对应RNC ID 1，RNC索引5、6对应RNC ID 2。为简化配置， [**ADD IUPAGING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口寻呼数据/增加Iu接口寻呼数据(ADD IUPAGING)_26305844.md) 脚本中分别使用RNC索引1、3、5完成配置，和使用实际的RNC索引效果一致。
