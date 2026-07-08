---
id: UNC@20.15.2@MMLCommand@DSP WLRPAEG
type: MMLCommand
name: DSP WLRPAEG（显示PAEG信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: WLRPAEG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由相关信息
status: active
---

# DSP WLRPAEG（显示PAEG信息）

## 功能

该命令用于显示PAEG信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

## 操作的配置对象

- [PAEG信息（WLRPAEG）](configobject/UNC/20.15.2/WLRPAEG.md)

## 使用实例

显示PAEG信息：

```
DSP WLRPAEG:ADDRESSFAMILY=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
用户ID     Peer地址        地址族            PAEG IID    PAE GROUPID    TB high    TB low    TP    版本号
1000       10.1.1.100       IPv4单播          1           2              0          64        0     1
1000       10.1.1.100       IPv4单播          1           2              0          65        0     1
1000       10.1.1.100       IPv4单播          1           2              0          66        0     1
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示PAEG信息（DSP-WLRPAEG）_50121310.md`
