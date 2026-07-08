---
id: UNC@20.15.2@MMLCommand@RMV NGSGWPLMN
type: MMLCommand
name: RMV NGSGWPLMN（删除SGW-C Home PLMN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGSGWPLMN
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- SGW计费控制
- SGW-C PLMN信息管理
status: active
---

# RMV NGSGWPLMN（删除SGW-C Home PLMN）

## 功能

![](删除SGW-C Home PLMN（RMV NGSGWPLMN）_23782818.assets/notice_3.0-zh-cn_2.png)

删除SGW-C Home PLMN可能影响用户计费模式。

**适用NF：SGW-C**

该命令用于删除指定的SGW-C Home PLMN。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成SGW-C上Home PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成SGW-C上Home PLMN的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGSGWPLMN]] · SGW-C Home PLMN（NGSGWPLMN）

## 使用实例

将12368从运营商的SGW-C Home PLMN列表中删除，执行如下命令：

```
RMV NGSGWPLMN: MCC="123", MNC="68";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SGW-C-Home-PLMN（RMV-NGSGWPLMN）_23782818.md`
