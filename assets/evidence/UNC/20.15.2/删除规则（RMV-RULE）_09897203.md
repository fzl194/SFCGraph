# 删除规则（RMV RULE）

- [命令功能](#ZH-CN_CONCEPT_0209897203__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897203__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897203__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897203__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897203__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897203)

**适用NF：PGW-C、SMF**

![](删除规则（RMV RULE）_09897203.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，此操作会删除规则下所有绑定关系，可能会导致正在使用此规则的用户出现规则匹配错误、计费错误等现象，进而影响用户使用业务。

该命令用于删除规则。

#### [注意事项](#ZH-CN_CONCEPT_0209897203)

- 该命令执行后立即生效。
- 如果Rule与用户模板（UserProfile）绑定，删除Rule会自动解除与用户模板的绑定关系。
- 如果Rule与数据网络访问标识符（DNAI）绑定，删除Rule会自动解除与数据网络访问标识符的绑定关系。
- 如果Rule正在被业务使用，则不允许删除。
- 如果不输入任何参数，表示删除系统中所有的规则。当配置量较大时单次执行可能无法删除全部记录，需要执行多次。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897203)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897203)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：设置该参数时表示删除指定名称的规则，未设置该参数时表示删除系统中所有的规则。 |
| POLICYTYPE | 策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置策略类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- PCC：计费与策略控制，代表该规则可以配置PCC策略，用于实现计费和策略控制功能。<br>- BWM：带宽管理，代表该规则可以配置带宽管理分类策略，其分类结果可以用于带宽管理的策略匹配功能。<br>- HEADEN：头增强，代表该规则可以配置头增强策略，可以基于配置的头增强策略向HTTP/RTSP请求报文头域中插入字段。<br>- WEBPROXY：Web Proxy，代表该规则可以配置WebProxy的IPFarm对象名称，用于设置WebProxy选择的服务器地址池。<br>- IPREDIR：IP重定向，代表该规则可以配置IP重定向的目标IP地址，支持IPv4和IPv6两种类型的IP地址。<br>- SMARTREDIRECT：Captive Portal智能重定向，代表该规则可以配置Captive Portal的IPFarm对象名称，用于设置Captive Portal选择的服务器地址池。<br>- REMARK_FPI：Remark或者FPI，代表该规则可以配置IP报文的DSCP重标记值或FPI策略。<br>- SRV_TRIGGER：Service Trigger Radius，代表该规则可以配置业务触发Radius消息交互功能标识，并配置Radius交互过程中报文处理方式。<br>- TRAFFICCLASS：Traffic Classifier，代表该规则可以配置Service Chain对象名称，用于实现业务链功能。<br>- LBO：Local Break Out，代表该规则可以用于本地业务分流。<br>- FIREWALL：防火墙，代表该规则可以配置防火墙策略。<br>- ULCL：ULCL，代表该规则可以配置ULCL策略。<br>- ADC：代表该规则用于应用检测与控制功能。<br>- QOS：代表该规则可以配置QoS策略，可以基于配置的QoS策略进行业务级QoS处理。<br>- FUP：公平使用策略，代表该规则可以配置公平使用策略。<br>- NON_SPECIFIC_TYPE：不指定具体的类型。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |
| RULESPECTYPE | 规则规格类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则规格类型，当取值为SPECIFICATION_LIMITED时，表示规格受限规则，表示被用户安装的规格和被USERPROFILE绑定的规格均比默认规格小，需要配合相应特性使用。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DEFAULT：默认配置。<br>- SPECIFICATION_LIMITED：规格受限配置。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897203)

假如运营商想删除名为testrule的所有规则：

```
RMV RULE:RULENAME="testrule";
```
