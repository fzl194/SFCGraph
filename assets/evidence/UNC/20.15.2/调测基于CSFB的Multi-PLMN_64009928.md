# 调测基于CSFB的Multi PLMN

- [操作场景](#ZH-CN_OPI_0164009928__1.3.1)
- [必备事项](#ZH-CN_OPI_0164009928__1.3.2)
- [操作步骤](#ZH-CN_OPI_0164009928__1.3.3)

## [操作场景](#ZH-CN_OPI_0164009928)

本操作介绍了通过调测手段检查 UNC 是否正确配置该功能的过程。

> **说明**
> 适用于MME

## [必备事项](#ZH-CN_OPI_0164009928)

前提条件

基于CSFB的Multi PLMN功能已经激活。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0164009928)

- 调测基于CSFB的Multi PLMN业务。
    1. 创建用户跟踪。
      参数选择如下：
          - IMSI:被跟踪用户的IMSI。
          - 其它参数：选择默认值。
    2. 通过 [**ADD HPLMN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) 命令增加两条PLMN配置，分别为PLMN1，PLMN2，用户A，用户B分别签约PLMN1及PLMN2。通过 **[ADD TAILAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)** 配置TAI与LAI的映射关系。两个用户发起附着流程，附着成功。
    3. eNodeB基于本地配置和MME下发的PLMN ID，将PLMN1及PLMN2广播给UE。
    4. 用户A及用户B分别从空口接收到的相应的PLMN ID，选择HPLMN接入到eNodeB。
    5. eNodeB将Selected PLMN ID并入到TAI中，发送给MME。
    6. MME收到Initial UE Message（Attach Request或者TAU Request）消息后，根据消息中携带的TAI查询本地配置TAILAI映射表获取到LAI，再次查询本地配置找到这个LAI所对应的MSC。查询过程请参见 [WSFD-102301 基于CSFB的语音业务](../WSFD-102301 基于CSFB的语音业务_70014756.md) 。
    7. MME在返回Attach Accept或者Tau Accept时，将LAI信息下发给UE。
