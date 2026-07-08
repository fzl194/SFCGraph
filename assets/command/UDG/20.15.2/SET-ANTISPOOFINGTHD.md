---
id: UDG@20.15.2@MMLCommand@SET ANTISPOOFINGTHD
type: MMLCommand
name: SET ANTISPOOFINGTHD（设置攻击用户去活报文的阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ANTISPOOFINGTHD
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- IP Spoofing攻击防护
- 攻击用户去活的报文一分钟内个数门限
status: active
---

# SET ANTISPOOFINGTHD（设置攻击用户去活报文的阈值）

## 功能

**适用NF：UPF**

该参数用于指定攻击用户去活报文的阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | THRESHOLD |
| --- | --- |
| 初始值 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| THRESHOLD | 攻击用户去活报文的阈值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定攻击用户去活报文的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ANTISPOOFINGTHD]] · 攻击用户去活报文的阈值（ANTISPOOFINGTHD）

## 使用实例

假设运营商需要对攻击用户的报文进行流控处理，通过配置SET ANTISPOOFINGTHD命令来实现，门限值为5000：

```
SET ANTISPOOFINGTHD: THRESHOLD=5000;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-ANTISPOOFINGTHD.md`
