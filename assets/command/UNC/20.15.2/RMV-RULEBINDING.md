---
id: UNC@20.15.2@MMLCommand@RMV RULEBINDING
type: MMLCommand
name: RMV RULEBINDING（删除用户模板和规则的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RULEBINDING
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 规则绑定
status: active
---

# RMV RULEBINDING（删除用户模板和规则的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

![](删除用户模板和规则的绑定关系（RMV RULEBINDING）_09897217.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果不输入规则名称，表示删除该用户模板名称对应的用户模板下所有的规则与用户模板绑定关系。删除后使用该模板的用户可能会因为无法命中规则导致业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于删除用户模板与规则的绑定关系。当运营商希望删除用户模板与规则的绑定关系时，则配置该命令。如果不输入规则名称，表示删除该用户模板名称对应的用户模板下所有的规则与用户模板绑定关系。

## 注意事项

该命令执行后立即生效。

- 如果不输入规则名称，表示删除该用户模板名称对应的用户模板下所有的规则与用户模板绑定关系。

- 删除RuleBinding可能会改变业务匹配结果，影响策略获取，导致用户业务受损，请谨慎使用并联系华为支持协助操作。

- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| POLICYTYPE | 策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PCC：计费与策略控制，代表该规则可以配置PCC策略，用于实现计费和策略控制功能。<br>- BWM：带宽管理，代表该规则可以配置带宽管理分类策略，其分类结果可以用于带宽管理的策略匹配功能。<br>- HEADEN：头增强，代表该规则可以配置头增强策略，可以基于配置的头增强策略向HTTP/RTSP请求报文头域中插入字段。<br>- WEBPROXY：Web Proxy，代表该规则可以配置WebProxy的IPFarm对象名称，用于设置WebProxy选择的服务器地址池。<br>- IPREDIR：IP重定向，代表该规则可以配置IP重定向的目标IP地址，支持IPv4和IPv6两种类型的IP地址。<br>- SMARTREDIRECT：Captive Portal智能重定向，代表该规则可以配置Captive Portal的IPFarm对象名称，用于设置Captive Portal选择的服务器地址池。<br>- REMARK_FPI：Remark或者FPI，代表该规则可以配置IP报文的DSCP重标记值或FPI策略。<br>- SRV_TRIGGER：Service Trigger Radius，代表该规则可以配置业务触发Radius消息交互功能标识，并配置Radius交互过程中报文处理方式。<br>- TRAFFICCLASS：Traffic Classifier，代表该规则可以配置Service Chain对象名称，用于实现业务链功能。<br>- LBO：Local Break Out，代表该规则可以用于本地业务分流。<br>- FIREWALL：防火墙，代表该规则可以配置防火墙策略。<br>- ULCL：ULCL，代表该规则可以配置ULCL策略。<br>- ADC：代表该规则用于应用检测与控制功能。<br>- QOS：代表该规则可以配置QoS策略，可以基于配置的QoS策略进行业务级QoS处理。<br>- FUP：公平使用策略，代表该规则可以配置公平使用策略。<br>- NON_SPECIFIC_TYPE：不指定具体的类型。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |

## 操作的配置对象

- [用户模板和规则的绑定关系（RULEBINDING）](configobject/UNC/20.15.2/RULEBINDING.md)

## 使用实例

假如运营商需要删除名称为用户模板名称为userprofile和规则的绑定关系：

```
RMV RULEBINDING: USERPROFILENAME="userprofile";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户模板和规则的绑定关系（RMV-RULEBINDING）_09897217.md`
