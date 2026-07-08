---
id: UDG@20.15.2@MMLCommand@DSP OSPFROUTING
type: MMLCommand
name: DSP OSPFROUTING（查询OSPF路由信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFROUTING
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF路由信息
status: active
---

# DSP OSPFROUTING（查询OSPF路由信息）

## 功能

该命令用于显示OSPF路由信息。

## 注意事项

此命令最多支持显示1000条路由信息，如果路由信息比较多，建议指定参数进行查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| DESTIPADDR | 目的IP地址 | 可选必选说明：可选参数<br>参数含义：目的IP地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| NEXTHOPIPADDR | 下一跳IP地址 | 可选必选说明：可选参数<br>参数含义：下一跳IP地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| ADVROUTERID | 宣告路由器标识 | 可选必选说明：可选参数<br>参数含义：宣告路由器标识。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：接口名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFROUTING]] · OSPF路由信息（OSPFROUTING）

## 使用实例

显示设备OSPF进程号为1的所有路由信息：

```
DSP OSPFROUTING: PROCESSID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
      进程号  =  1
  目的IP地址  =  192.168.5.0
    掩码长度  =  24
  路径Cost值  =  1
下一跳IP地址  =  192.168.5.1
宣告路由标识  =  192.168.7.1
    区域标识  =  0.0.0.0
    路由类型  =  Direct
      接口名  =  Ethernet64/0/5
        标签  =  0
      优先级  =  Low
  下一跳数目  =  1
  下一跳标志  =  A/-
  备份下一跳  =  0.0.0.0
    备份接口  =  NULL
    备份类型  =  None
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF路由信息（DSP-OSPFROUTING）_50121274.md`
