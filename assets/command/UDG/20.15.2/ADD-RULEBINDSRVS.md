---
id: UDG@20.15.2@MMLCommand@ADD RULEBINDSRVS
type: MMLCommand
name: ADD RULEBINDSRVS（增加业务统计规则绑定配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RULEBINDSRVS
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新流生效
is_dangerous: true
max_records: 1600
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务统计实例对象绑定规则
status: active
---

# ADD RULEBINDSRVS（增加业务统计规则绑定配置）

## 功能

**适用NF：PGW-U、UPF**

![](增加业务统计规则绑定配置（ADD RULEBINDSRVS）_82837851.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于将Rule绑定到ServiceStat实例下，添加基于业务的性能统计组合中的Rule对象，添加Rule过滤规则。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1600。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVSTATNAME | 业务统计名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务统计配置的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定被绑定的Rule的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD RULE命令配置生成。 |
| POLICYTYPE | 策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PCC：计费与策略控制，代表该规则可以配置PCC策略，用于实现计费和策略控制功能。<br>- BWM：带宽管理，代表该规则可以配置带宽管理分类策略，其分类结果可以用于带宽管理的策略匹配功能。<br>- HEADEN：头增强，代表该规则可以配置头增强策略，可以基于配置的头增强策略向HTTP/RTSP请求报文头域中插入字段。<br>- WEBPROXY：Web Proxy，代表该规则可以配置WebProxy的IPFarm对象名称，用于设置WebProxy选择的服务器地址池。<br>- IPREDIR：IP重定向，代表该规则可以配置IP重定向的目标IP地址，支持IPv4和IPv6两种类型的IP地址。<br>- SMARTREDIRECT：智能重定向，代表该规则可以配置CaptivePortal业务对应的IPFarm的名称，HTTP智能重定向的名称，DNS重写动作的名称或者重定向的名称。<br>- REMARK_FPI：Remark或者FPI，代表该规则可以配置IP报文的DSCP重标记值或FPI策略。<br>- SRV_TRIGGER：Service Trigger Radius，代表该规则可以配置业务触发Radius消息交互功能标识，并配置Radius交互过程中报文处理方式。<br>- TRAFFICCLASS：Traffic Classifier，代表该规则可以配置Service Chain对象名称，用于实现业务链功能，此参数当前不支持。<br>- LBO：Local Break Out，代表该规则可以用于本地业务分流，此参数当前不支持。<br>- FIREWALL：防火墙，代表该规则可以配置防火墙策略。<br>- ADC：代表该规则用于应用检测与控制功能。<br>- QOS：代表该规则可以配置QoS策略，可以基于配置的QoS策略进行业务级QoS处理。<br>- WORKER：代表该规则用于通用Rule业务。<br>默认值：无<br>配置原则：<br>- 如果本处不指定策略类型，则将相同规则名称、不同策略类型的规则都绑定到业务实例下。<br>- 可以通过指定策略类型来区分相同规则名称的不同规则。<br>- 如果指定策略类型，则该策略类型需要与ADD RULE命令配置生成的相同规则名称的规则对应的策略类型一致。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RULEBINDSRVS]] · 业务统计规则绑定配置（RULEBINDSRVS）

## 使用实例

假如运营商希望配置基于业务的性能统计组合，统计规则“rule1”下的业务的数据包的请求次数、响应次数和响应时延：

```
ADD RULEBINDSRVS:SRVSTATNAME="stat1",RULENAME="rule1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-RULEBINDSRVS.md`
