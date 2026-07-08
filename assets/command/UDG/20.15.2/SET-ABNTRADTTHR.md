---
id: UDG@20.15.2@MMLCommand@SET ABNTRADTTHR
type: MMLCommand
name: SET ABNTRADTTHR（设置异常流量检测报文阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ABNTRADTTHR
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务防欺诈
- 异常下行流量检测阈值
status: active
---

# SET ABNTRADTTHR（设置异常流量检测报文阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询终端异常下行流量检测阈值。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | DETECTTHR |
| --- | --- |
| 初始值 | 20 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DETECTTHR | 异常流量检测报文阈值 | 可选必选说明：可选参数<br>参数含义：异常流量检测报文阈值个数。<br>数据来源：本端规划<br>取值范围：整数类型，1-255。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD ABNTRAFFICDT命令配置生成。<br>- 建议根据现网异常下行流程值进行配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ABNTRADTTHR]] · 异常流量检测报文阈值（ABNTRADTTHR）

## 使用实例

假如运营商需查询终端异常下行流量检测阈值：

```
SET ABNTRADTTHR: DETECTTHR=20;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-ABNTRADTTHR.md`
