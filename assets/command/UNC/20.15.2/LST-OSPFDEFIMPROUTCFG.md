---
id: UNC@20.15.2@MMLCommand@LST OSPFDEFIMPROUTCFG
type: MMLCommand
name: LST OSPFDEFIMPROUTCFG（查询OSPF引入路由默认配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFDEFIMPROUTCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 设置OSPF引入路由默认配置
status: active
---

# LST OSPFDEFIMPROUTCFG（查询OSPF引入路由默认配置）

## 功能

该命令用于查询OSPF引入路由默认配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFDEFIMPROUTCFG]] · OSPF引入路由默认配置（OSPFDEFIMPROUTCFG）

## 使用实例

查询OSPF引入路由默认配置：

```
LST OSPFDEFIMPROUTCFG:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                            进程号  =  1
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

- 原始手册：`evidence/UNC/20.15.2/查询OSPF引入路由默认配置（LST-OSPFDEFIMPROUTCFG）_49801726.md`
