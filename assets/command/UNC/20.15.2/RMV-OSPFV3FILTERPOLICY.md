---
id: UNC@20.15.2@MMLCommand@RMV OSPFV3FILTERPOLICY
type: MMLCommand
name: RMV OSPFV3FILTERPOLICY（删除OSPFv3过滤策略配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPFV3FILTERPOLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3过滤策略配置
status: active
---

# RMV OSPFV3FILTERPOLICY（删除OSPFv3过滤策略配置）

## 功能

该命令用于删除OSPFv3过滤策略。

## 注意事项

- 该命令执行后立即生效。
- 要删除的FilterPolicy必须存在。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| FILTERTYPE | 过滤方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤方向是import还是export。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- import：引入方向的过滤。<br>- export：发布方向的过滤。<br>默认值：无 |
| PROTOCOL | 协议号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“FILTERTYPE”配置为“export”时为可选参数。<br>参数含义：该参数用于指定对某一种协议的路由进行过滤。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- direct：直连路由。<br>- static：静态路由。<br>- bgp：BGP协议。<br>- ospfv3：OSPFv3协议。<br>- wlr：无线路由。<br>默认值：无 |
| PROTOCOLPROCESSID | 协议进程号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOL”配置为“ospfv3”时为必选参数。<br>参数含义：该参数用于指定对某一进程的路由进行过滤。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3过滤策略配置（OSPFV3FILTERPOLICY）](configobject/UNC/20.15.2/OSPFV3FILTERPOLICY.md)

## 使用实例

删除设备上OSPFv3进程1下的import类型过滤策略：

```
RMV OSPFV3FILTERPOLICY: PROCID=1,TOPOID=0,FILTERTYPE=import;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除OSPFv3过滤策略配置（RMV-OSPFV3FILTERPOLICY）_00865593.md`
