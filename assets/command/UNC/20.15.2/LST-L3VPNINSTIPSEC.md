---
id: UNC@20.15.2@MMLCommand@LST L3VPNINSTIPSEC
type: MMLCommand
name: LST L3VPNINSTIPSEC（查询L3VPN实例）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: L3VPNINSTIPSEC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- VPN管理
- L3VPN管理
- L3VPN实例配置命令
status: active
---

# LST L3VPNINSTIPSEC（查询L3VPN实例）

## 功能

该命令用于查询已配置的L3VPN实例名称。

## 注意事项

不指定参数，则显示设备上所有已配置的VPN实例名称。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户需要增加的L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>不支持空格。 |

## 操作的配置对象

- [L3VPN实例（L3VPNINSTIPSEC）](configobject/UNC/20.15.2/L3VPNINSTIPSEC.md)

## 使用实例

查询所有VPN实例，其中VPN实例_public_为公网实例，表示相对于私网的公网概念：

```
LST L3VPNINSTIPSEC:;

RETCODE = 0  操作成功。

        结果如下
        -------------------------
        VPN实例名称   
        _public_                      
        vrf1               
        (结果个数 = 2)
         ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询L3VPN实例（LST-L3VPNINSTIPSEC）_25912249.md`
