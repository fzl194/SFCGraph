---
id: UDG@20.15.2@MMLCommand@DSP SFEIFPKTSTC
type: MMLCommand
name: DSP SFEIFPKTSTC（显示SFE接口报文统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFEIFPKTSTC
command_category: 查询类
effect_mode: ''
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

# DSP SFEIFPKTSTC（显示SFE接口报文统计）

## 功能

该命令用来查询SFE指定接口心跳报文及二层透传报文统计。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [SFE接口报文统计（SFEIFPKTSTC）](configobject/UDG/20.15.2/SFEIFPKTSTC.md)

## 使用实例

查询指定接口的SFE心跳报文及二层透传报文统计：

```
DSP SFEIFPKTSTC:IFNAME="Ethernet66/0/3";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
报文类型           接收报文个数             发送报文个数

心跳报文            0                        0                 
L2-ip2cslb         0                        0                 
L2-cslb2ip         0                        0                 
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示SFE接口报文统计（DSP-SFEIFPKTSTC）_50120638.md`
