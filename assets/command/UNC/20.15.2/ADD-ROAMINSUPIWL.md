---
id: UNC@20.15.2@MMLCommand@ADD ROAMINSUPIWL
type: MMLCommand
name: ADD ROAMINSUPIWL（增加漫入场景SUPI白名单）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ROAMINSUPIWL
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# ADD ROAMINSUPIWL（增加漫入场景SUPI白名单）

## 功能

**适用NF：NRF**

该命令用于增加漫入场景SUPI白名单。

该命令与漫入SUPI服务发现白名单开关SET NRFINTERFUNC中的ROAMINSUPIWLSW配合使用，ROAMINSUPIWLSW为FUNC_ON时基于白名单用户SUPI号码或SUPI号段列表配置I-NRF允许服务发现他网AUSF/UDM。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入100000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGSTART | 号段起始字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段的结束号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROAMINSUPIWL]] · 漫入场景SUPI白名单（ROAMINSUPIWL）

## 使用实例

增加漫入场景SUPI白名单，号段起始字符串123456789876501，号段结束字符串123456789876505：

```
ADD ROAMINSUPIWL: SEGSTART="123456789876501", SEGEND="123456789876505";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加漫入场景SUPI白名单（ADD-ROAMINSUPIWL）_70462521.md`
