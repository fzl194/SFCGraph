---
id: UDG@20.15.2@MMLCommand@DSP MPACV4RULESTAT
type: MMLCommand
name: DSP MPACV4RULESTAT（查询IPv4 MPAC策略匹配统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MPACV4RULESTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- IPv4规则匹配统计
status: active
---

# DSP MPACV4RULESTAT（查询IPv4 MPAC策略匹配统计）

## 功能

该命令用于显示当前规则的匹配统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| RULENAME | 规则名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MPACV4RULESTAT]] · IPv4 MPAC策略匹配统计（MPACV4RULESTAT）

## 使用实例

显示当前规则的匹配统计信息：

```
DSP MPACV4RULESTAT:POLICYNAME="policyV4",RULENAME="name-test";
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
        策略名称  =  policyV4
        规则名字  =  name-test
        匹配计数  =  0
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPv4-MPAC策略匹配统计（DSP-MPACV4RULESTAT）_00866469.md`
