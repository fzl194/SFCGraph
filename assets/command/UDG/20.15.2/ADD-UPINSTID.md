---
id: UDG@20.15.2@MMLCommand@ADD UPINSTID
type: MMLCommand
name: ADD UPINSTID（添加NF实例ID）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPINSTID
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- DN管理
- NE信息管理
- NF实例标识管理
status: active
---

# ADD UPINSTID（添加NF实例ID）

## 功能

**适用NF：UPF**

该命令用于添加一个NF实例ID配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UUID | UUID | 可选必选说明：必选参数<br>参数含义：NF实例标识ID。<br>数据来源：全网规划<br>取值范围：字符串类型，NF实例ID的长度为36个字节，以连字号分为五段，格式为：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (8-4-4-4-12)，其中每个 x 是 0-9 或 a-f 范围内的一个十六进制的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF实例ID（UPINSTID）](configobject/UDG/20.15.2/UPINSTID.md)

## 使用实例

假如运营商希望增加一条NF实例ID为"4947a69a-f61b-4bc1-b9da-47c9c5d14b64"的记录：

```
ADD UPINSTID: UUID="4947a69a-f61b-4bc1-b9da-47c9c5d14b64";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加NF实例ID（ADD-UPINSTID）_93973671.md`
