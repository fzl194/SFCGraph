---
id: UDG@20.15.2@MMLCommand@MOD OSPFPREFERENCE
type: MMLCommand
name: MOD OSPFPREFERENCE（修改OSPF协议路由的优先级配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFPREFERENCE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF协议路由的优先级配置
status: active
---

# MOD OSPFPREFERENCE（修改OSPF协议路由的优先级配置）

## 功能

该命令用于修改OSPF协议路由的优先级配置。

## 注意事项

- 该命令执行后立即生效。
- 只有在配置了OSPF进程后才能使用此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| ROUTETYPE | 路由类型 | 可选必选说明：必选参数<br>参数含义：路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- default：区域内和区域间路由。<br>- ase：AS-External路由。<br>- intra：区域内路由。<br>- inter：区域间路由。<br>默认值：无 |
| PREFERENCE | 路由优先级 | 可选必选说明：可选参数<br>参数含义：路由优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：<br>- 优先级的值越小，其实际的优先程度越高。<br>- PREFERENCE和ROUTEPOLICYNAME参数如果都不配置，则实际没有调整路由优先级。<br>- 缺省情况下，OSPF路由的优先级为10。当指定ASE时，缺省优先级为150。 |
| ROUTEPOLICYNAME | 路由策略名称 | 可选必选说明：可选参数<br>参数含义：路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 区分大小写。<br>- PREFERENCE和ROUTEPOLICYNAME参数如果都不配置，则实际没有调整路由优先级。 |

## 操作的配置对象

- [OSPF协议路由的优先级配置（OSPFPREFERENCE）](configobject/UDG/20.15.2/OSPFPREFERENCE.md)

## 使用实例

修改OSPF进程1的区域内路由的优先级为150：

```
MOD OSPFPREFERENCE:PROCID=1,TOPOID=0,ROUTETYPE=intra,PREFERENCE=150;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPF协议路由的优先级配置（MOD-OSPFPREFERENCE）_50121234.md`
