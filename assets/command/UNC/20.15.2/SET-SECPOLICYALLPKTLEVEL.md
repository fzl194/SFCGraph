---
id: UNC@20.15.2@MMLCommand@SET SECPOLICYALLPKTLEVEL
type: MMLCommand
name: SET SECPOLICYALLPKTLEVEL（设置上送报文总体速率等级）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SECPOLICYALLPKTLEVEL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略总报文
status: active
---

# SET SECPOLICYALLPKTLEVEL（设置上送报文总体速率等级）

## 功能

该命令用来添加上送报文总体速率等级设置。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| SECRATELEVEL |
| --- |
| high |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：需要先添加安全策略，下发本MML命令前可使用LST SECPOLICY查看已添加的安全策略。 |
| SECRATELEVEL | 上报速率等级 | 可选必选说明：必选参数<br>参数含义：上报速率标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- low：3000pps。<br>- middle：4500pps。<br>- high：6000pps。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECPOLICYALLPKTLEVEL]] · 上送报文总体速率等级（SECPOLICYALLPKTLEVEL）

## 使用实例

添加上送报文总体速率等级设置：

```
SET SECPOLICYALLPKTLEVEL:SECPOLICYID=1, SECRATELEVEL=middle;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SECPOLICYALLPKTLEVEL.md`
