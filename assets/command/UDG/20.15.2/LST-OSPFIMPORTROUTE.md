---
id: UDG@20.15.2@MMLCommand@LST OSPFIMPORTROUTE
type: MMLCommand
name: LST OSPFIMPORTROUTE（查询OSPF引入路由配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFIMPORTROUTE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 引入外部路由配置
status: active
---

# LST OSPFIMPORTROUTE（查询OSPF引入路由配置）

## 功能

该命令用于查询OSPF引入路由配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| PROTOCOL | 协议分类 | 可选必选说明：可选参数<br>参数含义：用于指定OSPF引入外部路由的路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Direct：直连路由。<br>- OSPF：OSPF路由。<br>- Static：静态路由。<br>- BGP：BGP路由。<br>- wlr：无线路由。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFIMPORTROUTE]] · OSPF引入路由配置（OSPFIMPORTROUTE）

## 使用实例

查询OSPF引入路由配置：

```
LST OSPFIMPORTROUTE:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
        OSPF进程号  =  1
          拓扑标识  =  0
          协议分类  =  静态路由
        协议进程号  =  1
引入路由开销值配置  =  TRUE
  引入路由标签配置  =  TRUE
  引入路由类型配置  =  TRUE
        路径Cost值  =  10
              标签  =  10
      引入路由类型  =  1
      路由策略名称  =  NULL
       允许BGP配置  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF引入路由配置（LST-OSPFIMPORTROUTE）_00441505.md`
