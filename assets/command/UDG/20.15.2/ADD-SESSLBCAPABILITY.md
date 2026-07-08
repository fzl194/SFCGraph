---
id: UDG@20.15.2@MMLCommand@ADD SESSLBCAPABILITY
type: MMLCommand
name: ADD SESSLBCAPABILITY（添加会话均衡基线能力值）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SESSLBCAPABILITY
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话均衡基线能力
status: active
---

# ADD SESSLBCAPABILITY（添加会话均衡基线能力值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](添加会话均衡基线能力值（ADD SESSLBCAPABILITY）_15006393.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果参数设置不合理，会导致业务板负荷不均、转发不通、用户激活失败等。

在异构硬件场景下，使用该命令用于配置CPU的基线能力。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置3000条。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | Cpu类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。当前只支持x86_64和aarch64两种类型。<br>默认值：无<br>配置原则：无 |
| VERSION | Cpu代数 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Cpu代数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| FREQUENCY | Cpu主频 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Cpu主频。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| CAPABILITY | 能力 | 可选必选说明：必选参数<br>参数含义：该参数用来配置Cpu基线能力。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～3000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SESSLBCAPABILITY]] · 会话均衡基线能力值（SESSLBCAPABILITY）

## 使用实例

在异构硬件场景下，配置此命令，让用户会话根据CPU的能力进行负载均衡：

```
ADD SESSLBCAPABILITY: TYPE="x86_64", VERSION="Intel(R) Xeon(R) CPU E5-2658 v4 @ 2.30GHz", FREQUENCY=2500, CAPABILITY=900;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SESSLBCAPABILITY.md`
