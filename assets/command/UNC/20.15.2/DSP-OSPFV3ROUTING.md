---
id: UNC@20.15.2@MMLCommand@DSP OSPFV3ROUTING
type: MMLCommand
name: DSP OSPFV3ROUTING（查询OSPFv3路由信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFV3ROUTING
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- 查询OSPFv3路由信息
status: active
---

# DSP OSPFV3ROUTING（查询OSPFv3路由信息）

## 功能

该命令用于显示OSPFv3路由信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| DESTIPV6ADDR | 目的IPv6地址 | 可选必选说明：可选参数<br>参数含义：目的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| IPV6MASKLEN | 前缀长度 | 可选必选说明：可选参数<br>参数含义：前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |
| NEXTHOPIPV6ADDR | 下一跳IPv6地址 | 可选必选说明：可选参数<br>参数含义：下一跳IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [OSPFv3路由信息（OSPFV3ROUTING）](configobject/UNC/20.15.2/OSPFV3ROUTING.md)

## 使用实例

显示设备OSPFv3进程的所有路由信息：

```
DSP OSPFV3ROUTING:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
             OSPFv3进程号  =  1000
               路径Cost值  =  1
                 路径类型  =  directly connected
                   优先级  =  Low
               下一跳数目  =  1
             目的IPv6地址  =  2001:db8::
                 前缀长度  =  64
           下一跳IPv6地址  =  2001:db8::1
                 接口名称  =  Ethernet64/0/7
                 显示标志  =  Added to URT6
                 备份接口  =  NULL
       备份下一跳IPv6地址  =  ::
                 备份类型  =  None
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPFv3路由信息（DSP-OSPFV3ROUTING）_50121634.md`
