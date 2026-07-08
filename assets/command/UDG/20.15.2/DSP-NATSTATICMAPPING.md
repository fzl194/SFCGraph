---
id: UDG@20.15.2@MMLCommand@DSP NATSTATICMAPPING
type: MMLCommand
name: DSP NATSTATICMAPPING（查询NAT静态地址映射关系）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NATSTATICMAPPING
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- NAT服务管理
- NAT服务管理
- NAT静态地址映射
status: active
---

# DSP NATSTATICMAPPING（查询NAT静态地址映射关系）

## 功能

**适用NF：UPF**

该命令用于查询NAT静态地址映射关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INSIDEIPV4：私网IPv4地址。<br>- GLOBALIPV4：公网IPv4地址。<br>默认值：无<br>配置原则：无 |
| STATICMAPNAME | 静态地址映射关系名称 | 可选必选说明：必选参数<br>参数含义：静态地址映射关系名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| INSIDEIPV4 | 私网IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“INSIDEIPV4”时为必选参数。<br>参数含义：私网IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| GLOBALIPV4 | 公网IPv4地址 | 可选必选说明：可选参数<br>参数含义：公网IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PORT | 端口 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“GLOBALIPV4”时为必选参数。<br>参数含义：端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NAT静态地址映射关系（NATSTATICMAPPING）](configobject/UDG/20.15.2/NATSTATICMAPPING.md)

## 使用实例

该命令用于查询NAT静态地址映射关系：

```
DSP NATSTATICMAPPING: QUERYTYPE=INSIDEIPV4, STATICMAPNAME="map1", INSIDEIPV4="10.2.2.8";
```

```

RETCODE = 0  Operation Success.

Static Mapping Information:
---------------------------
                  Static Mapping Name  =  map1
                  Inside IPv4 Address  =  10.2.2.8
                  Global IPv4 Address  =  10.x.x.x
Start Port of the Global IPv4 Address  =  2048
  End Port of the Global IPv4 Address  =  4095
(Number of results = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NAT静态地址映射关系（DSP-NATSTATICMAPPING）_05939508.md`
