---
id: UDG@20.15.2@MMLCommand@LST L3VPNINST
type: MMLCommand
name: LST L3VPNINST（查询L3VPN实例）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: L3VPNINST
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- L3VPN管理
- L3VPN实例
status: active
---

# LST L3VPNINST（查询L3VPN实例）

## 功能

该命令用于查询已配置的L3VPN实例信息。

## 注意事项

- 该命令执行后立即生效。
- 不指定参数，则显示设备上所有已配置的VPN实例名称。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L3VPNINST]] · L3VPN实例（L3VPNINST）

## 使用实例

查询所有VPN实例，其中VPN实例_public_为公网实例：

```
LST L3VPNINST:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
VPN实例名称          VPN实例描述     路由器ID
_public_             NULL            NULL
__mpp_vpn_inner__    NULL            NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询L3VPN实例（LST-L3VPNINST）_49961238.md`
