---
id: UDG@20.15.2@MMLCommand@RMV OSPFINTERFACEAUTH
type: MMLCommand
name: RMV OSPFINTERFACEAUTH（删除OSPF接口认证配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFINTERFACEAUTH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF接口认证配置
status: active
---

# RMV OSPFINTERFACEAUTH（删除OSPF接口认证配置）

## 功能

该命令用于删除OSPF接口认证配置。

## 注意事项

- 该命令执行后立即生效。
- 删除OSPF接口认证，请确保和邻居认证配置相同，否则会导致邻接关系中断，影响业务。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。 |
| AREAID | 区域号 | 可选必选说明：必选参数<br>参数含义：区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFINTERFACEAUTH]] · OSPF接口认证配置（OSPFINTERFACEAUTH）

## 使用实例

删除接口Ethernet64/0/4配置的OSPF keychain认证：

```
RMV OSPFINTERFACEAUTH:PROCID=1,AREAID="0.0.0.0",IFNAME="Ethernet64/0/4";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-OSPFINTERFACEAUTH.md`
