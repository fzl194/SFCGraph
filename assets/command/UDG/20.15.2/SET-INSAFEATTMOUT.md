---
id: UDG@20.15.2@MMLCommand@SET INSAFEATTMOUT
type: MMLCommand
name: SET INSAFEATTMOUT（设置流特征节点超时时间）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: INSAFEATTMOUT
command_category: 配置类
applicable_nf:
- CloudEPSN
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 智能SA管理
- 流特征节点超时时间配置
status: active
---

# SET INSAFEATTMOUT（设置流特征节点超时时间）

## 功能

**适用NF：CloudEPSN**

设置流特征节点超时时间。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | TIMEOUT |
| --- | --- |
| 初始值 | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMEOUT | 超时时间(秒) | 可选必选说明：必选参数<br>参数含义：该参数用于表示流特征结点超时时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1~60，单位秒。<br>默认值：无<br>配置原则：推荐使用初始值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/INSAFEATTMOUT]] · 流特征节点超时时间（INSAFEATTMOUT）

## 使用实例

设置超时时间为30秒：

```
SET INSAFEATTMOUT:TIMEOUT=30;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-INSAFEATTMOUT.md`
