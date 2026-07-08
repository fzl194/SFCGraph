---
id: UDG@20.15.2@MMLCommand@LST OSPFFRR
type: MMLCommand
name: LST OSPFFRR（查询OSPF IP FRR配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFFRR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF的FRR配置
status: active
---

# LST OSPFFRR（查询OSPF IP FRR配置）

## 功能

该命令用于查询OSPF IP FRR（快速重路由）配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [OSPF IP FRR配置（OSPFFRR）](configobject/UDG/20.15.2/OSPFFRR.md)

## 使用实例

查询OSPF进程号为1的IP FRR（快速重路由）配置信息：

```
LST OSPFFRR: PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                  OSPF进程号  =  1
                 LFA是否使能  =  FALSE
              节点保护优先级  =  40
          最小开销路径优先级  =  20
   LDP联动最大开销路径优先级  =  10
                路由策略类型  =  无策略
                路由策略名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF-IP-FRR配置（LST-OSPFFRR）_00866329.md`
