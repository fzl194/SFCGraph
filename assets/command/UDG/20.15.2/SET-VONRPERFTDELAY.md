---
id: UDG@20.15.2@MMLCommand@SET VONRPERFTDELAY
type: MMLCommand
name: SET VONRPERFTDELAY（配置理想到达报文的最小时延偏差、固定传输时延）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: VONRPERFTDELAY
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR 理想到达报文
status: active
---

# SET VONRPERFTDELAY（配置理想到达报文的最小时延偏差、固定传输时延）

## 功能

**适用NF：UPF**

该命令用于设置理想到达报文的最小时延偏差、固定传输时延。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MINDELAYERROR | FIXTRANSTIME |
| --- | --- | --- |
| 初始值 | 10 | 180 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MINDELAYERROR | 理想到达报文的最小时延偏差 | 可选必选说明：可选参数<br>参数含义：该参数用于指定理想到达报文的最小时延偏差。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～200，粒度为100。<br>默认值：无<br>配置原则：无 |
| FIXTRANSTIME | 理想时延报文的固定传输时延 | 可选必选说明：可选参数<br>参数含义：该参数用于指定理想时延报文的固定传输时延。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1000，单位是毫秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VONRPERFTDELAY]] · 理想到达报文的最小时延偏差、固定传输时延（VONRPERFTDELAY）

## 使用实例

设置理想报文的最小时延误差、固定传输时延：

```
SET VONRPERFTDELAY: MINDELAYERROR=20, FIXTRANSTIME=20;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置理想到达报文的最小时延偏差、固定传输时延（SET-VONRPERFTDELAY）_91535714.md`
