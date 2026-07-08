---
id: UDG@20.15.2@MMLCommand@LST SECPOLICYACL
type: MMLCommand
name: LST SECPOLICYACL（查询安全策略ACL规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SECPOLICYACL
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略ACL
status: active
---

# LST SECPOLICYACL（查询安全策略ACL规则）

## 功能

该命令用来查询一个安全策略规则。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：可选参数<br>参数含义：安全策略号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- WhiteList：白名单。<br>- BlackList：黑名单。<br>- UserFlow：用户自定义流。<br>- IPV6WhiteList：IPv6白名单。<br>- IPV6BlackList：IPv6黑名单。<br>- IPV6UserFlow：IPv6用户自定义流。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：可选参数<br>参数含义：安全策略类型编号，对应不同策略类型其含义不同，如SECPOLICYTYPE为User Flow，则此值为1－32的数值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SECACLNUM | 安全ACL规则编号 | 可选必选说明：可选参数<br>参数含义：安全规则号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2000～3999。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SECPOLICYACL]] · 安全策略ACL规则（SECPOLICYACL）

## 使用实例

- 查询安全策略规则：
  ```
  LST SECPOLICYACL:SECPOLICYID=1,SECPOLICYTYPE=WhiteList;
  ```
  ```
  RETCODE = 0  操作成功

  显示安全ACL策略信息:
  -------------------------
      安全策略类型   =  白名单
   安全ACL规则编号   =  2001
      安全策略编号   =  1
  (结果个数 = 1)
  ---    END
  ```
- 查询指定条件的安全策略规则：
  ```
  LST SECPOLICYACL:SECPOLICYID=1,SECPOLICYTYPE=UserFlow,SECPOLICYTYPEID=2;
  ```
  ```
  RETCODE = 0  操作成功

  显示安全ACL策略信息:
  -------------------------
       安全策略类型  =  用户自定义流
   安全策略类型编号  =  2
    安全ACL规则编号  =  2000
       安全策略编号  =  1
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询安全策略ACL规则（LST-SECPOLICYACL）_00441405.md`
