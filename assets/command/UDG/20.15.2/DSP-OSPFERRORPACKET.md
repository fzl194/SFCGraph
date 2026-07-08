---
id: UDG@20.15.2@MMLCommand@DSP OSPFERRORPACKET
type: MMLCommand
name: DSP OSPFERRORPACKET（查询OSPF错误报文的信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFERRORPACKET
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF错误报文信息
status: active
---

# DSP OSPFERRORPACKET（查询OSPF错误报文的信息）

## 功能

该命令用于查询OSPF错误报文的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PKTNUM | 指定查询的错误报文的数量 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询最近接收的错误报文的数目。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10。<br>默认值：1 |

## 操作的配置对象

- [OSPF错误报文的信息（OSPFERRORPACKET）](configobject/UDG/20.15.2/OSPFERRORPACKET.md)

## 使用实例

查询OSPF错误报文的信息：

```
DSP OSPFERRORPACKET:PKTNUM=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
指定查询的错误报文的数量  =  1
          错误报文的序号  =  1
          错误报文的来源  =  192.168.7.2
      错误报文的目的地址  =  192.168.7.1
  接收错误报文的接口名称  =  Ethernet66/0/3
      错误报文产生的原因  =  接口MTU值不匹配
                接收时间  =  2017-10-24 12:05:38
                报文长度  =  72
                报文内容  =  45 C0 34 00 00 1D 00 00 01 59 9C 70 07 07 07 02
  07 07 07 01 02 02 00 34 02 02 02 02 00 00 00 00
  65 52 00 00 00 00 00 00 00 00 00 00 13 92 02 00
  00 01 38 6E 06 F1 02 01 02 02 02 02 02 02 02 02
  80 00 00 F0 B4 4B 00 3C
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF错误报文的信息（DSP-OSPFERRORPACKET）_49961186.md`
