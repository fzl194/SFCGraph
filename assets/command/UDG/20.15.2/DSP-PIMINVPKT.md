---
id: UDG@20.15.2@MMLCommand@DSP PIMINVPKT
type: MMLCommand
name: DSP PIMINVPKT（查询PIM无效报文）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PIMINVPKT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- 收到的PIM非法报文内容
status: active
---

# DSP PIMINVPKT（查询PIM无效报文）

## 功能

该命令用于显示PIM无效报文信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PIMINVPKT]] · PIM无效报文（PIMINVPKT）

## 使用实例

显示PIM无效报文信息：

```
DSP PIMINVPKT:ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0 操作成功

结果如下
-------------------------
                            地址族 = IPv4单播
无效报文按照时间排序（逆序）的序号 = 1
              接收到无效报文的接口 = Ethernet64/0/4
              接收到无效报文的时间 = 2017-05-31 06:49:11
                          时区显示 = UTC
                    无效报文的长度 = 34
                    无效报文的类型 = Invalid IP Src Addr
                    无效报文的内容 = 0000: 20 00 38 b4 00 01 00 02 00 69 00 13 00 04 00 00
                                     0010: 00 02 00 14 00 04 f2 b2 a8 3d 00 02 00 04 01 f4
                                     0020: 09 c4
(结果个数 = 1)
----- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PIMINVPKT.md`
