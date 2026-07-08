---
id: UDG@20.15.2@MMLCommand@LST MPACIPV4RULE
type: MMLCommand
name: LST MPACIPV4RULE（查询IPv4 MPAC策略规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MPACIPV4RULE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- IPv4策略规则
status: active
---

# LST MPACIPV4RULE（查询IPv4 MPAC策略规则）

## 功能

该命令用于查询MPAC策略规则。

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

- [[configobject/UDG/20.15.2/MPACIPV4RULE]] · IPv4 MPAC策略规则（MPACIPV4RULE）

## 使用实例

查询MPAC策略规则：

```
LST MPACIPV4RULE:POLICYNAME="policyV4",RULENAME="name-test";
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
                策略名称  =  policyV4
                规则名字  =  name-test
                  规则ID  =  5
                规则动作  =  拒绝
                协议方式  =  IP协议号
                协议名称  =  TCP协议报文
                IP协议号  =  6
                  源地址  =  10.1.1.0
        IPv4源地址反掩码  =  0.0.0.255
                目的地址  =  10.2.2.0
      IPv4目的地址反掩码  =  0.0.0.255
                源端口号  =  0
              目的端口号  =  0
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPv4-MPAC策略规则（LST-MPACIPV4RULE）_50280742.md`
