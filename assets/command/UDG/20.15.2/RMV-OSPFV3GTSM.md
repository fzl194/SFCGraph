---
id: UDG@20.15.2@MMLCommand@RMV OSPFV3GTSM
type: MMLCommand
name: RMV OSPFV3GTSM（删除OSPFv3 GTSM配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFV3GTSM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3 GTSM功能配置
status: active
---

# RMV OSPFV3GTSM（删除OSPFv3 GTSM配置）

## 功能

该命令用于用来去使能OSPFv3 GTSM特性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名 | 可选必选说明：必选参数<br>参数含义：VPN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：默认为公网配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFV3GTSM]] · OSPFv3 GTSM配置（OSPFV3GTSM）

## 使用实例

去使能OSPFv3 GTSM功能：

```
RMV OSPFV3GTSM:VRFNAME="abc";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-OSPFV3GTSM.md`
