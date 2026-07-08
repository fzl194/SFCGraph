---
id: UDG@20.15.2@MMLCommand@RMV BWMRULEGLOBAL
type: MMLCommand
name: RMV BWMRULEGLOBAL（删除全局带宽管理规则）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: BWMRULEGLOBAL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理规则
status: active
---

# RMV BWMRULEGLOBAL（删除全局带宽管理规则）

## 功能

**适用NF：PGW-U、UPF**

![](删除全局带宽管理规则（RMV BWMRULEGLOBAL）_82837484.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除BwmRuleGlobal会影响用户业务访问，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除全局业务带宽管理规则。当运营商希望删除全局的某个或全部带宽控制规则时，则执行该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BWMRULENAME | 带宽管理规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置带宽管理规则的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BWMRULEGLOBAL]] · 全局带宽管理规则（BWMRULEGLOBAL）

## 使用实例

假如运营商需要删除名为“testbwmruleglobal”的全局带宽管理规则：

```
RMV BWMRULEGLOBAL:BWMRULENAME="testbwmruleglobal";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-BWMRULEGLOBAL.md`
