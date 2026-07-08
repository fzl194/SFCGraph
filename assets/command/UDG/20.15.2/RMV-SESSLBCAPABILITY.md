---
id: UDG@20.15.2@MMLCommand@RMV SESSLBCAPABILITY
type: MMLCommand
name: RMV SESSLBCAPABILITY（删除会话均衡基线能力值）
nf: UDG
version: 20.15.2
verb: RMV
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

# RMV SESSLBCAPABILITY（删除会话均衡基线能力值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](删除会话均衡基线能力值（RMV SESSLBCAPABILITY）_27399646.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除前请确认该CPU基线已不存在，否则会导致业务板负荷不均、转发不通、用户激活失败等。

该命令用于删除CPU的基线能力。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | Cpu类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。当前只支持x86_64和aarch64两种类型。<br>默认值：无<br>配置原则：无 |
| VERSION | Cpu代数 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Cpu代数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| FREQUENCY | Cpu主频 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Cpu主频。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SESSLBCAPABILITY]] · 会话均衡基线能力值（SESSLBCAPABILITY）

## 使用实例

删除已配置的CPUCAPABILITY实例信息：

```
RMV SESSLBCAPABILITY: TYPE="x86_64", VERSION="Intel(R) Xeon(R) CPU E5-2658 v4 @ 2.30GHz", FREQUENCY=2500;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SESSLBCAPABILITY.md`
