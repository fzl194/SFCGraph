# 激活支持多HPLMN功能（适用于 SGSN/ MME）

- [操作场景](#ZH-CN_OPI_0170150791__1.3.1)
- [必备事项](#ZH-CN_OPI_0170150791__1.3.2)
- [操作流程](#ZH-CN_OPI_0170150791__1.3.3)
- [操作步骤](#ZH-CN_OPI_0170150791__1.3.4)
- [任务示例](#ZH-CN_OPI_0170150791__1.3.5)

## [操作场景](#ZH-CN_OPI_0170150791)

当单一PLMN内的用户号段数量无法满足签约用户数量时，运营商可以选择开启本特性来运营多个PLMN，从而为更多签约用户提供服务。且如果运营商要对不同的PLMN内的签约用户采取不同的计费和策略控制等处理，则运营商可通过本特性在 UNC 上配置多个HPLMN，保证对签约用户进行精准的计费和业务控制。

> **说明**
> 适用于 SGSN、 MME。

## [必备事项](#ZH-CN_OPI_0170150791)

前提条件

- 请仔细阅读[WSFD-104401 支持多HPLMN功能特性概述](特性概述_69313567.md)。
- 已完成加载License。

数据

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 移动国家码（MCC） | 123 | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 移动网号（MNC） | 11 | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 国家码（CC） | 86 | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | MNO标识（MNOID） | 128 | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 是否允许SM业务（SM） | YES | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 最大承载数（MAXSMNUM） | 11 | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 是否允许SMS业务（SMS） | YES | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 是否允许纠正短消息中心（SMSCR） | YES | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 纠正后的短消息中心（SMSCT） | 861395678956778 | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 是否允许LCS业务（LCS） | YES | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 协议类型（S5S8TYPE） | GTP | 全网规划 | HPLMN参数 |
| [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 运营商名称（PLMNN） | noname | 全网规划 | HPLMN参数 |
| [**ADD MMESHAREPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/MME POOL区管理/MME共享管理/增加MME的共享PLMN(ADD MMESHAREPLMN)_26146086.md) | 移动国家码（MCC） | 123 | 全网规划 | MME的共享PLMN |
| [**ADD MMESHAREPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/MME POOL区管理/MME共享管理/增加MME的共享PLMN(ADD MMESHAREPLMN)_26146086.md) | 移动网号（MNC） | 10 | 全网规划 | MME的共享PLMN |
| [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md) | 发送网络信息（MMINFO） | S1_MODE-1 | 全网规划 | 运营商网络标识相关参数 |
| [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md) | EMM Information消息的信元携带策略（EMMINFOIEPLY） | NETWORK_NAME-1 | 全网规划 | 运营商网络标识相关参数 |
| [**ADD MNO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md) | MNO标识（MNOID） | 128 | 全网规划 | 运营商网络标识相关参数 |
| [**ADD MNO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md) | 运营商全称（FULLNAME） | A | 全网规划 | 运营商网络标识相关参数 |
| [**ADD MNO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md) | 运营商简称（SHORTNAME） | a | 全网规划 | 运营商网络标识相关参数 |
| [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) | 用户范围（SUBRANGE） | IMSI_RANGE | 全网规划 | 运营商网络标识相关参数 |
| [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) | 起始IMSI（BEGIMSI） | 123002000000000 | 全网规划 | 运营商网络标识相关参数 |
| [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) | 终止IMSI（ENDIMSI） | 123004000000000 | 全网规划 | 运营商网络标识相关参数 |
| [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) | PLMN匹配策略（PLMNPLCY） | YES | 全网规划 | 运营商网络标识相关参数 |
| [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) | 移动国家码（MCC） | 401 | 全网规划 | 运营商网络标识相关参数 |
| [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) | 移动网号（MNC） | 01 | 全网规划 | 运营商网络标识相关参数 |
| [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) | 运营商全称（FULLNAME） | aaa | 全网规划 | 运营商网络标识相关参数 |
| [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) | 运营商简称（SHORTNAME） | a | 全网规划 | 运营商网络标识相关参数 |
| [**ADD CONNECTPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 移动国家码（MCC） | 123 | 全网规划 | 互联PLMN参数 |
| [**ADD CONNECTPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 移动网号（MNC） | 003 | 全网规划 | 互联PLMN参数 |
| [**ADD CONNECTPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 运营商标识（NOID） | 128 | 全网规划 | 互联PLMN参数 |
| [**ADD HNOINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络信息管理/增加归属网络信息(ADD HNOINFO)_26305862.md) | 运营商标识（NOID） | 128 | 全网规划 | 本端标识参数 |
| [**ADD HNOINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络信息管理/增加归属网络信息(ADD HNOINFO)_26305862.md) | 本地实体索引（LOINDEX） | 1 | 全网规划 | 本端标识参数 |
| [**ADD HNOINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络信息管理/增加归属网络信息(ADD HNOINFO)_26305862.md) | 本局SGSN号（SGSNN） | 8613912345 | 全网规划 | 本端标识参数 |
| [**ADD IMSICHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md) | 用户范围（SUBRANGE） | IMSI_RANGE | 全网规划 | 本端标识参数 |
| [**ADD IMSICHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md) | IMSI前缀（IMSIPRE） | 123 | 全网规划 | 本端标识参数 |
| [**ADD IMSICHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md) | 起始IMSI（BEGIMSI） | 123001 | 全网规划 | 本端标识参数 |
| [**ADD IMSICHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md) | 终止IMSI（ENDIMSI） | 123004 | 全网规划 | 本端标识参数 |
| [**ADD IMSICHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md) | 本地实体索引（LOCALIDX） | 1 | 全网规划 | 本端标识参数 |
| [**ADD IMSICHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md) | SGSN号码（SGSNNO） | 8613912345 | 全网规划 | 本端标识参数 |

## [操作流程](#ZH-CN_OPI_0170150791)

激活支持多HPLMN功能操作流程如 [图1](#ZH-CN_OPI_0170150791__fig114914833413) 所示。

**图1** 激活支持多HPLMN功能操作流程

<br>

![](激活支持多HPLMN功能（适用于SGSN_MME）_70150791.assets/zh-cn_image_0173404685_2.png)

## [操作步骤](#ZH-CN_OPI_0170150791)

- 一个 UNC 为一个拥有多PLMN ID的MNO服务。
  > **说明**
  > 系统缺省会增加一条MNO ID为0的MNO记录，当 UNC 只被一个MNO使用时，无须再增加MNO。
    1. 进入 “MML命令行-UNC” 窗口。
    2. 打开本特性的License开关。
      **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    3. 增加运营商网络标识。
          a. 打开运营商网络名称下发开关，当4G终端接入时，系统允许将运营商网络名称携带给终端。
            [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)

            > **说明**
            > 若系统中同时存在命令 [**ADD MNO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md) 和 [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) 的配置记录，系统会优先将命令 [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) 配置的运营商网络名称下发给终端。
          b. 当需要特性IMSI范围的用户增加特定网络名称时执行以下步骤。
            [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md)
    4. 增加HPLMN记录。
      [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)
    5. 配置共享MME的PLMN ID。
      [**ADD MMESHAREPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/MME POOL区管理/MME共享管理/增加MME的共享PLMN(ADD MMESHAREPLMN)_26146086.md)
    6. **可选：**当MNO签订了漫游协议时，增加互联PLMN配置信息。
      [**ADD CONNECTPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)
    7. **可选：**配置本端标识的选择规则。
      [**ADD IMSICHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md)
      > **说明**
      > 对于只有一个MNO的场景，本端标识依次分为两层配置粒度，即第一层指根据IMSI号段配置，第二层轮选系统中所有的缺省配置。
    8. **可选：**增加PLMN对应的RNC信息。当MNO拥有多个HPLMN，且这些PLMN都需要在RNC侧进行广播，需要为每个PLMN配置RNC和寻呼信息。
      [**ADD RNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md)
    9. **可选：**增加PLMN对应的寻呼信息。
      [**ADD IUPAGING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口寻呼数据/增加Iu接口寻呼数据(ADD IUPAGING)_26305844.md)
- 网络中存在多个MNO，一个 UNC 为多个MNO服务。
    1. 进入 “MML命令行-UNC” 窗口。
    2. 打开本特性的License开关。
      **[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
    3. 增加运营商网络标识。
          a. 打开运营商网络名称下发开关，当终端接入时，系统允许将运营商网络名称携带给终端。
            [**SET MMFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)
          b. 增加运营商网络名称。
                  - [**ADD MNO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)
                    增加MNO信息。

                    > **说明**
                    > - 系统缺省已增加一条MNO ID为0的MNO记录，当 UNC 被多个MNO共享时，需要此步增加多个MNO。
                    > - 若系统中同时存在命令 [**ADD MNO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md) 和 [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) 的配置记录，系统会优先将命令 [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md) 配置的运营商网络名称下发给终端。
                  - **可选：**
                    当需要特定IMSI范围的用户增加特定网络名称时执行以下步骤。
                    [**ADD USRMMINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/网络名称管理/增加网络名称(ADD USRMMINFO)_26146058.md)
    4. 增加HPLMN记录。
      [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)
    5. 配置共享MME的PLMN ID。
      [**ADD MMESHAREPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/MME POOL区管理/MME共享管理/增加MME的共享PLMN(ADD MMESHAREPLMN)_26146086.md)
      > **说明**
      > MME侧必须配置该命令，否则可能导致MME不能识别eNodeB发来的S1 Setup Request消息中携带的PLMN，从而返回S1 Setup Failure。
    6. **可选：**当MNO签订了漫游协议时，增加互联PLMN配置信息。
      [**ADD CONNECTPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)
    7. **可选：**配置本端标识的选择规则。
      > **说明**
      > 对于存在多个MNO的场景，本端标识依次分为三层配置粒度，即第一层指根据IMSI号段配置，第二层根据MNO/MVNO ID配置，第三层轮选系统中所有的缺省配置。
          - 本端标识是SGSN号码
                  - 根据IMSI号段选择本端标识。
                    [**ADD IMSICHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md)
                  - 根据MNO ID选择本端标识
                    [**ADD HNOINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络信息管理/增加归属网络信息(ADD HNOINFO)_26305862.md)
          - 本端标识是Diameter
            > **说明**
            > - 如果系统中配置了多个Diameter本端标识，需要执行如下步骤。
            > - 如果系统中仅配置了一个Diameter本端标识，不需要执行如下步骤。
            >
            > 系统配置的Diameter本端标识可以通过 [**LST DMLE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter本地实体/查询Diameter本端实体(LST DMLE)_26306094.md) 命令查询。
                  - 根据IMSI号段选择本端标识
                    [**ADD IMSICHAR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md)
                  - 根据MNO ID选择本端标识
                    [**ADD HNOINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/归属网络信息管理/增加归属网络信息(ADD HNOINFO)_26305862.md)
    8. **可选：**增加PLMN对应的RNC信息。当一个MNO拥有多个HPLMN，且这些PLMN都需要在RNC侧进行广播，需要为每个PLMN配置RNC和寻呼信息。
      [**ADD RNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md)
    9. **可选：**增加PLMN对应的寻呼信息。
      [**ADD IUPAGING**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口寻呼数据/增加Iu接口寻呼数据(ADD IUPAGING)_26305844.md)

## [任务示例](#ZH-CN_OPI_0170150791)

任务描述

一个 UNC 为一个拥有2个PLMN ID的MNO服务，两个HPLMN的信息分别如下：

- PLMN1：移动国家码为123，移动网号为002，国家码为86，允许该HPLMN用户使用SMS业务，允许纠正短消息中心，纠正后的短消息中心为861395678956778。
- PLMN2：移动国家码为123，移动网号为003，国家码为86，允许该HPLMN用户使用SMS业务，不允许该HPLMN用户使用纠正短消息中心业务。

脚本

//打开本特性License开关。

```
SET LICENSESWITCH: LICITEM="LKV2HPLMN02", SWITCH=ENABLE;
```

//打开运营商网络名称下发开关，当4G终端接入时，系统允许将运营商网络名称携带给终端。

```
SET MMFUNC: MMINFO=S1_MODE-1, EMMINFOIEPLY=NETWORK_NAME-1;
```

//添加两条HPLMN记录。

```
ADD HPLMN: MCC="123", MNC="002", CC="86", SM=YES, SMS=YES, SMSCR=YES, SMSCT="861395678956778", LCS=YES, S5S8TYPE=GTP, EMCBS=YES;
ADD HPLMN: MCC="123", MNC="002", CC="86", SM=YES, SMS=YES, SMSCR=NO, LCS=YES, S5S8TYPE=GTP, EMCBS=YES;
```

//增加MME的共享信息。

```
ADD MMESHAREPLMN: MCC="123", MNC="11";
ADD MMESHAREPLMN: MCC="123", MNC="12";
```
