---
id: UNC@20.15.2@MMLCommand@LST SECPOLICY
type: MMLCommand
name: LST SECPOLICY（查询防攻击策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SECPOLICY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略
status: active
---

# LST SECPOLICY（查询防攻击策略）

## 功能

该命令用于查询安全策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYID | 安全策略编号 | 可选必选说明：可选参数<br>参数含义：策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| DESCRIPTION | 策略描述 | 可选必选说明：可选参数<br>参数含义：防攻击策略描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECPOLICY]] · 防攻击策略（SECPOLICY）

## 使用实例

- 查询安全策略：
  ```
  LST SECPOLICY:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
  安全策略编号    策略描述

  1               NULL
  2               NULL
  (结果个数 = 2)
  ---    END
  ```
- 查询指定条件的安全策略：
  ```
  LST SECPOLICY:POLICYID=1;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
  安全策略编号  =  1
      策略描述  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SECPOLICY.md`
