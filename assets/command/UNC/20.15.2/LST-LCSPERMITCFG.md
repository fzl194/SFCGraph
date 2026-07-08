---
id: UNC@20.15.2@MMLCommand@LST LCSPERMITCFG
type: MMLCommand
name: LST LCSPERMITCFG（查询定位服务权限配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LCSPERMITCFG
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G定位服务管理
- 定位服务权限配置管理
status: active
---

# LST LCSPERMITCFG（查询定位服务权限配置）

## 功能

**适用NF：AMF**

该命令用于查询定位服务权限配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTYPE | 定位服务操作类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定定位服务的服务操作类型。<br>数据来源：全网规划<br>取值范围：<br>- “Namf_Location_ProvidePositioningInfo（请求UE地理位置信息）”：NF服务消费者（例如GMLC）调用此服务请求UE地理位置信息。<br>- “Namf_Location_ProvideLocationInfo（请求网络侧提供UE位置信息）”：NF服务消费者（例如UDM）调用此服务请求网络侧提供UE位置信息。<br>- “Namf_Location_EventNotify（位置事件通知）”：用于通知NF服务消费者（例如GMLC）关于与紧急业务或延迟定位等UE位置相关的事件信息。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定定位服务消费者的IPV4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0表示无效值。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定定位服务消费者的IPV6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。0:0:0:0:0:0:0:0表示无效值。<br>默认值：无<br>配置原则：无 |
| USRGRPID | 用户群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G用户群标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：<br>该用户群标识必须已经通过ADD NGUSRGRP命令添加成功，可执行LST NGUSRGRP进行查看，用户群中的用户可通过ADD NGUSRGRPMEM添加。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LCSPERMITCFG]] · 定位服务权限配置（LCSPERMITCFG）

## 使用实例

查询定位服务权限配置，执行如下命令：

```
%%LST LCSPERMITCFG:;%%
RETCODE = 0  操作成功

结果如下
--------
定位服务操作类型  =  请求UE地理位置信息
        IPV4地址  =  10.10.10.10
        IPV6地址  =  NULL
    用户群组标识  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LCSPERMITCFG.md`
