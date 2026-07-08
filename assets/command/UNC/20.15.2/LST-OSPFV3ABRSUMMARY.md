---
id: UNC@20.15.2@MMLCommand@LST OSPFV3ABRSUMMARY
type: MMLCommand
name: LST OSPFV3ABRSUMMARY（显示OSPFv3区域内路由聚合配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFV3ABRSUMMARY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3区域内路由聚合配置
status: active
---

# LST OSPFV3ABRSUMMARY（显示OSPFv3区域内路由聚合配置）

## 功能

该命令用于查询OSPFv3区域内路由聚合。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。 |
| AREAID | OSPFv3区域ID | 可选必选说明：可选参数<br>参数含义：OSPFv3区域ID。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IPADDRESS | IPv6地址 | 可选必选说明：可选参数<br>参数含义：IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| IPV6MASKLEN | IPv6前缀长度 | 可选必选说明：可选参数<br>参数含义：IPv6前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3区域内路由聚合配置（OSPFV3ABRSUMMARY）](configobject/UNC/20.15.2/OSPFV3ABRSUMMARY.md)

## 使用实例

显示OSPFv3区域内路由聚合配置：

```
LST OSPFV3ABRSUMMARY:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------
      OSPFv3进程号  =  1
      OSPFv3区域ID  =  0.0.0.1
          拓扑标识  =  0
          IPv6地址  =  2001:db8::1
      IPv6前缀长度  =  64
      发布路由标识  =  TRUE
      使能开销配置  =  TRUE
    聚合路由的开销  =  100
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示OSPFv3区域内路由聚合配置（LST-OSPFV3ABRSUMMARY）_00840513.md`
