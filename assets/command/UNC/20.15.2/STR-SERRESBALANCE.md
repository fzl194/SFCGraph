---
id: UNC@20.15.2@MMLCommand@STR SERRESBALANCE
type: MMLCommand
name: STR SERRESBALANCE（启动业务资源均衡操作）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: SERRESBALANCE
command_category: 动作类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 虚拟化和弹性伸缩
- 业务资源部署位置
status: active
---

# STR SERRESBALANCE（启动业务资源均衡操作）

## 功能

![](启动业务资源均衡操作(STR SERRESBALANCE)_72345965.assets/notice_3.0-zh-cn_2.png)

资源均衡过程中可能会影响现有业务，建议在业务低峰时执行此命令。

**适用网元：SGSN、MME**

1. 此命令用于手动启动系统内资源均衡。
2. 系统扩容、减容或出现进程或节点故障场景时，可能出现系统资源在进程或节点之间部署不均。
3. RM_TYPE_USER、RM_TYPE_S1ECMCONN、RM_TYPE_S1UCMCONN、RM_TYPE_GTPUPDP、RM_TYPE_GBCELL、RM_TYPE_GBUSER、RM_TYPE_IUUSRCONN、RM_TYPE_NGAPLNK这几类资源在执行此命令后，不能保证进程间完全均衡，各个进程间上下文差值占进程上下文规格的比例小于10%。其他资源在执行此命令后，能保证各个进程间上下文分布均衡。
4. 资源部署不均衡对进程的影响:
    - RM_TYPE_DMLNK(Diameter链路)、RM_TYPE_M3UALNK(M3UA链路)、RM_TYPE_SGSVLRLNK(SGS链路)、RM_TYPE_DNSCONN(DNS本端端点)、RM_TYPE_S1ECMCONN（S1链路）、RM_TYPE_S1UCMCONN（S1连接）、RM_TYPE_IUUSRCONN(IU连接)、RM_TYPE_NGAPLNK（N2链路）这些资源部署在SGP进程上，这些资源部署不均衡可能导致SGP CPU开销不均。
    - RM_TYPE_GBCELL(2G小区)、RM_TYPE_NSE(NSE)、RM_TYPE_GBUSER(GB用户上下文)这些资源部署在GBP进程上，这些资源部署不均衡可能导致GBP CPU开销不均。
    - RM_TYPE_GTPCPATH(GTPC本端端点)、RM_TYPE_GTPUPATH(GTPU本端端点)、RM_TYPE_GTPUPDP(用户面PDP上下文)这些资源部署在UPP进程上，这些资源不均衡可能导致UPP CPU开销不均。
    - RM_TYPE_USER(用户和承载上下文)这个资源部署在SPP进程上，这个资源不均衡可能导致SPP CPU开销不均。

## 注意事项

- 该命令执行后立刻生效。
- 资源均衡过程中，现有业务会有影响。建议在业务低峰时段进行资源迁移。
- 迁移过程中出现进程或节点复位，则停止均衡。通过[**DSP SERRESLOC**](显示业务资源部署位置(DSP SERRESLOC)_26306176.md)命令可以查询各种资源在系统中的部署情况。
- 该命令生效以后，需要等待4分钟左右才能实现资源的均衡，此过程中如果节点或者进程复位，则停止均衡。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERRESTYPE | 业务资源类型 | 可选必选说明：必选参数<br>参数含义：需要重新进行负载均衡的业务资源。<br>MNT_RM_TYPE_USER：用户和承载上下文资源。<br>MNT_RM_TYPE_DMLNK：Diameter链路资源。<br>MNT_RM_TYPE_S1ECMCONN：S1链路资源。<br>MNT_RM_TYPE_S1UCMCONN：S1连接资源。<br>MNT_RM_TYPE_GTPCPATH：GTPC本端端点资源。<br>MNT_RM_TYPE_GTPUPATH：GTPU本端端点资源。<br>MNT_RM_TYPE_DNSCONN：DNS本端端点资源。<br>MNT_RM_TYPE_M3UALNK：M3UA链路资源。<br>MNT_RM_TYPE_GTPUPDP：用户面PDP上下文资源。MNT_RM_TYPE_SGSVLRLNK：SGS链路资源。<br>MNT_RM_TYPE_IUUSRCONN：IU连接资源。<br>MNT_RM_TYPE_GBCELL：2G小区资源。<br>MNT_RM_TYPE_GBUSER：GB用户上下文资源。<br>MNT_RM_TYPE_NSE：GB NSE资源。<br>MNT_RM_TYPE_NGAPLNK：N2链路资源。<br>取值范围:<br>- “MNT_RM_TYPE_USER(USER)”<br>- “MNT_RM_TYPE_DMLNK(DMLNK)”<br>- “MNT_RM_TYPE_S1ECMCONN(S1ECMCONN)”<br>- “MNT_RM_TYPE_S1UCMCONN(S1UCMCONN)”<br>- “MNT_RM_TYPE_GTPCPATH(GTPCPATH)”<br>- “MNT_RM_TYPE_GTPUPATH(GTPUPATH)”<br>- “MNT_RM_TYPE_DNSCONN(DNSCONN)”<br>- “MNT_RM_TYPE_M3UALNK(M3UALNK)”<br>- “MNT_RM_TYPE_GTPUPDP(GTPUPDP)”<br>- “MNT_RM_TYPE_SGSVLRLNK(SGSVLRLNK)”<br>- “MNT_RM_TYPE_IUUSRCONN(IUUSRCONN)”<br>- “MNT_RM_TYPE_GBCELL(GBCELL)”<br>- “MNT_RM_TYPE_GBUSER(GBUSER)”<br>- “MNT_RM_TYPE_NSE(NSE)”<br>- “MNT_RM_TYPE_NGAPLNK(NGAPLNK)”<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过VNFP上的<br>[**LST VNFC**](../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SERRESBALANCE]] · 业务资源均衡操作（SERRESBALANCE）

## 使用实例

启动业务资源均衡操作，选择MNT_RM_TYPE_USER(用户和承载上下文资源)的业务资源：

STR SERRESBALANCE: SERRESTYPE=MNT_RM_TYPE_USER, SERVICETYPE="USN_VNFC";

```
%%STR SERRESBALANCE: SERRESTYPE=MNT_RM_TYPE_USER
, SERVICETYPE="USN_VNFC";
%%
RETCODE = 0  操作成功。

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-SERRESBALANCE.md`
