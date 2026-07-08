---
id: UDG@20.15.2@MMLCommand@LST OSPFNEXTHOP
type: MMLCommand
name: LST OSPFNEXTHOP（查询OSPF等价路由优先级配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFNEXTHOP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF等价路由优先级配置
status: active
---

# LST OSPFNEXTHOP（查询OSPF等价路由优先级配置）

## 功能

该命令用于查询OSPF等价路由优先级配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| NBRIPADDRESS | 下一跳IP地址 | 可选必选说明：可选参数<br>参数含义：下一跳IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFNEXTHOP]] · OSPF等价路由优先级配置（OSPFNEXTHOP）

## 使用实例

查询OSPF等价路由优先级配置：

```
LST OSPFNEXTHOP:;
```

```

RETCODE = 0  操作成功。

结果如下
-----------
      进程号  =  1
    拓扑标识  =  0
下一跳IP地址  =  10.4.4.4
  下一跳权重  =  10
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF等价路由优先级配置（LST-OSPFNEXTHOP）_00841773.md`
