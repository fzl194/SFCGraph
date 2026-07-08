---
id: UDG@20.15.2@MMLCommand@DSP OSPFPEER
type: MMLCommand
name: DSP OSPFPEER（查询OSPF邻居状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFPEER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF邻居状态
status: active
---

# DSP OSPFPEER（查询OSPF邻居状态）

## 功能

该命令用于显示OSPF邻居信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NBRROUTERID | 邻居路由器标识 | 可选必选说明：可选参数<br>参数含义：邻居路由器标识。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| NBRIPADDR | 邻居IP地址 | 可选必选说明：可选参数<br>参数含义：邻居IP地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：接口名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFPEER]] · OSPF的NBMA网络邻居路由器配置（OSPFPEER）

## 使用实例

显示设备OSPF进程号为1的所有节点邻居信息：

```
DSP OSPFPEER: PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
  邻居路由器标识  =  192.168.5.2
          进程号  =  1
          区域号  =  0.0.0.0
      邻居IP地址  =  192.168.5.2
          接口名  =  Ethernet64/0/5
        邻居状态  =  Full
        邻居模式  =  Slave
      邻居优先级  =  1
      指定路由器  =  192.168.5.1
      备份路由器  =  192.168.5.2
   邻居接口MTU值  =  0
  邻居认证序列号  =  0
      邻居UP时间  =  00h21m22s
          GR状态  =  NA
    失效时间（s） =  38
邻居重传间隔（s） =  5
          主机名  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-OSPFPEER.md`
