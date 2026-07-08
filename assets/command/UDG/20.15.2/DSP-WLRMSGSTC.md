---
id: UDG@20.15.2@MMLCommand@DSP WLRMSGSTC
type: MMLCommand
name: DSP WLRMSGSTC（显示WLR与各Partner的消息统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRMSGSTC
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

# DSP WLRMSGSTC（显示WLR与各Partner的消息统计）

## 功能

该命令用于显示WLR与各Partner的消息统计。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

## 操作的配置对象

- [WLR与各Partner的消息统计（WLRMSGSTC）](configobject/UDG/20.15.2/WLRMSGSTC.md)

## 使用实例

显示WLR与各Partner的消息统计：

```
DSP WLRMSGSTC:ADDRESSFAMILY=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
Partner ID  接收的数目       丢弃的数目  发送的数目   发送失败数目 重传的数目    序列号异常数目     被流控次数      流控状态

0x6A0015      8                0          183           0             0               0             0                FALSE
0x710009      10               0          67            0             0               0             0                FALSE
0x790011      5                0          3             0             0               0             0                FALSE
0x7F0012      2                0          2             0             0               0             0                FALSE
0x7F0019      1                0          1             0             0               0             0                FALSE
0x1DB0002     19               0          20            0             0               0             0                FALSE
0x2DE0001     2                0          2             0             0               0             0                FALSE
(结果个数 = 7)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示WLR与各Partner的消息统计（DSP-WLRMSGSTC）_00841049.md`
