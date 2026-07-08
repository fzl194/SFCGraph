---
id: UDG@20.15.2@MMLCommand@DSP VPNINSTINTF
type: MMLCommand
name: DSP VPNINSTINTF（查询VPN实例接口信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: VPNINSTINTF
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- L3VPN管理
- VPN实例接口
status: active
---

# DSP VPNINSTINTF（查询VPN实例接口信息）

## 功能

该命令用于查询VPN实例接口信息。

## 注意事项

- 该命令执行后立即生效。
- 此命令最多查询1000个VPN实例，且每个VPN实例最多显示5个接口名，超出则显示“……”。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VPNINSTINTF]] · VPN实例接口信息（VPNINSTINTF）

## 使用实例

查询VPN实例接口信息：

```
DSP VPNINSTINTF: VRFNAME="__mpp_vpn_inner__";
```

```

RETCODE = 0 操作成功。

结果如下
------------------------
VPN实例接口信息 =
VPN-Instance Name : __mpp_vpn_inner__
VPN-Instance ID : 1
Interface Number : 1
Interface list : GigabitEthernet0/0/1

(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-VPNINSTINTF.md`
