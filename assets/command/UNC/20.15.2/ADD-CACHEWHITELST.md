---
id: UNC@20.15.2@MMLCommand@ADD CACHEWHITELST
type: MMLCommand
name: ADD CACHEWHITELST（增加异网白名单PLMN信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CACHEWHITELST
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF Cache管理
status: active
---

# ADD CACHEWHITELST（增加异网白名单PLMN信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加异网白名单PLMN信息。

## 注意事项

- 该命令执行后立即生效。

- CACHEPLCY为“非白名单禁止模式”、“非白名单尽力而为模式”时需要配该命令。
- 有大量漫游用户接入的PLMN建议配置白名单，否则网元可能不会缓存该PLMN的NF数据，导致频繁的去NRF服务发现，影响性能。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定异网缓存白名单中的移动国家码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：<br>本参数由3个十进制数字组成。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定异网白名单中的移动网号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：<br>本参数由2~3个十进制数字组成。 |

## 操作的配置对象

- [异网白名单PLMN信息（CACHEWHITELST）](configobject/UNC/20.15.2/CACHEWHITELST.md)

## 使用实例

增加异网白名单PLMN信息，MCC为460，MNC为03。

```
ADD CACHEWHITELST: MCC="460",MNC="03";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加异网白名单PLMN信息（ADD-CACHEWHITELST）_18357777.md`
