---
id: UDG@20.15.2@MMLCommand@LST ACLRULEADV4IPSEC
type: MMLCommand
name: LST ACLRULEADV4IPSEC（查询高级ACL规则配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ACLRULEADV4IPSEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- ACL管理
- 高级ACL规则
status: active
---

# LST ACLRULEADV4IPSEC（查询高级ACL规则配置）

## 功能

该命令用于查询当前系统中高级ACL的配置信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则属于哪个规则组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是3000～3999。<br>默认值：无<br>配置原则：无 |
| ACLRULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACLRULEADV4IPSEC]] · 高级ACL规则（ACLRULEADV4IPSEC）

## 使用实例

查询当前ACL规则3000组中规则名称为"rule_6"的规则配置：

```
LST ACLRULEADV4IPSEC:ACLNAME="3000",ACLRULENAME="rule_6";
RETCODE = 0  操作成功。

结果如下
--------
         ACL规则组标识  =  3000
              规则名称  =  rule_6
                规则ID  =  5
              规则行为  =  指定匹配模式为允许模式
            协议类型值  =  0
              源IP地址  =  10.1.1.1
        源IP地址反掩码  =  0.0.0.0
            目的IP地址  =  10.1.1.2
      目的IP地址反掩码  =  0.0.0.0
          报文分片类型  =  NULL
            服务优先级  =  0
        源端口范围类型  =  Unconfiged
    源端口的开始端口号  =  0
    源端口的结束端口号  =  0
      目的端口范围类型  =  Unconfiged
  目的端口的结束端口号  =  0
  目的端口的开始端口号  =  0
              TCP-FLAG  =  NULL
  网络控制管理协议类型  =  0
网络控制管理协议消息码  =  0
                DSCP值  =  0
            报文优先级  =  NULL
           VPN实例名称  =  NULL
              ICMP名称  =  Unconfiged
               规则描述  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询高级ACL规则配置（LST-ACLRULEADV4IPSEC）_80592502.md`
