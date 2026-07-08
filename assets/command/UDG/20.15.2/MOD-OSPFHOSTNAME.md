---
id: UDG@20.15.2@MMLCommand@MOD OSPFHOSTNAME
type: MMLCommand
name: MOD OSPFHOSTNAME（修改OSPF主机名配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFHOSTNAME
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF主机名配置
status: active
---

# MOD OSPFHOSTNAME（修改OSPF主机名配置）

## 功能

该命令用于修改OSPF主机名。

## 注意事项

- 该命令执行后立即生效。
- 只有配置了OSPF进程后才能使用该命令。
- 如果配置了hostname参数，则以hostname作为动态主机名发布，如果只执行hostname命令，不配置hostname参数，则以sysname命令输入的设备名称作为动态主机名发布。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFHOSTNAME]] · OSPF主机名配置（OSPFHOSTNAME）

## 使用实例

修改OSPF进程1下主机名为“BLR1”：

```
MOD OSPFHOSTNAME:PROCID=1, HOSTNAME="BLR1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-OSPFHOSTNAME.md`
