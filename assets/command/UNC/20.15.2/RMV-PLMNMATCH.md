---
id: UNC@20.15.2@MMLCommand@RMV PLMNMATCH
type: MMLCommand
name: RMV PLMNMATCH（删除MCC与MNC的归属关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PLMNMATCH
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- PLMN归属管理
status: active
---

# RMV PLMNMATCH（删除MCC与MNC的归属关系）

## 功能

**适用NF：SGW-C**

该命令用于删除MCC与MNC的归属关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLMNMATCH]] · MCC与MNC的归属关系（PLMNMATCH）

## 使用实例

删除MCC为678下MNC为123的归属，执行如下命令：

```
RMV PLMNMATCH: MCC="123", MNC="678";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MCC与MNC的归属关系（RMV-PLMNMATCH）_63709202.md`
