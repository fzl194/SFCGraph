---
id: UNC@20.15.2@MMLCommand@DSP OSPFV3PEER
type: MMLCommand
name: DSP OSPFV3PEER（查询OSPFv3邻居信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFV3PEER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- 查询OSPFv3邻居信息
status: active
---

# DSP OSPFV3PEER（查询OSPFv3邻居信息）

## 功能

该命令用于显示OSPFv3邻居信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NBRROUTERID | 邻居路由器标识 | 可选必选说明：可选参数<br>参数含义：邻居路由器标识。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFV3PEER]] · OSPFv3邻居信息（OSPFV3PEER）

## 使用实例

显示设备OSPFv3进程号为1的所有节点邻居信息：

```
DSP OSPFV3PEER: PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
  邻居路由器标识  =  10.2.2.2
    OSPFv3进程号  =  1
  OSPFv3区域标识  =  0.0.0.0
        接口名称  =  Ethernet64/0/5
        邻居状态  =  Full
邻居路由器优先级  =  1
    邻居接口状态  =  Backup
邻居Dead间隔（s） =  00:00:39
          实例号  =  1
          主机名  =  NULL
        邻居地址  =  FE80::250:56FF:FEAC:FC80
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPFv3邻居信息（DSP-OSPFV3PEER）_00600589.md`
