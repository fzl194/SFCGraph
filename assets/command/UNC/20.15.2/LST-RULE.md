---
id: UNC@20.15.2@MMLCommand@LST RULE
type: MMLCommand
name: LST RULE（查询规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RULE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 规则
status: active
---

# LST RULE（查询规则）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询规则。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：设置该参数时表示查询指定名称的规则，未设置该参数时表示查询系统中所有的规则。 |
| POLICYTYPE | 策略类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置策略类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- PCC：计费与策略控制，代表该规则可以配置PCC策略，用于实现计费和策略控制功能。<br>- BWM：带宽管理，代表该规则可以配置带宽管理分类策略，其分类结果可以用于带宽管理的策略匹配功能。<br>- HEADEN：头增强，代表该规则可以配置头增强策略，可以基于配置的头增强策略向HTTP/RTSP请求报文头域中插入字段。<br>- WEBPROXY：Web Proxy，代表该规则可以配置WebProxy的IPFarm对象名称，用于设置WebProxy选择的服务器地址池。<br>- IPREDIR：IP重定向，代表该规则可以配置IP重定向的目标IP地址，支持IPv4和IPv6两种类型的IP地址。<br>- SMARTREDIRECT：Captive Portal智能重定向，代表该规则可以配置Captive Portal的IPFarm对象名称，用于设置Captive Portal选择的服务器地址池。<br>- REMARK_FPI：Remark或者FPI，代表该规则可以配置IP报文的DSCP重标记值或FPI策略。<br>- SRV_TRIGGER：Service Trigger Radius，代表该规则可以配置业务触发Radius消息交互功能标识，并配置Radius交互过程中报文处理方式。<br>- TRAFFICCLASS：Traffic Classifier，代表该规则可以配置Service Chain对象名称，用于实现业务链功能。<br>- LBO：Local Break Out，代表该规则可以用于本地业务分流。<br>- FIREWALL：防火墙，代表该规则可以配置防火墙策略。<br>- ULCL：ULCL，代表该规则可以配置ULCL策略。<br>- ADC：代表该规则用于应用检测与控制功能。<br>- QOS：代表该规则可以配置QoS策略，可以基于配置的QoS策略进行业务级QoS处理。<br>- FUP：公平使用策略，代表该规则可以配置公平使用策略。<br>- NON_SPECIFIC_TYPE：不指定具体的类型。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |
| RULESPECTYPE | 规则规格类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则规格类型，当取值为SPECIFICATION_LIMITED时，表示规格受限规则，表示被用户安装的规格和被USERPROFILE绑定的规格均比默认规格小，需要配合相应特性使用。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DEFAULT：默认配置。<br>- SPECIFICATION_LIMITED：规格受限配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RULE]] · 规则（RULE）

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
    全局优先级  =  50
      策略类型  =  PCC
      策略名称  =  testpccpolicygrpnm
  流过滤器名称  =  NULL
  规则生效范围  =  对中心和边缘UPF均生效
  规则规格类型  =  默认配置
  NWDAF数据分析事件  =  NULL
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
  规则名称  全局优先级  策略类型  策略名称            流过滤器名称  规则生效范围           规则规格类型      NWDAF数据分析事件

  rule1     4294967295  PCC       testpccpolicygrpnm  NULL          对中心和边缘UPF均生效  默认配置    NULL
  testrule  50          PCC       testpccpolicygrpnm  NULL          对中心和边缘UPF均生效  默认配置    NULL
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RULE.md`
