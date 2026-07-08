---
id: UNC@20.15.2@MMLCommand@LST QOSRDRWLRFLOW
type: MMLCommand
name: LST QOSRDRWLRFLOW（查询WLR引流重定向）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSRDRWLRFLOW
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重定向WLR业务流
status: active
---

# LST QOSRDRWLRFLOW（查询WLR引流重定向）

## 功能

该命令用于查询所有配置了WLR引流重定向的接口。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| IPVERSION | IP协议版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口重定向引流使能的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4类型。<br>- ipv6：IPv6类型。<br>默认值：ipv4 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSRDRWLRFLOW]] · WLR引流重定向（QOSRDRWLRFLOW）

## 使用实例

查询所有配置了WLR引流重定向的接口：

```
LST QOSRDRWLRFLOW:;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
   接口名称             IP协议版本
   Ethernet66/0/3       IPv4
   (结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSRDRWLRFLOW.md`
