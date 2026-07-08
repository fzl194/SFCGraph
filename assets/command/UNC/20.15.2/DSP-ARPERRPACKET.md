---
id: UNC@20.15.2@MMLCommand@DSP ARPERRPACKET
type: MMLCommand
name: DSP ARPERRPACKET（显示ARP错误报文统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ARPERRPACKET
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP统计查询
status: active
---

# DSP ARPERRPACKET（显示ARP错误报文统计）

## 功能

该命令用于显示设备上ARP错误报文信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/ARPERRPACKET]] · ARP错误报文统计（ARPERRPACKET）

## 使用实例

显示错误报文信息：

```
DSP ARPERRPACKET:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
接口名称         接收时间               接收报文内容

Ethernet64/0/5   2016-05-23T21:43:40    00 01 08 00 06 04 00 02 14 11 26 21 03 00 BD 64
00 0B 14 11 26 21 03 00 BD 64 00 0B

Ethernet64/0/5   2016-05-23T21:43:42    00 01 08 00 06 04 00 01 14 11 26 21 03 00 BD 64
00 0B FF FF FF FF FF FF BD 64 00 0B

(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ARPERRPACKET.md`
