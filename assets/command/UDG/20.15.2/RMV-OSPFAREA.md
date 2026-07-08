---
id: UDG@20.15.2@MMLCommand@RMV OSPFAREA
type: MMLCommand
name: RMV OSPFAREA（删除OSPF区域配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFAREA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF区域配置
status: active
---

# RMV OSPFAREA（删除OSPF区域配置）

## 功能

该命令用于在OSPF进程下删除区域。

## 注意事项

- 该命令执行后立即生效。
- 删除区域前应该先删除本区域下的相关配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域号 | 可选必选说明：必选参数<br>参数含义：OSPF区域号。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [OSPF区域配置（OSPFAREA）](configobject/UDG/20.15.2/OSPFAREA.md)

## 使用实例

删除OSPF进程下1区域0.0.0.0：

```
RMV OSPFAREA: PROCID=1, AREAID="0.0.0.0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除OSPF区域配置（RMV-OSPFAREA）_49961418.md`
