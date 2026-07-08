---
id: UDG@20.15.2@MMLCommand@DSP WLRTBLSTAT
type: MMLCommand
name: DSP WLRTBLSTAT（查询基于表无线路由数据信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRTBLSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由统计信息
status: active
---

# DSP WLRTBLSTAT（查询基于表无线路由数据信息）

## 功能

该命令用于查询基于表无线路由数据信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：_public_ |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

## 操作的配置对象

- [基于表无线路由数据信息（WLRTBLSTAT）](configobject/UDG/20.15.2/WLRTBLSTAT.md)

## 使用实例

查询基于表无线路由数据信息：

```
DSP WLRTBLSTAT:AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
VPN实例名称    数据类型    总数    活跃数    添加数    删除数    更新数
_public_       Prefix      1       1         1         0         0
_public_       IID         0       0         1         0         0
_public_       Route       1       1         NULL      NULL      NULL
_public_       Attr        0       0         1         0         0
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询基于表无线路由数据信息（DSP-WLRTBLSTAT）_00600917.md`
