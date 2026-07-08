---
id: UDG@20.15.2@MMLCommand@DSP RULECHECK
type: MMLCommand
name: DSP RULECHECK（查询规则检测结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RULECHECK
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 延迟生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- 规则检测
status: active
---

# DSP RULECHECK（查询规则检测结果）

## 功能

**适用NF：PGW-U、UPF**

该命令用于对指定规则或所有规则的IP版本一致性进行检查；查询名称相同策略类型不同的规则；当特征库升级发生了协议名称变更时，查询进行过自动配置转换的命令，或查询进行自动配置转换协议名称冲突的命令；确认接受自动配置转换结果，并消除告警。规则的IP版本一致性检查指的是规则下的过滤器或者过滤器组配置过的IP版本是否包含了策略组下配置过的IP版本；如果不包含，则算异常；包含则算正常。

## 注意事项

- 协议识别特征库支持无损升级，升级后如果出现协议名称变更，系统会自动进行配置转换，支持协议名称变更冲突导致自动转换配置失败检测，并产生ALM-81032告警。
- 新增、修改完规则配置或者特征库升级后产生的ALM-81032告警可以通过该命令清除，且立即生效。
- 在选择PROT_CHG_CONFIRM参数时，表示确认接受自动配置转换结果，可用于消除配置自动转换触发的ALM-81032告警；在执行此参数前，建议先使用PROT_CHG_CHECK参数查看自动转换结果，并确认转换结果可以接受。如果某条命令自动转换结果有问题，可以手工执行该命令修改配置。
- 在选择PROT_CONFLICT_CONFIRM参数时，表示确认自动配置转换出现冲突的情况，可用于消除配置自动转换冲突触发的ALM-81032告警。在执行此参数前，必须先使用PROT_CONFLICT_CHECK参数查看自动转换冲突检查结果，并手动进行冲突配置修改。
- 执行完DSP RULECHECK命令后，需等待5秒再执行BwmService，ProtocolDefine，ProtFAgetime，WellKnownPort，ProtBindSrvS，ProtBindFlowF，SaDedicBearer，UsrRelateIden，SignaDbRule，ProtRedefine，FingerIdent，AfHttpsCtCk对象的MOD、RMV命令，否则可能导致MOD、RMV命令不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULECHECKTYPE | 规则检测类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置规则检测类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RULE_IP_CHECK：检测规则IP版本是否冲突。<br>- PROT_CHG_CHECK：查询进行过自动配置转换的命令。<br>- PROT_CHG_CONFIRM：确认接受自动转换结果。<br>- HOMONYMY_RULE：名称相同策略类型不同的规则检测。<br>- PROT_CONFLICT_CHECK：协议名称变更与已有协议名称冲突检测。<br>- PROT_CONFLICT_CONFIRM：确认自动转换冲突。<br>默认值：无<br>配置原则：无 |
| RULENAME | 规则名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RULECHECKTYPE”配置为“RULE_IP_CHECK”时为可选参数。<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD RULE 或 ADD BLACKLISTRULE 命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RULECHECK]] · 规则检测结果（RULECHECK）

## 使用实例

- 运营商新增或者修改了规则配置时，要查询指定规则的IP版本是否冲突。指定规则检测类型为RULE_IP_CHECK：
  ```
  DSP RULECHECK:RULECHECKTYPE=RULE_IP_CHECK,RULENAME="r1";
  ```
  ```

  RETCODE = 0  Operation Success.

  Rule Check Result Information
  -----------------------------
  Rule Check Type  =  Rule IP Version Check
     Query Result  =  
  Rule Check Information
  ----------------------
                    Rule Name = r1
                  Policy Type = IPREDIR
                 Check Result = OK
                    Rule Name = r1
                  Policy Type = SMARTREDIRECT
                 Check Result = NOK
        Exception Action Name = Captive Portal Smart Redirect

  (Number of results = 1)
  ---    END
  ```
- 运营商要查询所有规则的IP版本是否冲突。指定规则检测类型为RULE_IP_CHECK，不填写规则名称：
  ```
  DSP RULECHECK:RULECHECKTYPE=RULE_IP_CHECK;
  ```
  ```

  RETCODE = 0  Operation Success.

  Rule Check Result Information
  -----------------------------
  Rule Check Type  =  Rule IP Version Check
     Query Result  =  
  Rule Check Information
  ----------------------
                    Rule Name = r1
                  Policy Type = IPREDIR
                 Check Result = OK
                    Rule Name = r2
                  Policy Type = SMARTREDIRECT
                 Check Result = OK

  (Number of results = 1)
  ---    END
  ```
- 运营商升级了特征库，要查询进行过自动配置转换的命令。指定规则检测类型为PROT_CHG_CHECK：
  ```
  DSP RULECHECK:RULECHECKTYPE=PROT_CHG_CHECK;
  ```
  ```

  RETCODE = 0  Operation Success.

  Rule Check Result Information
  -----------------------------
  Rule Check Type  =  Protocol Change Check
     Query Result  =  
  Configuration Conversion Info
  ---------------------------------
                                 Service Statistics Name = test1
                                   New Sub-Protocol Name = youku

  (Number of automatic configuration conversions for this product = 1)

  (Number of results = 1)
  ---    END
  ```
- 运营商升级了特征库，要查询确认接受自动转换结果。指定规则检测类型为PROT_CHG_CONFIRM：
  ```
  DSP RULECHECK: RULECHECKTYPE=PROT_CHG_CONFIRM;
  ```
  ```

  RETCODE = 0  Operation Success.

  Rule Check Result Information
  -----------------------------
  Rule Check Type  =  Protocol Change Confirm
     Query Result  =  Number of automatic configuration conversions changed for this product = 0!

  (Number of results = 1)
  ---    END
  ```
- 运营商要查询名称相同策略类型不同的规则，指定规则检测类型为HOMONYMY_RULE：
  ```
  DSP RULECHECK:RULECHECKTYPE=HOMONYMY_RULE;
  ```
  ```

  RETCODE = 0  Operation Success.

  Rule Check Result Information
  -----------------------------
  Rule Check Type  =  Homonymy Rule Check
     Query Result  =  
  Homonymy Rule Information
  -----------------------------
  Rule Name = r1
  Rule Type = PCC
  Rule Type = BWM
  Rule Type = IPREDIR

  Rule Name = r2
  Rule Type = PCC
  Rule Type = HEADEN
  Rule Type = IPREDIR

  (Number of results = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询规则检测结果（DSP-RULECHECK）_86526138.md`
