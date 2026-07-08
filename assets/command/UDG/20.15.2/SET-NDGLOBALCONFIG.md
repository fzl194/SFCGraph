---
id: UDG@20.15.2@MMLCommand@SET NDGLOBALCONFIG
type: MMLCommand
name: SET NDGLOBALCONFIG（设置IPv6 ND系统配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NDGLOBALCONFIG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND全局配置
status: active
---

# SET NDGLOBALCONFIG（设置IPv6 ND系统配置）

## 功能

该命令用于设置IPv6 ND全局配置。

## 注意事项

- 该命令执行后立即生效。
- 可选参数至少下发一个。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| PREDETECTFLAG | AUTODETECTFLAG | SYSHOPLIMIT | RSACALCRATELMT | SYSSTALETIME |
| --- | --- | --- | --- | --- |
| FALSE | TRUE | 64 | 0 | 1200 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PREDETECTFLAG | 使能预探测 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使能提前探测ND表项功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TRUE：开启状态。<br>- FALSE：关闭状态。<br>默认值：无 |
| AUTODETECTFLAG | 使能自动探测 | 可选必选说明：可选参数<br>参数含义：该参数用于指定使能自动探测。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TRUE：开启状态。<br>- FALSE：关闭状态。<br>默认值：无 |
| SYSHOPLIMIT | 跳限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跳限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无 |
| RSACALCRATELMT | 速率限制 | 可选必选说明：可选参数<br>参数含义：该参数用于指定速率限制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。0表示去使能该配置。<br>默认值：无 |
| SYSSTALETIME | 失效时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用来配置邻居表项在STALE状态的老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～172800，单位是秒。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NDGLOBALCONFIG]] · IPv6 ND系统配置（NDGLOBALCONFIG）

## 使用实例

设置IPv6 ND全局配置：使能提前探测ND表项功能：

```
SET NDGLOBALCONFIG:PREDETECTFLAG=TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置IPv6-ND系统配置（SET-NDGLOBALCONFIG）_00601205.md`
