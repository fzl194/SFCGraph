---
id: UNC@20.15.2@MMLCommand@MOD USRTAIRANGE
type: MMLCommand
name: MOD USRTAIRANGE（修改用户TAI区域）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: USRTAIRANGE
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- 用户TAI区域
status: active
---

# MOD USRTAIRANGE（修改用户TAI区域）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于修改用户TAI区域。

## 注意事项

- 该命令执行后立即生效。

- 由于PCFSSCOPEBIND记录中不同PCF业务服务区对应的用户TAI区域不能重叠，MOD USRTAIRANGE时需要检查重复性。若该操作会导致PCFSSCOPEBIND中绑定的TAI区域重叠，则配置下发失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGENAME | 区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：<br>只允许输入十进制数字（0-9）。 |
| MNC | 移动网络码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网络码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：<br>只允许输入十进制数字（0-9）。 |
| TACSTART | TAC区域起点值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAC区域起点值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是4~6。<br>默认值：无<br>配置原则：<br>该参数由4位或者6位十六进制数组成。 |
| TACEND | TAC区域结束值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAC区域结束值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是4~6。<br>默认值：无<br>配置原则：<br>该参数由4位或者6位十六进制数组成。该参数的位数需要与TACSTART值位数保持一致，并且值大于等于TACSTART值。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRTAIRANGE]] · 用户TAI区域（USRTAIRANGE）

## 使用实例

修改区域名称为tai1的记录的TAC区域结束值为1236。

```
MOD USRTAIRANGE: RANGENAME="tai1", TACEND="1236";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-USRTAIRANGE.md`
