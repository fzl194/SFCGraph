---
id: UNC@20.15.2@MMLCommand@RMV TRUNKMEMBER
type: MMLCommand
name: RMV TRUNKMEMBER（删除Trunk成员接口）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TRUNKMEMBER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- Trunk成员接口配置
status: active
---

# RMV TRUNKMEMBER（删除Trunk成员接口）

## 功能

该命令用于删除Trunk成员接口。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后可能影响业务，请谨慎使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRUNKIFNAME | Trunk接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置Trunk接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无 |
| MEMBERIFNAME | 成员接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置成员接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRUNKMEMBER]] · Trunk成员接口（TRUNKMEMBER）

## 使用实例

删除Eth-Trunk1的成员接口Ethernet64/0/3：

```
RMV TRUNKMEMBER: TRUNKIFNAME="Eth-Trunk1", MEMBERIFNAME="Ethernet64/0/3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Trunk成员接口（RMV-TRUNKMEMBER）_49962066.md`
