---
id: UNC@20.15.2@MMLCommand@LST MPACIPV6RULE
type: MMLCommand
name: LST MPACIPV6RULE（查询IPv6 MPAC策略规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MPACIPV6RULE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- IPv6策略规则
status: active
---

# LST MPACIPV6RULE（查询IPv6 MPAC策略规则）

## 功能

该命令用于查询MPAC策略规则。

不指定参数时，查询所有策略规则信息；当指定参数时，可以查询指定策略或者指定规则信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定创建规则的策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |
| RULENAME | 规则名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPACIPV6RULE]] · IPv6 MPAC策略规则（MPACIPV6RULE）

## 使用实例

查询MPAC策略规则：

```
LST MPACIPV6RULE:POLICYNAME="policyV6";
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
                策略名称  =  policyV6
                规则名字  =  name1
                  规则ID  =  19
                规则动作  =  允许
                协议方式  =  IP协议号
                协议名称  =  UDP协议报文
              IPv6协议号  =  17
                  源地址  =  2001:db8:2000:8999:1987:6787:2341:9876
          源地址前缀长度  =  1
                目的地址  =  2001:db8:1234::8
        目的地址前缀长度  =  64
                源端口号  =  0
              目的端口号  =  0
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPv6-MPAC策略规则（LST-MPACIPV6RULE）_00866397.md`
