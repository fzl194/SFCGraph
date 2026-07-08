# 激活MSC Pool场景下的CSFB

- [操作场景](#ZH-CN_OPI_0164009924__1.3.1)
- [必备事项](#ZH-CN_OPI_0164009924__1.3.2)
- [操作流程](#ZH-CN_OPI_0164009924__1.3.3)
- [操作步骤](#ZH-CN_OPI_0164009924__1.3.4)
- [任务示例](#ZH-CN_OPI_0164009924__1.3.5)

## [操作场景](#ZH-CN_OPI_0164009924)

本操作指导介绍在运行网络中激活MSC Pool场景下的CSFB业务特性的操作过程。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0164009924)

前提条件

- “基于CSFB的语音业务” 、 “通过SGs接口实现短消息” 特性已经激活。
- 用户在HSS中已签约EPS和CS业务。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/增加VLR配置信息(ADD VLR)_26305254.md) | VLR号（VN） | 86139027/86139028 | 全网规划 | 配置VLR1/VLR2相关数据。 |
| [**ADD VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/增加VLR配置信息(ADD VLR)_26305254.md) | VLR名称（VNM） | vlr12/vlr13 | 全网规划 | 配置VLR1/VLR2相关数据。 |
| [**ADD VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/增加VLR配置信息(ADD VLR)_26305254.md) | MSC POOL名称（POOLNM） | POOL11 | 全网规划 | 配置VLR1/VLR2相关数据。 |
| [**ADD VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/增加VLR配置信息(ADD VLR)_26305254.md) | 最小V值（MINV） | 0/301 | 全网规划 | 配置VLR1/VLR2相关数据。 |
| [**ADD VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/增加VLR配置信息(ADD VLR)_26305254.md) | 最大V值（MAXV） | 300/999 | 全网规划 | 配置VLR1/VLR2相关数据。 |
| [**ADD SGSLKS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路集管理/增加SGs链路集(ADD SGSLKS)_72345035.md) | 链路集索引（LSX） | 0/1 | 本端规划 | 配置SGs链路集1/2参数。 |
| [**ADD SGSLKS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路集管理/增加SGs链路集(ADD SGSLKS)_72345035.md) | VLR号（VN） | 86139027/86139028 | 与对端协商 | 配置SGs链路集1/2参数。 |
| [**ADD SGSLKS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路集管理/增加SGs链路集(ADD SGSLKS)_72345035.md) | 链路集名（LSN） | sgs1/sgs2 | 本端规划 | 配置SGs链路集1/2参数。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | 链路索引（LNK） | 1/2/3/4 | 本端规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | SGs链路名称（SGSLNKNM） | NONAME | 本端规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | IP地址类型（IPTYPE） | IPV4 | 全网规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | VLR IPv4地址1（VLRIPV4_1） | 10.49.49.205/10.50.50.205/10.51.51.205/10.52.52.205 | 全网规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | VLR IPv4地址2（VLRIPV4_2） | 10.49.49.204/10.50.50.204/10.51.51.204/10.52.52.204 | 全网规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | VLR端口（VLRPORT） | 29118/29119 | 与对端协商 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | 本地IPv4地址1（LOCALIPV4_1）<br>10. | 10.49.49.206/10.50.50.206/10.51.51.206/10.52.52.206 | 全网规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | 本地IPv4地址2（LOCALIPV4_2） | 10.49.49.207/10.50.50.207/10.51.51.207/10.52.52.207 | 全网规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | 本地端口（LOCALPORT） | 29118/29119 | 与对端协商 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | 链路集索引（LSX） | 0 | 本端规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | SCTP协议参数索引（SCTPINDX） | 0 | 本端规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | 交叉路径是否可用（CROSSIPFLAG） | NO | 全网规划 | 配置SGs链路1/2/3/4。 |
| [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) | VPN名称（VPNNAME） | _public_ | 全网规划 | 配置SGs链路1/2/3/4。 |
| [**ADD LAIVLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md) | LAI（BGNLAI） | 308015101 | 全网规划 | 配置LAIVLR相关数据。 |
| [**ADD LAIVLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md) | ENDLAI（终止LAI） | 308015101 | 全网规划 | 配置LAIVLR相关数据。 |
| [**ADD LAIVLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md) | VLRNO（VLR号） | 86139027 | 全网规划 | 配置LAIVLR相关数据。 |
| [**ADD LAIVLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md) | DFLVLR（是否缺省VLR） | YES | 全网规划 | 配置LAIVLR相关数据。 |
| **[ADD TAILAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)** | 起始TAI（BGNTAI） | 308015101 | 全网规划 | 配置TAILAI相关数据。 |
| **[ADD TAILAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)** | 终止TAI（ENDTAI） | 308015101 | 全网规划 | 配置TAILAI相关数据。 |
| **[ADD TAILAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)** | LAI（LAI）<br>_ | 308015101 | 全网规划 | 配置TAILAI相关数据。 |
| [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md) | 位置更新定时器（TS6_1） | 10 | 全网规划 | 配置SGs接口业务运行参数。 |
| [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md) | EPS分离定时器（TS8） | 4 | 全网规划 | 配置SGs接口业务运行参数。 |
| [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md) | 显式IMSI分离定时器（TS9） | 4 | 全网规划 | 配置SGs接口业务运行参数。 |
| [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md) | 隐式IMSI分离定时器（TS10） | 4 | 全网规划 | 配置SGs接口业务运行参数。 |
| [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md) | EPS分离重发次数（NS8） | 2 | 全网规划 | 配置SGs接口业务运行参数。 |
| [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md) | 显式IMSI分离重发次数（NS9） | 2 | 全网规划 | 配置SGs接口业务运行参数。 |
| [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md) | 隐式IMSI分离重发次数（NS10） | 2 | 全网规划 | 配置SGs接口业务运行参数。 |
| [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md) | SGs链路中断触发告警阈值（ALARMLIMIT） | 24 | 全网规划 | 配置SGs接口业务运行参数。 |
| [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md) | 自动迁移开关（AUTOOFFLOAD） | YES | 全网规划 | 配置SGs接口业务运行参数。 |

## [操作流程](#ZH-CN_OPI_0164009924)

激活MSC Pool场景下的CSFB业务操作流程如 [图1](#ZH-CN_OPI_0164009924__fig_01) 所示。

**图1** 激活MSC Pool场景下的CSFB业务操作流程

<br>

![](激活MSC Pool场景下的CSFB_64009924.assets/zh-cn_image_0199533595_2.png)

## [操作步骤](#ZH-CN_OPI_0164009924)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 建立MME和MSC之间的设备间通信。
    a. 添加MME和MSC之间偶联路径的SCTP参数模板。
      [**ADD SCTPPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/SCTP管理/增加SCTP协议参数(ADD SCTPPARA)_26306150.md)
    b. 增加MME到指定MSC的SCTP偶联信息。
      [**ADD VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/增加VLR配置信息(ADD VLR)_26305254.md)
      [**ADD SGSLKS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路集管理/增加SGs链路集(ADD SGSLKS)_72345035.md)
      [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md)
    c. 查询MME和MSC之间SCTP偶联状态是否正常。
      [**DSP SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/显示SGs链路状态(DSP SGSLNK)_72345033.md)
    d. 增加MME到另一个指定MSC的SCTP偶联信息。
      [**ADD VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/增加VLR配置信息(ADD VLR)_26305254.md)
      [**ADD SGSLKS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路集管理/增加SGs链路集(ADD SGSLKS)_72345035.md)
      [**ADD SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md)
    e. 查询MME和另一个MSC之间SCTP偶联状态是否正常。
      [**DSP SGSLNK**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP链路管理/显示SGs链路状态(DSP SGSLNK)_72345033.md)
4. 激活MSC Pool场景下的CSFB业务。
    a. 添加MSC覆盖的LA。
      > **说明**
      > MSC POOL的作用是负荷分担和容灾的，因此MSC POOL内的各个MSC管辖的LAI范围是一样的，此步骤只需要配置MSC Pool中任意一个MSC/VLR与LAI的对应关系即可。 UNC 首先根据LAI选择对应的MSC Pool，然后再根据用户IMSI V值与MSC/VLR的对应关系在Pool内选择一个链路状态正常的MSC/VLR为UE提供服务（IMSI V值与MSC/VLR的对应关系通过 [**ADD VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/增加VLR配置信息(ADD VLR)_26305254.md) 命令进行配置）。
      [**ADD LAIVLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md)
    b. 添加LA覆盖的TA范围。
      **[ADD TAILAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)**
    c. **可选：**配置缺省LAI记录。
      > **说明**
      > 若在网络中无法确定所有的TAI都能和LAI一一映射，避免因TAI配置遗漏而导致业务失败，则可以配置一条系统缺省LAI记录，即将参数 “BGNTAI” 设置成 “FFFFFFFFFF” 。
      >
      > 配置缺省LAI记录的影响：
      >
      > - 缺省LAI与UE目前附着的TA可能不共覆盖，会使UE回落时执行roaming retry procedure，导致呼叫延时增加。
      > - 在CSFB的流程中要尽量保证分配的TA LST不跨LAI区域。只有在短消息的情况下，由于没有回落的情况下才可以使用default的LAI。
      **[ADD TAILAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)**
5. 设置SGs接口业务运行参数。
  [**SET SGSPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/SGSAP/SGsAP参数管理/设置SGs参数(SET SGSPARA)_26145440.md)

## [任务示例](#ZH-CN_OPI_0164009924)

任务描述

启用MSC Pool场景下CSFB业务。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2CSFBMP02", SWITCH=ENABLE;
```

//MME上的配置。

//添加MME和MSC之间偶联路径的SCTP参数模板。

```
ADD SCTPPARA: SCTPPARAINDEX=0;
```

//增加MME到指定MSC的SCTP偶联信息。

```
ADD VLR: VN="86139027", VNM="vlr12", POOLNM="POOL11", MINV=0, MAXV=300;
ADD SGSLKS: LSX=0, VN="86139027", LSN="sgs1";
ADD SGSLNK: LNK=1, IPTYPE=IPV4, VLRIPV4_1="10.49.49.205", VLRIPV4_2="10.49.49.204", VLRPORT=29118, LOCALIPV4_1="10.49.49.206" ,LOCALIPV4_2="10.49.49.207", LOCALPORT=29118, LSX=0, SCTPINDX=0;
ADD SGSLNK: LNK=2, IPTYPE=IPV4, VLRIPV4_1="10.50.50.205", VLRIPV4_2="10.50.50.204", VLRPORT=29119, LOCALIPV4_1="10.50.50.206", LOCALIPV4_2="10.50.50.207", LOCALPORT=29119, LSX=0, SCTPINDX=0;
```

//查询MME和MSC之间SCTP偶联状态是否正常。

```
DSP SGSLNK: SRT=LNK, LNK=1;
DSP SGSLNK: SRT=LNK, LNK=2;
```

//增加MME到另一个指定MSC的SCTP偶联信息。

```
ADD VLR: VN="86139028", VNM="vlr13", POOLNM="POOL11", MINV=301, MAXV=999; 
ADD SGSLKS: LSX=1, VN="86139028", LSN="sgs2";
ADD SGSLNK: LNK=3, IPTYPE=IPV4, VLRIPV4_1="10.51.51.205", VLRIPV4_2="10.51.51.204", VLRPORT=29118, LOCALIPV4_1="10.51.51.206", LOCALIPV4_2="10.51.51.207", LOCALPORT=29118, LSX=1, SCTPINDX=0;
ADD SGSLNK: LNK=4, IPTYPE=IPV4, VLRIPV4_1="10.52.52.205" ,VLRIPV4_2="10.52.52.204", VLRPORT=29119, LOCALIPV4_1="10.52.52.206", LOCALIPV4_2="10.52.52.207", LOCALPORT=29119, LSX=1, SCTPINDX=0;
```

//查询MME和另一个MSC之间SCTP偶联状态是否正常。

```
DSP SGSLNK: SRT=LNK, LNK=3;
DSP SGSLNK: SRT=LNK, LNK=4;
```

//添加MSC覆盖的LA。

```
ADD LAIVLR: BGNLAI="308015101", ENDLAI="308015101", VLRNO="86139027";
```

//添加LA覆盖的TA范围。

```
ADD TAILAI: BGNTAI="308015101", ENDTAI="308015101", LAI="308015101";
```

//可选：配置缺省LAI记录。

```
ADD TAILAI: BGNTAI="FFFFFFFFFF", ENDTAI="308015101", LAI="308015101";
```

//设置SGs接口业务运行参数。

```
SET SGSPARA: TS6_1=10, TS8=4, TS9=4, TS10=4, NS8=2, NS9=2, NS10=2, ALARMLIMIT=42, AUTOOFFLOAD=YES;
```
