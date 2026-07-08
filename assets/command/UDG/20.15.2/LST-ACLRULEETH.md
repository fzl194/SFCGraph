---
id: UDG@20.15.2@MMLCommand@LST ACLRULEETH
type: MMLCommand
name: LST ACLRULEETH（查询以太ACL规则配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ACLRULEETH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- 以太ACL规则
status: active
---

# LST ACLRULEETH（查询以太ACL规则配置）

## 功能

该命令用于查询当前系统中以太ACL的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则属于哪个规则组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是4000～4999。<br>默认值：无 |
| ACLRULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。<br>默认值：无 |

## 操作的配置对象

- [以太ACL规则（ACLRULEETH）](configobject/UDG/20.15.2/ACLRULEETH.md)

## 使用实例

- 查询当前ACL规则组4000下所有规则的配置：
  ```
  LST ACLRULEETH: ACLNAME="4000";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  ACL规则组标识    规则名称    规则ID    规则行为                  以太帧头协议号    以太帧头协议掩码    源MAC地址         源MAC地址掩码     目的MAC地址       目的MAC地址掩码    VLAN ID    VLAN ID的掩码    规则描述

  4000             rule_5      5         指定匹配模式为允许模式    0x800             0xFFFF              0000-0000-0000    0000-0000-0000    0000-0000-0000    0000-0000-0000     NULL       NULL             NULL
  4000             rule_10     10        指定匹配模式为允许模式    NULL              NULL                0000-0000-0000    0000-0000-0000    0000-0000-0000    0000-0000-0000     NULL       NULL             NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询当前ACL规则4000组中规则名称为"rule_5"的规则配置：
  ```
  LST ACLRULEETH: ACLNAME="4000",ACLRULENAME="rule_5";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
     ACL规则组标识  =  4000
          规则名称  =  rule_5
            规则ID  =  5
          规则行为  =  指定匹配模式为允许模式
    以太帧头协议号  =  0x800
  以太帧头协议掩码  =  0xFFFF
         源MAC地址  =  00E0-FC12-3456
     源MAC地址掩码  =  FFFF-FFFF-FFFF
       目的MAC地址  =  00E0-FC12-3457
   目的MAC地址掩码  =  FFFF-FFFF-FFFF
           VLAN ID  =  NULL
     VLAN ID的掩码  =  NULL
          规则描述  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询以太ACL规则配置（LST-ACLRULEETH）_50280946.md`
