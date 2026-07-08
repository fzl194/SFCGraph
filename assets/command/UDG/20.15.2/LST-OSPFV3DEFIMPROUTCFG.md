---
id: UDG@20.15.2@MMLCommand@LST OSPFV3DEFIMPROUTCFG
type: MMLCommand
name: LST OSPFV3DEFIMPROUTCFG（显示OSPFv3引入路由默认配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFV3DEFIMPROUTCFG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3引入路由默认配置
status: active
---

# LST OSPFV3DEFIMPROUTCFG（显示OSPFv3引入路由默认配置）

## 功能

该命令用于查询OSPFv3引入路由默认配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3引入路由默认配置（OSPFV3DEFIMPROUTCFG）](configobject/UDG/20.15.2/OSPFV3DEFIMPROUTCFG.md)

## 使用实例

显示OSPFv3进程1下引入路由默认配置：

```
LST OSPFV3DEFIMPROUTCFG:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                      OSPFv3进程号  =  1
                          拓扑标识  =  0
                  等价路由最大数量  =  64
                        默认开销值  =  1
引入路由的开销值为路由自带的cost值  =  FALSE
                    外部路由的标记  =  1
                      外部路由类型  =  Type2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示OSPFv3引入路由默认配置（LST-OSPFV3DEFIMPROUTCFG）_00440297.md`
