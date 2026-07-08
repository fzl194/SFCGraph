---
id: UNC@20.15.2@MMLCommand@LST ACLRULEBAS6
type: MMLCommand
name: LST ACLRULEBAS6（查询基本IPv6 ACL规则配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ACLRULEBAS6
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- 基本IPv6 ACL规则
status: active
---

# LST ACLRULEBAS6（查询基本IPv6 ACL规则配置）

## 功能

该命令用于查询当前系统中基本IPv6 ACL的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | IPv6 ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPv6 ACL规则属于哪个规则组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是2000～2999。<br>默认值：无 |
| ACLRULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACLRULEBAS6]] · 基本IPv6 ACL规则（ACLRULEBAS6）

## 使用实例

- 查询当前IPv6 ACL规则2000下所有规则的配置：
  ```
  LST ACLRULEBAS6: ACLNAME="2000";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  IPv6 ACL规则组标识    规则名称    规则ID    规则行为                  报文分片类型    VPN实例名称    源IPv6地址    源IPv6地址正掩码长度    规则描述

  2000                  rule_5      5         指定匹配模式为允许模式    NULL            _public_       2001:DB8::    23                      NULL
  2000                  rule_10     10        指定匹配模式为允许模式    NULL            _public_       2001:DB8::    24                      NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询当前IPv6 ACL规则2000中规则名称为"rule_5"的规则配置：
  ```
  LST ACLRULEBAS6: ACLNAME="2000",ACLRULENAME="rule_5";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
    IPv6 ACL规则组标识  =  2000
              规则名称  =  rule_5
                规则ID  =  5
              规则行为  =  指定匹配模式为允许模式
          报文分片类型  =  NULL
           VPN实例名称  =  _public_
            源IPv6地址  =  2001:DB8::
  源IPv6地址正掩码长度  =  23
              规则描述  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ACLRULEBAS6.md`
