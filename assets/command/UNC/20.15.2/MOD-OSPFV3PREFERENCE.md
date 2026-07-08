---
id: UNC@20.15.2@MMLCommand@MOD OSPFV3PREFERENCE
type: MMLCommand
name: MOD OSPFV3PREFERENCE（修改OSPFv3路由优先级配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: OSPFV3PREFERENCE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3路由优先级配置
status: active
---

# MOD OSPFV3PREFERENCE（修改OSPFv3路由优先级配置）

## 功能

该命令用于修改OSPFv3协议路由的优先级。

## 注意事项

- 该命令执行后立即生效。
- 只有配置了OSPFv3进程后才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。请使用LST OSPFV3命令查看可用的OSPFv3进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| ROUTETYPE | 路由类型 | 可选必选说明：必选参数<br>参数含义：路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- non-ase：非AS-External路由。<br>- ase：AS-External路由。<br>默认值：无 |
| PREFERENCEVALUE | 优先级 | 可选必选说明：可选参数<br>参数含义：优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：PREFERENCEVALUE和ROUTEPOLICYNAME参数必须至少配置其中一个。 |
| ROUTEPOLICYNAME | 路由策略名称 | 可选必选说明：可选参数<br>参数含义：路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- PREFERENCEVALUE和ROUTEPOLICYNAME参数必须至少配置其中一个。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFV3PREFERENCE]] · OSPFv3路由优先级配置（OSPFV3PREFERENCE）

## 使用实例

修改OSPFv3进程1的路由优先级为150：

```
MOD OSPFV3PREFERENCE:PROCID=1,TOPOID=0,ROUTETYPE=ase,PREFERENCEVALUE=150;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-OSPFV3PREFERENCE.md`
