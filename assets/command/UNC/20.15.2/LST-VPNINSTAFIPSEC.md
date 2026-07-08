---
id: UNC@20.15.2@MMLCommand@LST VPNINSTAFIPSEC
type: MMLCommand
name: LST VPNINSTAFIPSEC（查询L3VPN实例地址族）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VPNINSTAFIPSEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- VPN管理
- L3VPN管理
- VPN实例地址族配置命令
status: active
---

# LST VPNINSTAFIPSEC（查询L3VPN实例地址族）

## 功能

该命令用于查询设备上VPN实例下配置的地址族及参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [L3VPN实例地址族（VPNINSTAFIPSEC）](configobject/UNC/20.15.2/VPNINSTAFIPSEC.md)

## 使用实例

查询设备上所有VPN实例的地址族，其中VPN实例_public_为公网实例，表示相对于私网的公网概念：

```
LST VPNINSTAFIPSEC:;

 RETCODE = 0  操作成功。

        结果如下
        -------------------------
        VPN实例名称   vrf1    
        地址族类型  IPv4 address family                     
        (结果个数 = 1)
         ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询L3VPN实例地址族（LST-VPNINSTAFIPSEC）_26032197.md`
