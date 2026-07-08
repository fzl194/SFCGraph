---
id: UNC@20.15.2@MMLCommand@LST SECPOLICYPROSEQ
type: MMLCommand
name: LST SECPOLICYPROSEQ（查询安全策略匹配顺序）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SECPOLICYPROSEQ
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略匹配顺序
status: active
---

# LST SECPOLICYPROSEQ（查询安全策略匹配顺序）

## 功能

该命令用来查询安全策略匹配顺序。

## 注意事项

该命令执行后立即生效。

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：可选参数<br>参数含义：安全策略号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPROSEQWL | 安全白名单匹配顺序 | 可选必选说明：可选参数<br>参数含义：安全白名单匹配顺序。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- First：匹配优先级高。<br>- Second：匹配优先级中。<br>- Third：匹配优先级低。<br>默认值：无 |
| SECPROSEQBL | 安全黑名单匹配顺序 | 可选必选说明：可选参数<br>参数含义：安全黑名单匹配顺序。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- First：匹配优先级高。<br>- Second：匹配优先级中。<br>- Third：匹配优先级低。<br>默认值：无 |
| SECPROSEQUF | 安全用户流匹配顺序 | 可选必选说明：可选参数<br>参数含义：安全用户自定义流。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- First：匹配优先级高。<br>- Second：匹配优先级中。<br>- Third：匹配优先级低。<br>默认值：无 |

## 操作的配置对象

- [安全策略匹配顺序（SECPOLICYPROSEQ）](configobject/UNC/20.15.2/SECPOLICYPROSEQ.md)

## 使用实例

- 查询安全策略匹配顺序：
  ```
  LST SECPOLICYPROSEQ:SECPOLICYID=1;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
        安全策略编号  =  1
  安全白名单匹配顺序  =  三
  安全黑名单匹配顺序  =  二
  安全用户流匹配顺序  =  一
  (结果个数 = 1)
  ---    END
  ```
- 查询指定条件的安全策略匹配顺序：
  ```
  LST SECPOLICYPROSEQ:SECPOLICYID=1,SECPROSEQWL=Third,SECPROSEQBL=Second,SECPROSEQUF=First;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
        安全策略编号  =  1
  安全白名单匹配顺序  =  三
  安全黑名单匹配顺序  =  二
  安全用户流匹配顺序  =  一
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询安全策略匹配顺序（LST-SECPOLICYPROSEQ）_49802150.md`
