---
id: UNC@20.15.2@MMLCommand@ADD SMSCGT
type: MMLCommand
name: ADD SMSCGT（增加SMSC的GT）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMSCGT
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- SMSC选择管理
status: active
---

# ADD SMSCGT（增加SMSC的GT）

## 功能

**适用NF：SMSF**

该命令用于增加SMSC的GT记录。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入256条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GT | SMSC的GT | 可选必选说明：必选参数<br>参数含义：该参数用于表示SMSC的GT。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCGT]] · SMSC的GT（SMSCGT）

## 使用实例

当运营商需要增加一条SMSC的GT为“123456”的记录时，执行如下命令：

```
ADD SMSCGT: GT="123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SMSC的GT（ADD-SMSCGT）_74378480.md`
