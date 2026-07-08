---
id: UNC@20.15.2@MMLCommand@RMV OSPFDNSUMRTID
type: MMLCommand
name: RMV OSPFDNSUMRTID（删除特定路由器禁止检查Summary-LSA的DN比特位配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPFDNSUMRTID
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF特定路由器禁止检查Summary-LSA的DN比特位配置
status: active
---

# RMV OSPFDNSUMRTID（删除特定路由器禁止检查Summary-LSA的DN比特位配置）

## 功能

该命令用于恢复特定路由器对Summary LSA的DN位检查的默认配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| ROUTERID | 路由器标识 | 可选必选说明：必选参数<br>参数含义：路由器标识。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFDNSUMRTID]] · 创建特定路由器禁止检查Summary-LSA的DN比特位配置（OSPFDNSUMRTID）

## 使用实例

恢复10.2.2.2路由器对Summary LSA的DN位检查的默认配置：

```
RMV OSPFDNSUMRTID:PROCID=1,ROUTERID="10.2.2.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-OSPFDNSUMRTID.md`
