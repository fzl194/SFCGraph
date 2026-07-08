---
id: UNC@20.15.2@MMLCommand@RMV OSPFV3AREA
type: MMLCommand
name: RMV OSPFV3AREA（删除OSPFv3区域配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPFV3AREA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3区域配置
status: active
---

# RMV OSPFV3AREA（删除OSPFv3区域配置）

## 功能

该命令用于在OSPFv3进程下删除区域。

![](删除OSPFv3区域配置（RMV OSPFV3AREA）_49801530.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该操作会删除OSPFv3区域相关的配置。

## 注意事项

- 该命令执行后立即生效。
- 删除OSPFv3区域可能会导致业务受损。
- 删除区域前应该先删除本区域下的相关配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。 |
| AREAID | OSPFv3区域标识 | 可选必选说明：必选参数<br>参数含义：OSPFv3区域标识。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：OSPFv3区域必须已经存在。 |

## 操作的配置对象

- [OSPFv3区域配置（OSPFV3AREA）](configobject/UNC/20.15.2/OSPFV3AREA.md)

## 使用实例

删除OSPFv3进程下1区域0.0.0.0：

```
RMV OSPFV3AREA: PROCID=1, AREAID="0.0.0.0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除OSPFv3区域配置（RMV-OSPFV3AREA）_49801530.md`
