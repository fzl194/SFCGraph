---
id: UNC@20.15.2@MMLCommand@DSP ACLRULEETH
type: MMLCommand
name: DSP ACLRULEETH（显示以太ACL规则）
nf: UNC
version: 20.15.2
verb: DSP
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

# DSP ACLRULEETH（显示以太ACL规则）

## 功能

该命令用于显示当前系统中以太ACL规则的状态，也可以显示规则组下所有规则状态。

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

- [[configobject/UNC/20.15.2/ACLRULEETH]] · 以太ACL规则（ACLRULEETH）

## 使用实例

- 显示当前ACL规则组4000下所有规则的状态：
  ```
  DSP ACLRULEETH: ACLNAME="4000";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  ACL规则组标识    规则名称    规则ID    规则行为                  以太帧头协议号    以太帧头协议掩码    源MAC地址         源MAC地址掩码     目的MAC地址       目的MAC地址掩码    VLAN ID    VLAN ID的掩码    激活状态    规则描述

  4000             rule_5      5         指定匹配模式为允许模式    0x800             0xFFFF              0000-0000-0000    0000-0000-0000    0000-0000-0000    0000-0000-0000     NULL       NULL             激活        NULL
  4000             rule_10     10        指定匹配模式为允许模式    NULL              NULL                0000-0000-0000    0000-0000-0000    0000-0000-0000    0000-0000-0000     NULL       NULL             激活        NULL
  (结果个数 = 2)
  ---    END
  ```
- 显示当前ACL规则组4000中规则名称为"rule_5"的规则状态：
  ```
  DSP ACLRULEETH: ACLNAME="4000",ACLRULENAME="rule_5";
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
          激活状态  =  激活
          规则描述  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ACLRULEETH.md`
