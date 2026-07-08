---
id: UNC@20.15.2@MMLCommand@LST PREFIXLIMIT
type: MMLCommand
name: LST PREFIXLIMIT（查询前缀限制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PREFIXLIMIT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由基础
- 路由管控功能列表
status: active
---

# LST PREFIXLIMIT（查询前缀限制）

## 功能

该命令用于查看当前配置的前缀限制情况。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：默认查询所有VPN。 |
| AFTYPE | 地址族 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址族类型。支持IPv4和IPv6单播地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无<br>配置原则：默认查询IPv4和IPv6单播地址族。 |

## 操作的配置对象

- [前缀限制（PREFIXLIMIT）](configobject/UNC/20.15.2/PREFIXLIMIT.md)

## 使用实例

查询IPv4前缀限制情况：

```
LST PREFIXLIMIT: AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
地址族      最大路由前缀数  是否只是生成告警 VPN实例名称       告警阈值           是否保留路由表
IPv4单播    0               FALSE            _public_          NULL               FALSE
IPv4单播    0               FALSE            __mpp_vpn_inner__ NULL               FALSE
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询前缀限制（LST-PREFIXLIMIT）_50281698.md`
