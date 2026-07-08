---
id: UNC@20.15.2@MMLCommand@DSP RMSMOOTHSTC
type: MMLCommand
name: DSP RMSMOOTHSTC（查询路由管理平滑统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RMSMOOTHSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 路由基础调测
- 查询路由管理统计信息
status: active
---

# DSP RMSMOOTHSTC（查询路由管理平滑统计信息）

## 功能

该命令用来查询路由管理平滑统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示路由所属VPN的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RMSMOOTHSTC]] · 路由管理平滑统计信息（RMSMOOTHSTC）

## 使用实例

查询路由管理平滑统计信息：

```
DSP RMSMOOTHSTC:AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功。

结果如下
--------
Partner ID    总的平滑次数    拒绝的平滑次数    最后一次平滑开始的时间    最后一次平滑结束的时间

0x1           0               0                 NULL                      NULL
0x0           0               0                 NULL                      NULL
0x10004       0               0                 NULL                      NULL
0x4000B       0               0                 NULL                      NULL
0x260005      0               0                 NULL                      NULL
0x60000D      0               0                 NULL                      NULL
0x660014      0               0                 NULL                      NULL
0x670013      0               0                 NULL                      NULL
0x690029      0               0                 NULL                      NULL
0x6A0016      0               0                 NULL                      NULL
0x6F0005      1               0                 2016-11-11 07:40:55       2016-11-11 07:41:04
0x700007      1               0                 2016-11-11 07:40:55       2016-11-11 07:40:55
0x72000F      0               0                 NULL                      NULL
0x74001F      0               0                 NULL                      NULL
0x77000B      0               0                 NULL                      NULL
0x790012      0               0                 NULL                      NULL
0x7A0011      0               0                 NULL                      NULL
0x8C0017      0               0                 NULL                      NULL
0x8F0015      0               0                 NULL                      NULL
0x97001E      0               0                 NULL                      NULL
0xA60021      1               0                 2016-11-11 07:40:58       2016-11-11 07:40:58
0xB00022      1               0                 2016-11-11 07:40:58       2016-11-11 07:40:58
0xCA2712      0               0                 NULL                      NULL
0xD5000E      0               0                 NULL                      NULL
0xE7000C      0               0                 NULL                      NULL
0x1970020     0               0                 NULL                      NULL
0x1DA0003     1               0                 2016-11-11 07:40:55       2016-11-11 07:40:55
0x1DD000B     1               0                 2016-11-11 07:40:55       2016-11-11 07:41:04
0x208001B     0               0                 NULL                      NULL
0x2FB003C     0               0                 NULL                      NULL
0x3DD000A     0               0                 NULL                      NULL
0x404001A     0               0                 NULL                      NULL
0xBEF001D     0               0                 NULL                      NULL
0xBF1001C     0               0                 NULL                      NULL
(结果个数 = 34)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RMSMOOTHSTC.md`
