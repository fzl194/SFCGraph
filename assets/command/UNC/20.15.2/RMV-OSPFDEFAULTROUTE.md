---
id: UNC@20.15.2@MMLCommand@RMV OSPFDEFAULTROUTE
type: MMLCommand
name: RMV OSPFDEFAULTROUTE（删除OSPF默认宣告路由配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPFDEFAULTROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF默认宣告路由配置
status: active
---

# RMV OSPFDEFAULTROUTE（删除OSPF默认宣告路由配置）

## 功能

该命令用于取消缺省路由通告到普通OSPF区域。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFDEFAULTROUTE]] · OSPF默认宣告路由配置（OSPFDEFAULTROUTE）

## 使用实例

取消缺省路由通告到普通OSPF进程1区域：

```
RMV OSPFDEFAULTROUTE:PROCID=1,TOPOID=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除OSPF默认宣告路由配置（RMV-OSPFDEFAULTROUTE）_50281658.md`
