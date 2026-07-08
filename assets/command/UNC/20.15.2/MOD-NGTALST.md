---
id: UNC@20.15.2@MMLCommand@MOD NGTALST
type: MMLCommand
name: MOD NGTALST（修改5G跟踪区列表）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGTALST
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 跟踪区管理
- 跟踪区列表管理
status: active
---

# MOD NGTALST（修改5G跟踪区列表）

## 功能

**适用NF：AMF**

该命令用来修改跟踪区列表配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTID | 跟踪区列表标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个跟踪区列表，一个跟踪区列表由一个或若干个跟踪区组成。一个跟踪区列表最多可包含16个跟踪区。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65534。<br>默认值：无<br>配置原则：无 |
| TAI | 跟踪区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于在全网中唯一标识一个跟踪区。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。TAI由MCC、MNC和TAC组成。MCC为3位十进制数字，MNC为2个或者3位十进制数字，填写时请遵循实际长度。TAC编码为16进制数，固定为6位。若不足则左起用0补足6位。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数是对跟踪区列表的描述信息，在运维中起助记作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGTALST]] · 5G跟踪区列表（NGTALST）

## 使用实例

将包含跟踪区46001000101的跟踪列表1的描述改为“AREA3”，执行如下命令：

```
MOD NGTALST: TALISTID=1, TAI="46001000101", DESC="AREA3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NGTALST.md`
