---
id: UNC@20.15.2@MMLCommand@DSP GLBCDRFLDCFG
type: MMLCommand
name: DSP GLBCDRFLDCFG（查询全局生效CDR字段配置）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GLBCDRFLDCFG
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
- 全局生效话单字段配置查询
status: active
---

# DSP GLBCDRFLDCFG（查询全局生效CDR字段配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来显示全局生效的各类型的话单字段的具体配置。

如果全局模板下某话单类型未绑定模板，则显示该话单类型的缺省配置信息。显示信息中如果模板名字为NULL，则表示是缺省配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [全局生效CDR字段配置（GLBCDRFLDCFG）](configobject/UNC/20.15.2/GLBCDRFLDCFG.md)

## 使用实例

显示全局绑定的话单字段的具体配置信息：

```
DSP GLBCDRFLDCFG:;
```

```

RETCODE = 0  操作成功

全局生效的CDR字段配置
---------------------
                 G-CDR话单字段模板名  =  NULL
              apn-network-identifier  =  使能
                  apn-selection-mode  =  使能
charge-characteristic-selection-mode  =  使能
                         diagnostics  =  使能
                dynamic-address-flag  =  使能
        external-charging-identifier  =  使能
              ims-signalling-context  =  使能
           imsi-unauthenticated-flag  =  不使能
                list-of-service-data  =  使能
              list-of-traffic-volume  =  使能
        local-record-sequence-number  =  使能
                              MSISDN  =  使能
                        ms-time-zone  =  使能
       network-initiated-pdp-context  =  使能
                             node-id  =  使能
                   pdn-connection-id  =  不使能
                            pdp-type  =  使能
                    pgw-address-used  =  不使能
                    pgw-address-ipv6  =  使能
                 pgw-plmn-identifier  =  不使能
     ps-furnish-charging-information  =  使能
                            rat-type  =  使能
                   record-extensions  =  不使能
                        扩展字段类型  =  内容计费
                     业务URL存在标识  =  不使能
                业务使用时长存在标识  =  不使能
                      高精度时间标识  =  不使能
                   Direct Tunnel记录  =  不使能
              record-sequence-number  =  使能
                       served-imeisv  =  使能
                  served-pdp-address  =  使能
            sgsn-sgw-plmn-identifier  =  使能
                          start-time  =  不使能
                           stop-time  =  不使能
             threegpp2-user-location  =  使能
           user-location-information  =  使能
               PGW-CDR话单字段模板名  =  NULL
              apn-network-identifier  =  使能
                  apn-selection-mode  =  使能
charge-characteristic-selection-mode  =  使能
                         diagnostics  =  使能
                dynamic-address-flag  =  使能
        external-charging-identifier  =  使能
              ims-signalling-context  =  使能
           imsi-unauthenticated-flag  =  不使能
                list-of-service-data  =  使能
              list-of-traffic-volume  =  使能
        local-record-sequence-number  =  使能
                              MSISDN  =  使能
                        ms-time-zone  =  使能
       network-initiated-pdp-context  =  使能
                             node-id  =  使能
                   pdn-connection-id  =  不使能
                            pdp-type  =  使能
                    pgw-address-used  =  不使能
                    pgw-address-ipv6  =  使能
                 pgw-plmn-identifier  =  不使能
     ps-furnish-charging-information  =  使能
                            rat-type  =  使能
                   record-extensions  =  不使能
                        扩展字段类型  =  内容计费
                     业务URL存在标识  =  不使能
                业务使用时长存在标识  =  不使能
                      高精度时间标识  =  不使能
                   Direct Tunnel记录  =  不使能
              record-sequence-number  =  使能
                       served-imeisv  =  使能
                  served-pdp-address  =  使能
            sgsn-sgw-plmn-identifier  =  使能
                          start-time  =  不使能
                           stop-time  =  不使能
             threegpp2-user-location  =  使能
           user-location-information  =  使能
               SGW-CDR话单字段模板名  =  NULL
              apn-network-identifier  =  使能
                  apn-selection-mode  =  使能
charge-characteristic-selection-mode  =  使能
                         diagnostics  =  使能
                dynamic-address-flag  =  使能
        external-charging-identifier  =  使能
              ims-signalling-context  =  使能
           imsi-unauthenticated-flag  =  不使能
                list-of-service-data  =  使能
              list-of-traffic-volume  =  使能
        local-record-sequence-number  =  使能
                              MSISDN  =  使能
                        ms-time-zone  =  使能
       network-initiated-pdp-context  =  使能
                             node-id  =  使能
                   pdn-connection-id  =  不使能
                            pdp-type  =  使能
                    pgw-address-used  =  不使能
                    pgw-address-ipv6  =  使能
                 pgw-plmn-identifier  =  不使能
     ps-furnish-charging-information  =  使能
                            rat-type  =  使能
                   record-extensions  =  不使能
                        扩展字段类型  =  内容计费
                     业务URL存在标识  =  不使能
                业务使用时长存在标识  =  不使能
                      高精度时间标识  =  不使能
                   Direct Tunnel记录  =  不使能
              record-sequence-number  =  使能
                       served-imeisv  =  使能
                  served-pdp-address  =  使能
            sgsn-sgw-plmn-identifier  =  使能
                          start-time  =  不使能
                           stop-time  =  不使能
             threegpp2-user-location  =  使能
           user-location-information  =  使能
           ePDG UE Local IP and Port  =  不携带该字段
              low-priority-indicator  =  不携带该字段
                    apn-rate-control  =  不携带该字段
                   mo-exception-data  =  不携带该字段
           serving-plmn-rate-control  =  不携带该字段
                 ULI携带WLAN地址信息  =  不包含该字段。
                    sgw-address-ipv6  =  携带该字段
                       packet-number  =  不使能
                   object identifier  =  1.3.6.1.4.1.2011.2.63
                   object identifier  =  1.3.6.1.4.1.2011.2.63
                   mo-exception-data  =  不携带该字段
                    apn-rate-control  =  不携带该字段
           serving-plmn-rate-control  =  不携带该字段
       cp-eps-optimisation-indicator  =  不携带该字段
                    sgw-address-ipv6  =  携带该字段
                    sgw-address-ipv6  =  携带该字段
            ePDG UE Local IP 和 Port  =  不携带该字段
              low-priority-indicator  =  不携带该字段
           serving-plmn-rate-control  =  不携带该字段
       cp-eps-optimisation-indicator  =  不携带该字段
       RAN-SecondaryRAT-Usage-Report  =  不使能
                       packet-number  =  不使能
                uni-pdu-cp-only-flag  =  不携带该字段
                   object identifier  =  1.3.6.1.4.1.2011.2.63
           sgi-ptp-tunnelling-method  =  不携带该字段
                  pdp-type-extention  =  不携带该字段
                      scs-as-address  =  不携带该字段
                  pdp-type-extention  =  不携带该字段
       cp-eps-optimisation-indicator  =  不携带该字段
                 ULI携带WLAN地址信息  =  不包含该字段。
                  pdp-type-extention  =  不携带该字段
       RAN-SecondaryRAT-Usage-Report  =  不使能
                    apn-rate-control  =  不携带该字段
              low-priority-indicator  =  不携带该字段
           sgi-ptp-tunnelling-method  =  不携带该字段
           sgi-ptp-tunnelling-method  =  不携带该字段
                uni-pdu-cp-only-flag  =  不携带该字段
       RAN-SecondaryRAT-Usage-Report  =  不使能
                uni-pdu-cp-only-flag  =  不携带该字段
                      scs-as-address  =  不携带该字段
            ePDG UE Local IP 和 Port  =  不携带该字段
                      scs-as-address  =  不携带该字段
                       packet-number  =  不使能
                 ULI携带WLAN地址信息  =  不包含该字段。
                   mo-exception-data  =  不携带该字段
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局生效CDR字段配置（DSP-GLBCDRFLDCFG）_09897014.md`
