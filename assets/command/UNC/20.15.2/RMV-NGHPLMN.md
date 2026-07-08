---
id: UNC@20.15.2@MMLCommand@RMV NGHPLMN
type: MMLCommand
name: RMV NGHPLMN（删除5G Home PLMN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGHPLMN
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- SGW-C
- PGW-C
- GGSN
- NSSF
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- Home PLMN信息管理
status: active
---

# RMV NGHPLMN（删除5G Home PLMN）

## 功能

![](删除5G Home PLMN（RMV NGHPLMN）_09653738.assets/notice_3.0-zh-cn_2.png)

删除Home PLMN可能影响用户接入。

**适用NF：AMF、SMF、NRF、SGW-C、PGW-C、GGSN、NSSF、SMSF**

该命令用以删除指定的Home PLMN。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成Home PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成Home PLMN的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGHPLMN]] · 5G Home PLMN（NGHPLMN）

## 使用实例

将12368从运营商的Home PLMN列表中删除，执行如下命令：

```
RMV NGHPLMN: MCC="123", MNC="68";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGHPLMN.md`
