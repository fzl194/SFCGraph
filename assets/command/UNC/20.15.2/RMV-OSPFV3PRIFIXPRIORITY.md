---
id: UNC@20.15.2@MMLCommand@RMV OSPFV3PRIFIXPRIORITY
type: MMLCommand
name: RMV OSPFV3PRIFIXPRIORITY（删除OSPFv3路由收敛优先级配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPFV3PRIFIXPRIORITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3路由收敛优先级配置
status: active
---

# RMV OSPFV3PRIFIXPRIORITY（删除OSPFv3路由收敛优先级配置）

## 功能

该命令用于恢复OSPFv3路由的默认收敛优先级。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| PRIORITY | 路由优先级 | 可选必选说明：必选参数<br>参数含义：路由优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- critical：配置OSPFv3路由的收敛优先级为关键。<br>- high：配置OSPFv3路由的收敛优先级为高。<br>- medium：配置OSPFv3路由的收敛优先级为中。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFV3PRIFIXPRIORITY]] · OSPFv3路由收敛优先级配置（OSPFV3PRIFIXPRIORITY）

## 使用实例

删除OSPFv3进程1下critical路由收敛优先级配置：

```
RMV OSPFV3PRIFIXPRIORITY:PROCID=1,PRIORITY=critical;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除OSPFv3路由收敛优先级配置（RMV-OSPFV3PRIFIXPRIORITY）_49801762.md`
