---
id: UDG@20.15.2@MMLCommand@LST OSPFV3IMPORTROUTE
type: MMLCommand
name: LST OSPFV3IMPORTROUTE（查询OSPFv3引入路由配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFV3IMPORTROUTE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3引入路由配置
status: active
---

# LST OSPFV3IMPORTROUTE（查询OSPFv3引入路由配置）

## 功能

该命令用于查询OSPFv3引入路由配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| PROTOCOL | 协议号 | 可选必选说明：可选参数<br>参数含义：协议号。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- direct：直连路由。<br>- static：静态路由。<br>- bgp：BGP协议。<br>- ospfv3：OSPFv3协议。<br>- wlr：无线路由。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3引入路由配置（OSPFV3IMPORTROUTE）](configobject/UDG/20.15.2/OSPFV3IMPORTROUTE.md)

## 使用实例

查询OSPFv3引入路由配置：

```
LST OSPFV3IMPORTROUTE:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                    OSPFv3进程号  =  1
                        拓扑标识  =  0
                          协议号  =  WLR路由
                      协议进程号  =  1
              引入路由开销值配置  =  FALSE
                引入路由标签配置  =  FALSE
                引入路由类型配置  =  FALSE
                      路径Cost值  =  1
                            标签  =  1
                    引入路由类型  =  Type2
                    路由策略名称  =  NULL
                     允许BGP配置  =  FALSE
指定引入路由时继承原路由的开销值  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPFv3引入路由配置（LST-OSPFV3IMPORTROUTE）_49961414.md`
