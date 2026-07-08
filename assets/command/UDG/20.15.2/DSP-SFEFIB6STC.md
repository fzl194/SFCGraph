---
id: UDG@20.15.2@MMLCommand@DSP SFEFIB6STC
type: MMLCommand
name: DSP SFEFIB6STC（查询IPv6指定的VPN路由表项统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFEFIB6STC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FIB表项统计
status: active
---

# DSP SFEFIB6STC（查询IPv6指定的VPN路由表项统计）

## 功能

该命令用于查询IPv6指定的VPN路由表项统计。FIB6用于保存报文转发信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称，可使用命令DSP RU查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFEFIB6STC]] · IPv6指定的VPN路由表项统计（SFEFIB6STC）

## 使用实例

查询IPv6指定的VPN路由表项统计：

```
DSP SFEFIB6STC : RUNAME="VNODE_VNRS_VNFC_IPU_0066", VPNNAME="_public_";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
             VPN名称  =  _public_
全部使用FIB6表项总数  =  4
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPv6指定的VPN路由表项统计（DSP-SFEFIB6STC）_49962058.md`
