---
id: UDG@20.15.2@MMLCommand@LST SRVCOMMONPARA
type: MMLCommand
name: LST SRVCOMMONPARA（查询业务公共参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRVCOMMONPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- 业务公共参数
status: active
---

# LST SRVCOMMONPARA（查询业务公共参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示业务相关控制参数，如RTSP业务在暂停时是否收费的标识以及RTSP按照什么模式计费等。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [业务公共参数（SRVCOMMONPARA）](configobject/UDG/20.15.2/SRVCOMMONPARA.md)

## 使用实例

显示业务公共参数：

```
LST SRVCOMMONPARA:;
```

```

RETCODE = 0  操作成功。

业务公共参数信息
----------------
                         带宽规则匹配协议层级选择  =  应用层
                          ADC规则匹配协议层级选择  =  应用层
                             性能统计协议层级选择  =  应用层
                               RTSP暂停时收费开关  =  不使能
                                     RTSP计费模式  =  ALL
                       专有承载老化删除时间（秒）  =  120
                        重定向报文FUP流量统计标识  =  使能
                            X-Online-Host生效标识  =  使能
                        token校验用的时间差（秒）  =  300
                                TunnelMarking开关  =  不使能
                  用户session的五元组节点最大数量  =  600
                                     默认流量配额  =  10000
                               默认流量配额的单位  =  字节
                               默认时长配额（秒）  =  5
DNS的serverip和domain对应关系老化时间配置（小时）  =  0
                       信令报文计费关联时间（秒）  =  60
                                 HTTP重定向返回码  =  302
                                 计费节点老化开关  =  使能
                           计费节点老化时间（秒）  =  3600
                               更新特征库规则开关  =  使能
                              HTTP2.0协议回落开关  =  使能
                     单用户最大流表数动态调整开关  =  使能
                                SA支持URL最大长度  =  1023
                                URL重定向最大长度  =  511
                            PCC动态重定向流控标识  =  不使能
                  PCC动态重定向流控时间间隔（秒）  =  5
                            重定向携带前缀URL开关  =  重定向URL不携带前缀URL
                           防火墙策略矫正时间(秒)  =  300
                                      DNS超长域名  =  前缀域名
                       内嵌IPv4的IPv6前缀功能开关  =  不使能
                               内嵌IPv4的IPv6前缀  =  NULL
                             VOIP大类识别功能开关  =  不使能
                 HTTPS SA协议确定后进行匹配的开关  =  不使能
                                   RTSP重定向开关  =  不使能
               SA协议识别加速处理时的最大报文个数  =  4
                         Proxy-Connection字段开关  =  不使能
                            特定类型的DNS报文开关  =  不使能
        HTTP connect报文中的X-Online-Host字段开关  =  不使能
                包含路径信息的SNI匹配七层规则开关  =  不使能
                             重定向完成时间（秒）  =  15
                                 SA发现协议的开关  =  不使能
                                   SA流量统计开关  =  不使能
                                 报表协议层级选择  =  应用层

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务公共参数（LST-SRVCOMMONPARA）_82837310.md`
