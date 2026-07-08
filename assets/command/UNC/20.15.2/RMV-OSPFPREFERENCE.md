---
id: UNC@20.15.2@MMLCommand@RMV OSPFPREFERENCE
type: MMLCommand
name: RMV OSPFPREFERENCE（删除OSPF协议路由的优先级配置）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV OSPFPREFERENCE（删除OSPF协议路由的优先级配置）

## 功能

该命令用于恢复OSPF协议路由的优先级默认配置。

## 注意事项

- 该命令执行后立即生效。
- 当前OSPF路由优先级的两种路由类型ASE和default不支持删除操作。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| ROUTETYPE | 路由类型 | 可选必选说明：必选参数<br>参数含义：路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- default：区域内和区域间路由。<br>- ase：AS-External路由。<br>- intra：区域内路由。<br>- inter：区域间路由。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFPREFERENCE]] · OSPF协议路由的优先级配置（OSPFPREFERENCE）

## 使用实例

恢复OSPF进程1的区域内路由的默认优先级：

```
RMV OSPFPREFERENCE:PROCID=1,TOPOID=0,ROUTETYPE=intra;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-OSPFPREFERENCE.md`
