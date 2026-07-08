---
id: UDG@20.15.2@MMLCommand@LST ACLRULEADV4
type: MMLCommand
name: LST ACLRULEADV4（查询高级ACL规则配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ACLRULEADV4
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- 高级ACL规则
status: active
---

# LST ACLRULEADV4（查询高级ACL规则配置）

## 功能

该命令用于查询当前系统中高级ACL的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则属于哪个规则组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是3000～3999。<br>默认值：无 |
| ACLRULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [高级ACL规则（ACLRULEADV4）](configobject/UDG/20.15.2/ACLRULEADV4.md)

## 使用实例

- 查询当前ACL规则组3000下所有规则的配置：
  ```
  LST ACLRULEADV4:ACLNAME="3000";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  ACL规则组标识    规则名称    规则ID    规则行为                  协议类型值    源IP地址    源IP地址反掩码     目的IP地址    目的IP地址反掩码    报文分片类型    服务优先级    源端口范围类型    源端口的开始端口号    源端口的结束端口号    目的端口范围类型    目的端口的结束端口号    目的端口的开始端口号    TCP-FLAG    网络控制管理协议类型    网络控制管理协议消息码    DSCP值    报文优先级    VPN实例名称    ICMP名称    TTL范围    TTL值    结束TTL值    规则描述

  3000             rule_5      5         指定匹配模式为允许模式    0             0.0.0.0     255.255.255.255    0.0.0.0       255.255.255.255     NULL            NULL          NULL              0                     0                     NULL                0                       0                       NULL        NULL                    NULL                      NULL      NULL          _public_       NULL        NULL       NULL     NULL         NULL
  3000             rule_10     10        指定匹配模式为允许模式    17            0.0.0.0     255.255.255.255    0.0.0.0       255.255.255.255     NULL            NULL          NULL              0                     0                     NULL                0                       0                       NULL        NULL                    NULL                      NULL      NULL          _public_       NULL        NULL       NULL     NULL         NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询当前ACL规则3000组中规则名称为"rule_5"的规则配置：
  ```
  LST ACLRULEADV4:ACLNAME="3000",ACLRULENAME="rule_5";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
           ACL规则组标识  =  3000
                规则名称  =  rule_5
                  规则ID  =  5
                规则行为  =  指定匹配模式为允许模式
              协议类型值  =  0
                源IP地址  =  0.0.0.0
          源IP地址反掩码  =  255.255.255.255
              目的IP地址  =  0.0.0.0
        目的IP地址反掩码  =  255.255.255.255
            报文分片类型  =  NULL
              服务优先级  =  NULL
          源端口范围类型  =  NULL
      源端口的开始端口号  =  0
      源端口的结束端口号  =  0
        目的端口范围类型  =  NULL
    目的端口的结束端口号  =  0
    目的端口的开始端口号  =  0
                TCP-FLAG  =  NULL
    网络控制管理协议类型  =  NULL
  网络控制管理协议消息码  =  NULL
                  DSCP值  =  NULL
              报文优先级  =  NULL
             VPN实例名称  =  _public_
                ICMP名称  =  NULL
                 TTL范围  =  NULL
                   TTL值  =  NULL
               结束TTL值  =  NULL
                规则描述  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询高级ACL规则配置（LST-ACLRULEADV4）_50280814.md`
