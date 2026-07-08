---
id: UDG@20.15.2@MMLCommand@DSP FABRICTRUNKSTATIS
type: MMLCommand
name: DSP FABRICTRUNKSTATIS（显示Fabric-Trunk成员接口统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FABRICTRUNKSTATIS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP Fabric链路管理
- Fabric-Trunk成员接口统计
status: active
---

# DSP FABRICTRUNKSTATIS（显示Fabric-Trunk成员接口统计）

## 功能

该命令用于显示NP卡Fabric-Trunk成员接口的详细统计信息，包含状态、流量速率和带宽使用率等信息。

## 注意事项

该命令仅适用于非NP卡基础上扩容NP卡的异构场景，在纯NP场景该命令不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRUNKNAME | Fabric-Trunk接口名称 | 可选必选说明：可选参数。<br>参数含义：该参数是Fabric-Trunk接口的名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>配置原则：无。<br>默认值：无。 |

## 操作的配置对象

- [Fabric-Trunk成员接口统计（FABRICTRUNKSTATIS）](configobject/UDG/20.15.2/FABRICTRUNKSTATIS.md)

## 使用实例

查询所有的Fabric-Trunk成员接口统计信息：

```
%%DSP FABRICTRUNKSTATIS:;%%
RETCODE = 0  操作成功

结果如下
--------
Fabric-Trunk 接口名称  框号  槽位号  端口号  物理状态            链路状态    发送流量速率  接收流量速率  发送带宽使用率  接收带宽使用率

Fabric-Trunk19         1     3       3       Physical Status Up  NP_LINK_UP  865344        4072632       9               5             
Fabric-Trunk20         1     4       3       Physical Status Up  NP_LINK_UP  4788720       8596600       9               5             
(结果数量 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示Fabric-Trunk成员接口统计（DSP-FABRICTRUNKSTATIS）_85021296.md`
