---
id: UNC@20.15.2@MMLCommand@DSP ARPENTRYSTATISTICS
type: MMLCommand
name: DSP ARPENTRYSTATISTICS（显示ARP统计计数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ARPENTRYSTATISTICS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP表项统计查询
status: active
---

# DSP ARPENTRYSTATISTICS（显示ARP统计计数）

## 功能

该命令用于显示ARP表项的统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数指定需要统计表项信息的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ARPENTRYSTATISTICS]] · ARP统计计数（ARPENTRYSTATISTICS）

## 使用实例

统计接口Ethernet64/0/5下表项信息：

```
DSP ARPENTRYSTATISTICS:IFNAME="Ethernet64/0/5";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
   接口名称  =  Ethernet64/0/5
动态ARP数量  =  8
静态ARP数量  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ARPENTRYSTATISTICS.md`
