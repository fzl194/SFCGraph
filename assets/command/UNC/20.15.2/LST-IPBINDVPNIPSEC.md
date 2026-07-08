---
id: UNC@20.15.2@MMLCommand@LST IPBINDVPNIPSEC
type: MMLCommand
name: LST IPBINDVPNIPSEC（查询接口绑定VPN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPBINDVPNIPSEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- 接口管理
- 绑定VPN
status: active
---

# LST IPBINDVPNIPSEC（查询接口绑定VPN）

## 功能

该命令用于查询接口绑定VPN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：用于设置绑定VPN的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [接口绑定VPN（IPBINDVPNIPSEC）](configobject/UNC/20.15.2/IPBINDVPNIPSEC.md)

## 使用实例

查询接口绑定VPN：

```
LST IPBINDVPNIPSEC:IFNAME="Loopback1";

RETCODE = 0  操作成功。
  
结果如下
------------------------
          接口名  =  Loopback1
    IPv4地址  =  192.168.1.1
IPv4地址掩码  =  255.255.0.0
     VPN实例名称  =  vrf1
(结果个数 = 1)
--END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询接口绑定VPN（LST-IPBINDVPNIPSEC）_26032195.md`
