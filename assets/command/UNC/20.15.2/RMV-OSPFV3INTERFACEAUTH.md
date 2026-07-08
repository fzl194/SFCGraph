---
id: UNC@20.15.2@MMLCommand@RMV OSPFV3INTERFACEAUTH
type: MMLCommand
name: RMV OSPFV3INTERFACEAUTH（删除OSPFv3接口认证配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPFV3INTERFACEAUTH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3接口认证配置
status: active
---

# RMV OSPFV3INTERFACEAUTH（删除OSPFv3接口认证配置）

## 功能

该命令用于删除OSPFv3接口上所使用的验证模式及验证口令。

## 注意事项

- 该命令执行后立即生效。
- 删除OSPFv3接口认证，请确保和邻居认证配置相同，否则会导致邻接关系中断，影响业务。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：必选参数<br>参数含义：OSPFv3区域号。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| INSTANCEID | 实例号 | 可选必选说明：必选参数<br>参数含义：实例号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFV3INTERFACEAUTH]] · OSPFv3接口认证配置（OSPFV3INTERFACEAUTH）

## 使用实例

删除接口Ethernet64/0/3下OSPFv3 HMAC-SHA256验证模式：

```
RMV OSPFV3INTERFACEAUTH:PROCID=1,AREAID="0.0.0.0",IFNAME="Ethernet64/0/3",INSTANCEID=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-OSPFV3INTERFACEAUTH.md`
