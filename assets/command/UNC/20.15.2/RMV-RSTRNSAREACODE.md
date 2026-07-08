---
id: UNC@20.15.2@MMLCommand@RMV RSTRNSAREACODE
type: MMLCommand
name: RMV RSTRNSAREACODE（删除TA级切片限制区域码）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RSTRNSAREACODE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片选择管理
- TA级限制切片区域管理
status: active
---

# RMV RSTRNSAREACODE（删除TA级切片限制区域码）

## 功能

**适用NF：AMF**

该命令用于删除TA级切片限制区域码。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREACODE | 区域编码 | 可选必选说明：必选参数<br>参数含义：该参数用于唯一标识AMF服务的某个区域，该区域由一个或者若干个跟踪区组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RSTRNSAREACODE]] · TA级切片限制区域码（RSTRNSAREACODE）

## 使用实例

删除编码为“jq001.pd006.sh.mcc123.mnc45”的TA级限制切片所属区域编码，执行如下命令：

```
RMV RSTRNSAREACODE:AREACODE="jq001.pd006.sh.mcc123.mnc45";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RSTRNSAREACODE.md`
