---
id: UDG@20.15.2@MMLCommand@RMV CHRRPTSUBID
type: MMLCommand
name: RMV CHRRPTSUBID（删除CHR上报用户）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CHRRPTSUBID
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 呼叫日志管理
- CHR本地存盘用户配置
status: active
---

# RMV CHRRPTSUBID（删除CHR上报用户）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除指定用户本地存储CHR表单。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户识别码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CHRRPTSUBID]] · CHR上报用户（CHRRPTSUBID）

## 使用实例

- 删除IMSI为460030123456789的用户本地存储CHR表单的配置：
  ```
  RMV CHRRPTSUBID: IMSI="460030123456789";
  ```
- 删除所有指定用户本地存储CHR表单配置：
  ```
  RMV CHRRPTSUBID:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-CHRRPTSUBID.md`
