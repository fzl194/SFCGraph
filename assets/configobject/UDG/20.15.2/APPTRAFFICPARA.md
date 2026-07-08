---
id: UDG@20.15.2@ConfigObject@APPTRAFFICPARA
type: ConfigObject
name: APPTRAFFICPARA（应用流量参数）
nf: UDG
version: 20.15.2
object_name: APPTRAFFICPARA
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# APPTRAFFICPARA（应用流量参数）

## 说明

**适用NF：PGW-U、UPF**

![](设置应用流量参数（SET APPTRAFFICPARA）_49101653.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，1、修改TrafficRuleSw为Disable会导致当前动态流量规则或者DNS衍生规则失效； 2、修改RuleSource为DYNAMIC_TRAFFIC_RULE会导致当前DNS衍生规则失效，动态流量规则开始生效； 3、修改RuleSource为DNS_RULE_EXTENDED会导致当前动态流量规则失效，DNS衍生规则开始生效；

该命令用于动态分流规则匹配时设置应用流量参数。

## 操作本对象的命令

- [LST APPTRAFFICPARA](command/UDG/20.15.2/LST-APPTRAFFICPARA.md)
- [SET APPTRAFFICPARA](command/UDG/20.15.2/SET-APPTRAFFICPARA.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示应用流量参数（LST-APPTRAFFICPARA）_49101654.md`
- 原始手册：`evidence/UDG/20.15.2/设置应用流量参数（SET-APPTRAFFICPARA）_49101653.md`
