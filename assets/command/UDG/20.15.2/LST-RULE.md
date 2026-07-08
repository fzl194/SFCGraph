---
id: UDG@20.15.2@MMLCommand@LST RULE
type: MMLCommand
name: LST RULE（查询规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RULE
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
- 业务规则管理
- 规则
status: active
---

# LST RULE（查询规则）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询规则。

## 注意事项

支持批量查询。如果不输入策略名称，则查询系统中所有的规则。如果输入了策略类型，则查询系统中配置为本策略类型的所有规则。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：设置该参数时表示查询指定名称的规则，未设置该参数时表示查询系统中所有的规则。 |
| POLICYTYPE | 策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PCC：计费与策略控制，代表该规则可以配置PCC策略，用于实现计费和策略控制功能。<br>- BWM：带宽管理，代表该规则可以配置带宽管理分类策略，其分类结果可以用于带宽管理的策略匹配功能。<br>- HEADEN：头增强，代表该规则可以配置头增强策略，可以基于配置的头增强策略向HTTP/RTSP请求报文头域中插入字段。<br>- WEBPROXY：Web Proxy，代表该规则可以配置WebProxy的IPFarm对象名称，用于设置WebProxy选择的服务器地址池。<br>- IPREDIR：IP重定向，代表该规则可以配置IP重定向的目标IP地址，支持IPv4和IPv6两种类型的IP地址。<br>- SMARTREDIRECT：智能重定向，代表该规则可以配置CaptivePortal业务对应的IPFarm的名称，HTTP智能重定向的名称，DNS重写动作的名称或者重定向的名称。<br>- REMARK_FPI：Remark、FPI或者SAI，代表该规则可以配置IP报文的DSCP重标记值、FPI策略或SAI策略。<br>- SRV_TRIGGER：Service Trigger Radius，代表该规则可以配置业务触发Radius消息交互功能标识，并配置Radius交互过程中报文处理方式。<br>- TRAFFICCLASS：Traffic Classifier，代表该规则可以配置Service Chain对象名称，用于实现业务链功能，此参数当前不支持。<br>- LBO：Local Break Out，代表该规则可以用于本地业务分流，此参数当前不支持。<br>- FIREWALL：防火墙，代表该规则可以配置防火墙策略。<br>- ADC：代表该规则用于应用检测与控制功能。<br>- QOS：代表该规则可以配置QoS策略，可以基于配置的QoS策略进行业务级QoS处理。<br>- WORKER：代表该规则用于通用Rule业务。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |
| RULESPECTYPE | 规则规格类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则类型，当取值为SPECIFICATION_LIMITED时，表示规格受限规则，表示会话安装的规则数和被USERPROFILE绑定的规则数量均存在一定限制。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT：默认配置。<br>- SPECIFICATION_LIMITED：规格受限配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RULE]] · 规则（RULE）

## 使用实例

- 查询一条名为testrule的规则：
  ```
  LST RULE: RULENAME="testrule";
  ```
  ```

  RETCODE = 0  操作成功

  规则信息
  --------
                                        规则名称  =  testrule
                                        策略类型  =  PCC
                                    规则规格类型  =  默认配置
                                  黑名单规则标识  =  普通规则
                                    流过滤器名称  =  testflowfiltername
                                  流过滤器组名称  =  NULL
                                      时间段名称  =  NULL
                                   PCC策略组名称  =  pccpolicygroup
                                    分类属性名称  =  NULL
                                      头增强名称  =  NULL
                              Radius消息触发标识  =  不使能
                Radius消息触发时报文默认处理动作  =  转发
                           Web Proxy IP-Farm名称  =  NULL
                          IP重定向虚拟IP协议版本  =  IPV4
                                IP重定向IPv6地址  =  ::
                                  IP重定向IP地址  =  0.0.0.0
                      Captive Portal IP-Farm名称  =  NULL
                            重标记、FPI或SAI选择  =  重标记
                                  Remark配置类型  =  CLASS
                                  Remark分类类型  =  NULL
                                          重标记  =  NULL
                                           FPI值  =  NULL
                                      业务链名称  =  NULL
                                本地业务分流标识  =  不使能
                                  防火墙策略名称  =  NULL
                        流过滤器或流过滤器组选择  =  流过滤器
                                     Qos属性名称  =  NULL
                                 ADC静默通知标识  =  使能
                                   URL重定向名称  =  NULL
                                 DNS重写动作名字  =  NULL
                                  智能重定向名称  =  NULL
  指定业务触发radius消息发送时的业务报文延时时间  =  0
                              通用Rule子策略名称  =  NULL
                                    通用策略参数  =  NULL
                                      配置域名称  =  NULL
                                替换用户模板名称  =  NULL
                                      全局优先级  =  4294967295
                                     ALG功能开关  =  不使能
                                     业务感知ID  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有规则：
  ```
  LST RULE:;
  ```
  ```

  RETCODE = 0  操作成功

  规则信息
  --------
  规则名称   策略类型  规则规格类型  黑名单规则标识  流过滤器名称  流过滤器组名称  时间段名称  PCC策略组名称  分类属性名称  头增强名称  Radius消息触发标识  Radius消息触发时报文默认处理动作  Web Proxy IP-Farm名称  IP重定向虚拟IP协议版本  IP重定向IPv6地址  IP重定向IP地址  Captive Portal IP-Farm名称  重标记、FPI或SAI选择  Remark配置类型  Remark分类类型  重标记  FPI值  业务链名称  本地业务分流标识  防火墙策略名称  流过滤器或流过滤器组选择  Qos属性名称  ADC静默通知标识  URL重定向名称  DNS重写动作名字  智能重定向名称  指定业务触发radius消息发送时的业务报文延时时间  通用Rule子策略名称  通用策略参数  配置域名称  替换用户模板名称  全局优先级  ALG功能开关     业务感知ID  
 
  testrule1  PCC       默认配置      普通规则        flowfilter    NULL            NULL        pccplygrp      NULL          NULL        不使能              转发                              NULL                   IPV4                    ::                0.0.0.0         NULL                        重标记                CLASS           NULL            NULL    NULL   NULL        不使能            NULL            流过滤器                  NULL         使能             NULL           NULL             NULL            0                                               NULL                NULL          NULL        NULL              4294967295  不使能  NULL        
  testrule2  PCC       默认配置      普通规则        flowfilter    NULL            NULL        pccplygrp      NULL          NULL        不使能              转发                              NULL                   IPV4                    ::                0.0.0.0         NULL                        重标记                CLASS           NULL            NULL    NULL   NULL        不使能            NULL            流过滤器                  NULL         使能             NULL           NULL             NULL            0                                               NULL                NULL          NULL        NULL              4294967295  不使能  NULL        
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询规则（LST-RULE）_82837270.md`
