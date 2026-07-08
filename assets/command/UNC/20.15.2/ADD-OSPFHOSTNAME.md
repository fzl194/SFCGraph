---
id: UNC@20.15.2@MMLCommand@ADD OSPFHOSTNAME
type: MMLCommand
name: ADD OSPFHOSTNAME（创建OSPF主机名配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OSPFHOSTNAME
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8016
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF主机名配置
status: active
---

# ADD OSPFHOSTNAME（创建OSPF主机名配置）

## 功能

该命令用于创建OSPF主机名。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8016。
- 只有执行ADD OSPF配置了OSPF进程后才能使用该命令。
- 如果配置了hostname参数，则以hostname作为动态主机名发布，如果只执行hostname命令，不配置hostname参数，则以sysname命令输入的设备名称作为动态主机名发布。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFHOSTNAME]] · OSPF主机名配置（OSPFHOSTNAME）

## 使用实例

OSPF进程1下创建主机名“BLR”：

```
ADD OSPFHOSTNAME:PROCID=1, HOSTNAME="BLR";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-OSPFHOSTNAME.md`
