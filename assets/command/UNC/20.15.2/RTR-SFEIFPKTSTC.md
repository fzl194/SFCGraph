---
id: UNC@20.15.2@MMLCommand@RTR SFEIFPKTSTC
type: MMLCommand
name: RTR SFEIFPKTSTC（清除SFE接口报文统计）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: SFEIFPKTSTC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE接口统计信息
status: active
---

# RTR SFEIFPKTSTC（清除SFE接口报文统计）

## 功能

该命令用来清除SFE指定接口心跳报文及二层透传报文统计。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待查询的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [SFE接口报文统计（SFEIFPKTSTC）](configobject/UNC/20.15.2/SFEIFPKTSTC.md)

## 使用实例

清除指定接口的SFE心跳报文及二层透传报文统计：

```
RTR SFEIFPKTSTC:IFNAME="Ethernet66/0/3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除SFE接口报文统计（RTR-SFEIFPKTSTC）_00865645.md`
