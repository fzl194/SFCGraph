---
id: UNC@20.15.2@MMLCommand@DSP GLBOFCTEMPCFG
type: MMLCommand
name: DSP GLBOFCTEMPCFG（查询全局生效离线计费模板配置）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GLBOFCTEMPCFG
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费维护
- 全局生效离线计费配置查询
status: active
---

# DSP GLBOFCTEMPCFG（查询全局生效离线计费模板配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查看全局离线计费模板生效的配置信息。

如果全局离线计费配置未绑定离线计费模板，则显示全局缺省配置。显示信息中如果模板名字为NULL，则表示是全局缺省配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBOFCTEMPCFG]] · 全局生效离线计费模板配置（GLBOFCTEMPCFG）

## 使用实例

查看全局离线计费模板的具体配置信息：

```
DSP GLBOFCTEMPCFG:;
```

```

RETCODE = 0  操作成功

全局生效离线计费配置
--------------------
                           GGSN离线计费模板  =  NULL
                                   时长阈值  =  60
                                   流量阈值  =  10240
                               最小流量阈值  =  0
                           计费条件改变阈值  =  3
                   Serving Node改变次数阈值  =  3
                     最大携带的业务容器数量  =  20
                               GCDR RAT更新  =  使能
                              RAT更新优先级  =  255
                           Serving Node更新  =  使能
                     Serving Node更新优先级  =  255
                               计费条件改变  =  使能
                         计费条件改变优先级  =  255
                                 MS时区更新  =  使能
                               MS时区优先级  =  255
                  Serving Node PLMN标识更新  =  使能
                Serving Node PLMN标识优先级  =  255
                         GContainer RAT更新  =  使能
                                    QoS更新  =  使能
                           Serving Node更新  =  使能
                                CGI/SAI更新  =  使能
                                   ECGI更新  =  使能
                                    TAI更新  =  使能
                                    ULI更新  =  使能
                  Serving Node PLMN标识更新  =  使能
                                    RAI更新  =  使能
                                   费率切换  =  使能
                                  G-CDR版本  =  R7V740_EGCDR
                                PGW-CDR版本  =  R8V850_PGW_CDR
                                SGW-CDR版本  =  R8V850_SGW_CDR
                               时长配额机制  =  QUOTA_CONSUME_TIME
                                    QCT时长  =  0
                                    BTI时长  =  60
           Record Sequence Number字段起始值  =  0
                               话单时间格式  =  本地时间
                                    QHT时长  =  0
                            PGW离线计费模板  =  NULL
                                   时长阈值  =  60
                                   流量阈值  =  10240
                               最小流量阈值  =  0
                           计费条件改变阈值  =  3
                   Serving Node改变次数阈值  =  3
                     最大携带的业务容器数量  =  20
                               PCDR RAT更新  =  使能
                              RAT更新优先级  =  255
                           Serving Node更新  =  使能
                     Serving Node更新优先级  =  255
                               计费条件改变  =  使能
                         计费条件改变优先级  =  255
                                 MS时区更新  =  使能
                               MS时区优先级  =  255
                  Serving Node PLMN标识更新  =  使能
                Serving Node PLMN标识优先级  =  255
                         Pcontainer RAT更新  =  使能
                                    QoS更新  =  使能
                           Serving Node更新  =  使能
                                CGI/SAI更新  =  使能
                                   ECGI更新  =  使能
                                    TAI更新  =  使能
                                    ULI更新  =  使能
                  Serving Node PLMN标识更新  =  使能
                                    RAI更新  =  使能
                                   费率切换  =  使能
                                  G-CDR版本  =  R7V740_EGCDR
                                PGW-CDR版本  =  R8V850_PGW_CDR
                                SGW-CDR版本  =  R8V850_SGW_CDR
                               时长配额机制  =  QUOTA_CONSUME_TIME
                                    QCT时长  =  0
                                    BTI时长  =  60
           Record Sequence Number字段起始值  =  0
                               话单时间格式  =  本地时间
                                    QHT时长  =  0
                            SGW离线计费模板  =  NULL
                                   时长阈值  =  60
                                   流量阈值  =  10240
                               最小流量阈值  =  0
                           计费条件改变阈值  =  3
                   Serving Node改变次数阈值  =  3
                     最大携带的业务容器数量  =  20
                               SCDR RAT更新  =  使能
                              RAT更新优先级  =  255
                           Serving Node更新  =  使能
                     Serving Node更新优先级  =  255
                               计费条件改变  =  使能
                         计费条件改变优先级  =  255
                                 MS时区更新  =  使能
                               MS时区优先级  =  255
                  Serving Node PLMN标识更新  =  使能
                Serving Node PLMN标识优先级  =  255
                         Scontainer RAT更新  =  使能
                                    QoS更新  =  使能
                           Serving Node更新  =  使能
                                CGI/SAI更新  =  使能
                                   ECGI更新  =  使能
                                    TAI更新  =  使能
                                    ULI更新  =  使能
                  Serving Node PLMN标识更新  =  使能
                                    RAI更新  =  使能
                                   费率切换  =  使能
                                  G-CDR版本  =  R7V740_EGCDR
                                PGW-CDR版本  =  R8V850_PGW_CDR
                                SGW-CDR版本  =  R8V850_SGW_CDR
                               时长配额机制  =  QUOTA_CONSUME_TIME
                                    QCT时长  =  0
                                    BTI时长  =  60
           Record Sequence Number字段起始值  =  0
                               话单时间格式  =  本地时间
                                    QHT时长  =  0
                       服务PLMN控制速率改变  =  使能
          CDR MO Exception Data Counter更新  =  使能
     在线计费转离线计费后的时长阈值（分钟）  =  4294967295
     在线计费转离线计费后的时长阈值（分钟）  =  4294967295
                          PCRF发起的QoS更新  =  不使能
                                 用户面更新  =  使能
   在线计费转离线计费后的流量阈值（千字节）  =  9000000001
                            APN控制速率改变  =  使能
          APN速率控制改变流量容器关闭原因值  = 服务PLMN控制速率改变
     在线计费转离线计费后的时长阈值（分钟）  =  4294967295
                                 用户面更新  =  使能
                       服务PLMN控制速率改变  =  使能
                          PCRF发起的QoS更新  =  不使能
                                 用户面更新  =  使能
                          PCRF发起的QoS更新  =  不使能
   在线计费转离线计费后的流量阈值（千字节）  =  9000000001
RAN-SecondaryRAT-Usage-Report生成话单的阈值  =  3
RAN-SecondaryRAT-Usage-Report生成话单的阈值  =  3
        MO Exception Data Counter更新优先级  =  255
        MO Exception Data Counter更新优先级  =  255
        MO Exception Data Counter更新优先级  =  255
                                 eNodeB更新  =  使能
   在线计费转离线计费后的流量阈值（千字节）  =  9000000001
          CDR MO Exception Data Counter更新  =  使能
RAN-SecondaryRAT-Usage-Report生成话单的阈值  =  3
                            APN控制速率改变  =  使能
          APN速率控制改变流量容器关闭原因值  = 服务PLMN控制速率改变
                                 eNodeB更新  =  使能
          CDR MO Exception Data Counter更新  =  使能
                                 eNodeB更新  =  使能
                            APN控制速率改变  =  使能
          APN速率控制改变流量容器关闭原因值  = 服务PLMN控制速率改变
                       服务PLMN控制速率改变  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GLBOFCTEMPCFG.md`
