---
id: UDG@20.15.2@MMLCommand@MOD IPSAGING
type: MMLCommand
name: MOD IPSAGING（修改IPS老化配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: IPSAGING
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IP管理
- IP维护
status: active
---

# MOD IPSAGING（修改IPS老化配置）

## 功能

该命令用于修改IPS老化配置。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENABLEAGING | 开启老化功能 | 可选必选说明：必选参数<br>参数含义：该参数用于开启老化功能。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>Boolean。 |
| AGINGTHRESHOLD | 老化阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设定老化轮次阈值，达到阈值数量同步轮次未接收到更新或同步的数据将会被老化。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255，单位是次。<br>默认值：5<br>配置原则：无 |
| SYNCBATCHSIZE | 同步打包包数 | 可选必选说明：可选参数<br>参数含义：该参数用于设定数据同步消息打包包数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10，单位是条。<br>默认值：10<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPSAGING]] · IPS老化配置（IPSAGING）

## 使用实例

- 开启IPS老化功能，老化阈值为5。
  ```
  MOD IPSAGING: ENABLEAGING=TRUE, AGINGTHRESHOLD=5;
  ```
- 设置同步打包包数为5。
  ```
  MOD IPSAGING: ENABLEAGING=FALSE, SYNCBATCHSIZE=5;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-IPSAGING.md`
