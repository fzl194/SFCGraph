---
id: UDG@20.15.2@MMLCommand@RMV OSPFV3DEFAULTROUTE
type: MMLCommand
name: RMV OSPFV3DEFAULTROUTE（删除OSPFv3默认路由宣告配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFV3DEFAULTROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3默认路由宣告配置
status: active
---

# RMV OSPFV3DEFAULTROUTE（删除OSPFv3默认路由宣告配置）

## 功能

该命令用于删除OSPFv3默认路由宣告。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFV3DEFAULTROUTE]] · OSPFv3默认路由宣告配置（OSPFV3DEFAULTROUTE）

## 使用实例

删除OSPFv3进程1下的默认路由：

```
RMV OSPFV3DEFAULTROUTE:PROCID=1,TOPOID=0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除OSPFv3默认路由宣告配置（RMV-OSPFV3DEFAULTROUTE）_49802410.md`
