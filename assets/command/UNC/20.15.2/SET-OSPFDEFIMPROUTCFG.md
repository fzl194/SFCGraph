---
id: UNC@20.15.2@MMLCommand@SET OSPFDEFIMPROUTCFG
type: MMLCommand
name: SET OSPFDEFIMPROUTCFG（设置OSPF引入路由默认配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OSPFDEFIMPROUTCFG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 设置OSPF引入路由默认配置
status: active
---

# SET OSPFDEFIMPROUTCFG（设置OSPF引入路由默认配置）

## 功能

该命令用于设置OSPF引入路由默认配置。

## 注意事项

- 该命令执行后立即生效。
- 只有在配置了OSPF进程后才能使用此命令。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| MAXLOADBALAC | DEFCOST | DEFCSTINMETRFLG | DEFTAG | DEFAULTTYPE |
| --- | --- | --- | --- | --- |
| 128 | 1 | FALSE | 1 | Type2 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| MAXLOADBALAC | 等价路由最大数量 | 可选必选说明：可选参数<br>参数含义：等价路由最大数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无 |
| DEFCOST | 默认开销值 | 可选必选说明：可选参数<br>参数含义：默认开销值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777214。<br>默认值：无<br>配置原则：DEFCOST和DEFCSTINMETRFLG不可以同时配置。 |
| DEFCSTINMETRFLG | 引入路由的开销值为路由自带的cost值 | 可选必选说明：可选参数<br>参数含义：引入路由的开销值为路由自带的cost值。如果没有指定开销值，则使用DEFCOST参数设置的缺省开销值。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：DEFCOST和DEFCSTINMETRFLG不可以同时配置。 |
| DEFTAG | 外部路由的标记 | 可选必选说明：可选参数<br>参数含义：外部路由的标记。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| DEFAULTTYPE | 外部路由类型 | 可选必选说明：可选参数<br>参数含义：外部路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Type1：外部路由类型1。<br>- Type2：外部路由类型2。<br>默认值：无 |

## 操作的配置对象

- [OSPF引入路由默认配置（OSPFDEFIMPROUTCFG）](configobject/UNC/20.15.2/OSPFDEFIMPROUTCFG.md)

## 使用实例

OSPF进程1下设置等价路由最大数量为10：

```
SET OSPFDEFIMPROUTCFG:PROCID=1,TOPOID=0,MAXLOADBALAC=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置OSPF引入路由默认配置（SET-OSPFDEFIMPROUTCFG）_50120858.md`
