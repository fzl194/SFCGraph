---
id: UNC@20.15.2@MMLCommand@LST OFCTEMPLATE
type: MMLCommand
name: LST OFCTEMPLATE（显示离线计费模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OFCTEMPLATE
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
- 离线计费基础参数
- 离线计费模板
status: active
---

# LST OFCTEMPLATE（显示离线计费模板）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用于查询离线计费模板的参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCTEMPLATENAME | 离线计费模板名 | 可选必选说明：可选参数<br>参数含义：配置离线模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OFCTEMPLATE]] · 离线计费模板（OFCTEMPLATE）

## 使用实例

要显示一个名字为“ofc_test”的OFCTemplate的实例：

```
LST OFCTEMPLATE:OFCTEMPLATENAME="ofc_test";
```

```

RETCODE = 0  操作成功

离线计费模板配置
----------------
                             离线计费模板名  =  ofc_test
                             继承上一级配置  =  继承
                             时长阈值（分）  =  60
                         流量阈值（千字节）  =  10240
                     最小流量阈值（千字节）  =  0
                           计费条件改变阈值  =  3
                   Serving Node改变次数阈值  =  3
                     最大携带的业务容器数量  =  20
                                CDR RAT更新  =  使能
                              RAT更新优先级  =  255
                           Serving Node更新  =  使能
                     Serving Node更新优先级  =  255
                               计费条件改变  =  使能
                         计费条件改变优先级  =  255
                                 MS时区更新  =  使能
                               MS时区优先级  =  255
                  Serving Node PLMN标识更新  =  使能
                Serving Node PLMN标识优先级  =  255
                          Container RAT更新  =  使能
                                    QoS更新  =  使能
                           Serving Node更新  =  使能
                                CGI/SAI更新  =  使能
                                   ECGI更新  =  使能
                                    TAI更新  =  使能
                                    ULI更新  =  使能
        Container Serving Node PLMN标识更新  =  使能
                                    RAI更新  =  使能
                                   费率切换  =  使能
                                  G-CDR版本  =  R98V760
                                PGW-CDR版本  =  R9V950_PGW_CDR
                                SGW-CDR版本  =  R10_SGW_CDR
                               时长配额机制  =  QUOTA_CONSUME_TIME
                              QCT时长（秒）  =  197
                              BTI时长（秒）  =  60
           Record Sequence Number字段起始值  =  0
                               话单时间格式  =  本地时间
                              QHT时长（秒）  =  0
     在线计费转离线计费后的时长阈值（分钟）  =  4294967295
                          PCRF发起的QoS更新  =  不使能
        MO Exception Data Counter更新优先级  =  255
          CDR MO Exception Data Counter更新  =  使能
                                 用户面更新  =  使能
                            APN控制速率改变  =  使能
          APN速率控制改变流量容器关闭原因值  = 服务PLMN控制速率改变
RAN-SecondaryRAT-Usage-Report生成话单的阈值  =  3
                                 eNodeB更新  =  使能
                       服务PLMN控制速率改变  =  使能
   在线计费转离线计费后的流量阈值（千字节）  =  9000000001
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示离线计费模板（LST-OFCTEMPLATE）_09896914.md`
