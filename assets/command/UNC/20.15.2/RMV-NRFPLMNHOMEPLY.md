---
id: UNC@20.15.2@MMLCommand@RMV NRFPLMNHOMEPLY
type: MMLCommand
name: RMV NRFPLMNHOMEPLY（删除指定拜访地PLMN的归属地策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFPLMNHOMEPLY
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

# RMV NRFPLMNHOMEPLY（删除指定拜访地PLMN的归属地策略）

## 功能

**适用NF：NRF**

该命令用于删除NRF作为归属地NRF时对指定拜访地PLMN的跨PLMN请求处理策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示拜访地PLMN的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示拜访地PLMN的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFPLMNHOMEPLY]] · 指定拜访地PLMN的归属地策略（NRFPLMNHOMEPLY）

## 使用实例

删除移动国家码为460，移动网号为03的指定拜访地PLMN的归属地策略。

```
RMV NRFPLMNHOMEPLY: MCC="466", MNC="03";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除指定拜访地PLMN的归属地策略（RMV-NRFPLMNHOMEPLY）_71516451.md`
