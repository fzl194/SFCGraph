---
id: UNC@20.15.2@MMLCommand@DSP ACLADV6RULECNT
type: MMLCommand
name: DSP ACLADV6RULECNT（显示高级IPv6 ACL规则匹配计数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ACLADV6RULECNT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- IPv6 ACL规则匹配计数
status: active
---

# DSP ACLADV6RULECNT（显示高级IPv6 ACL规则匹配计数）

## 功能

该命令用于显示高级IPv6 ACL规则的匹配计数信息。可应用于路由策略等使用场景的匹配计数信息查询。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | IPv6 ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6 ACL规则属于哪个IPv6 ACL规则组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。<br>默认值：无 |
| ACLRULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6 ACL规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ACLADV6RULECNT]] · 高级IPv6 ACL规则匹配计数（ACLADV6RULECNT）

## 使用实例

显示当前IPv6 ACL规则组3000下规则名称为"rule_5"的匹配计数：

```
DSP ACLADV6RULECNT:ACLNAME="3000",ACLRULENAME="rule_5";
```

```

RETCODE = 0  操作成功。

结果如下
--------
IPv6 ACL规则组标识  =  3000
          规则名称  =  rule_5
          匹配计数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ACLADV6RULECNT.md`
