---
id: UNC@20.15.2@MMLCommand@ADD SECPOLICYPROSEQ
type: MMLCommand
name: ADD SECPOLICYPROSEQ（增加安全策略匹配顺序）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SECPOLICYPROSEQ
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 30
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略匹配顺序
status: active
---

# ADD SECPOLICYPROSEQ（增加安全策略匹配顺序）

## 功能

该命令用来增加安全策略匹配顺序。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为30。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：安全策略号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：需要先添加安全策略，下发本MML命令前可使用LST SECPOLICY查看已添加的安全策略。 |
| SECPROSEQWL | 安全白名单匹配顺序 | 可选必选说明：必选参数<br>参数含义：安全白名单匹配顺序。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- First：匹配优先级高。<br>- Second：匹配优先级中。<br>- Third：匹配优先级低。<br>默认值：无<br>配置原则：SECPROSEQWL/SECPROSEQBL/SECPROSEQUF三个参数值不能相同。 |
| SECPROSEQBL | 安全黑名单匹配顺序 | 可选必选说明：必选参数<br>参数含义：安全黑名单匹配顺序。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- First：匹配优先级高。<br>- Second：匹配优先级中。<br>- Third：匹配优先级低。<br>默认值：无<br>配置原则：SECPROSEQWL/SECPROSEQBL/SECPROSEQUF三个参数值不能相同。 |
| SECPROSEQUF | 安全用户流匹配顺序 | 可选必选说明：必选参数<br>参数含义：安全用户自定义流。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- First：匹配优先级高。<br>- Second：匹配优先级中。<br>- Third：匹配优先级低。<br>默认值：无<br>配置原则：SECPROSEQWL/SECPROSEQBL/SECPROSEQUF三个参数值不能相同。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECPOLICYPROSEQ]] · 安全策略匹配顺序（SECPOLICYPROSEQ）

## 使用实例

增加安全策略匹配顺序：

```
ADD SECPOLICYPROSEQ:SECPOLICYID=1,SECPROSEQWL=Third,SECPROSEQBL=Second,SECPROSEQUF=First;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SECPOLICYPROSEQ.md`
