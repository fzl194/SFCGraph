---
id: UNC@20.15.2@MMLCommand@DSP NGLCSCTX
type: MMLCommand
name: DSP NGLCSCTX（显示5G定位上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGLCSCTX
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# DSP NGLCSCTX（显示5G定位上下文信息）

## 功能

**适用NF：AMF**

该命令用于查询5G定位上下文的相关信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G用户的IMSI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGLCSCTX]] · 5G定位上下文信息（NGLCSCTX）

## 使用实例

查询IMSI为123451234567890用户的定位上下文信息，执行如下命令：

```
%%DSP NGLCSCTX:IMSI="123451234567890";%%
RETCODE = 0  操作成功

结果如下
--------
                     IMSI  =  123451234567890
              CallBackURI  =  http://192.168.118.1:5080/ngmlc-loc/v1/location-update
              LMF的实例号  =  NULL
	    CorrelationId  =  NULL
                   Lmf Id  =  NULL
Location Notification Uri  =  http://192.168.118.1:5080/ngmlc-loc/hgmlc/v1/provide-location
             Lcs Location  =  DeferredLocation
          Lcs Client Type  =  ValueAddedServices
            Ldr Reference  =  11
                  Lcs QoS  =  HAccuracy:1;VAccuracy:1;VerticalRequested:false;ResponseTime:Invalid
 Lcs Supported GAD Shapes  =  Invalid
      Periodic Event Info  =  ReportingAmount:1;ReportingInterval:1
                 Priority  =  Invalid
       Velocity Requested  =  Invalid
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGLCSCTX.md`
