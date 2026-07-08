# 查询LB服务实例（DSP LBSRVINST）

- [命令功能](#ZH-CN_CONCEPT_0129627060__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0129627060__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0129627060__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0129627060__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0129627060__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0129627060__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0129627060)

该命令用于查询业务VNFC申请的LB服务实例信息。

#### [注意事项](#ZH-CN_CONCEPT_0129627060)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0129627060)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0129627060)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINDEX | 服务实例索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC实例索引。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~4294967294<br>说明：首次执行本命令时，无需输入本参数，显示所有<br>“服务VNFC ID（CONSUMERVNFCID）”<br>对应的记录 。后续查询过程中，根据首次查询结果输入本参数，可以查询单条记录。 |
| CONSUMERVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在业务VNFC下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_59103764.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~4294967294 |

#### [使用实例](#ZH-CN_CONCEPT_0129627060)

查询服务VNFC ID为4的LB服务实例信息:

DSP LBSRVINST: CONSUMERVNFCID=4;

```
%%DSP LBSRVINST: CONSUMERVNFCID=4;%%
RETCODE = 0  操作成功

结果如下:
-------------------------
         服务VNFC ID  =  4
        服务实例索引  =  0
        服务实例名称  =  Sig
          服务实例ID  =  0
        网络接入类型  =  带VNRS接入
负载均衡业务感知类型  =  L4业务感知
    负载均衡应用模式  =  通用模式
    负载均衡转发模式  =  通用模式
        首识别策略ID  =  4096
    首负载均衡策略ID  =  8192
              静默期  =  4294967295
            老化时间  =  4294967295
          服务组索引  =  0
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0129627060)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 服务实例索引 | 参数含义：该参数用于表示服务实例索引。 |
| 服务实例名称 | 参数含义：该参数用于表示服务实例名称。<br>取值范围：0~31位字符串 |
| 服务VNFC ID | 参数含义：该参数用于表示业务VNFC ID。 |
| 服务实例ID | 参数含义：该参数用于表示业务VNFC申请的服务实例ID。 |
| 网络接入类型 | 参数含义：该参数用于表示网络接入类型。<br>取值范围：<br>- “ACCESS_TYPE_INNERTS(内置VAS网管接入)”<br>- “ACCESS_TYPE_VNRS(带VNRS_VNFC接入) ”<br>- “ACCESS_TYPE_OUTERTS(外置VAS网管接入) ”<br>- “ACCESS_TYPE_INNERSERVICE(内部服务接入) ” |
| 负载均衡业务感知类型 | 参数含义：该参数用于表示负载均衡业务感知类型。<br>取值范围：<br>- “SRV_SA_TYPE_L3(L3业务感知) ”<br>- “SRV_SA_TYPE_L4(L4业务感知) ”<br>- “SRV_SA_TYPE_L5L7(L5-L7业务感知) ”<br>- “SRV_SA_TYPE_L4_PSEUDO(L4业务感知且支持伪重组) ” |
| 负载均衡应用模式 | 参数含义：该参数用于表示负载均衡应用模式。<br>取值范围：<br>- “SRV_APPLY_TYPE_COMM(通用模式) ”<br>- “SRV_APPLY_TYPE_EXT(扩展模式) ” |
| 负载均衡转发模式 | 参数含义：该参数用于表示负载均衡转发模式。<br>取值范围：<br>- “COMM_FWMODE(通用模式) ”<br>- “GI_FAST_FWMODE(Gi快转模式) ”<br>- “S1_FAST_FWMODE(S1快转模式) ”<br>- “GI_UP_FAST_FWMODE(Giup快转模式) ”<br>- “GI_DOWN_FAST_FWMODE(Gidown快转模式) ”<br>- “TOF_FAST_FWMODE(Tof快转模式) ”<br>- “X3U_FAST_FWMODE(X3u快转模式) ”<br>- “VNAT_FAST_FWMODE(Vnat快转模式) ” |
| 首识别策略ID | 参数含义：该参数用于表示首识别策略ID。 |
| 首负载均衡策略ID | 参数含义：该参数用于表示首负载均衡策略ID。 |
| 静默期 | 参数含义：该参数为预留输出参数。 |
| 老化时间 | 参数含义：该参数用于表示老化时间。 |
| 服务组索引 | 参数含义：该参数用于表示服务组索引。 |
