---
id: UDG@20.15.2@MMLCommand@LST OSPFV3AREA
type: MMLCommand
name: LST OSPFV3AREA（查询OSPFv3区域配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFV3AREA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3区域配置
status: active
---

# LST OSPFV3AREA（查询OSPFv3区域配置）

## 功能

该命令用于查询OSPFv3区域配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域标识 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域标识。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFV3AREA]] · OSPFv3区域配置（OSPFV3AREA）

## 使用实例

查询OSPFv3区域配置：

```
LST OSPFV3AREA:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                              OSPFv3进程号  =  1
                            OSPFv3区域标识  =  0.0.0.0
                            OSPFv3区域描述  =  NULL
                            OSPFv3区域类型  =  普通区域
        禁止ABR向Stub区域内发送Summary LSA  =  FALSE
 发送到Stub或NSSA区域的Type3缺省路由的开销  =  1
                              IPsec SA名称  =  NULL
                  产生缺省7类LSA到NSSA区域  =  FALSE
                            指定缺省开销值  =  FALSE
                                缺省开销值  =  1
                       指定缺省路由的tag值  =  FALSE
                           缺省路由的tag值  =  0
                        指定缺省路由的类型  =  FALSE
                              缺省路由类型  =  Type2
                            不引入外部路由  =  FALSE
        禁止ABR向NSSA区域内发送Summary LSA  =  FALSE
                     在DD报文中配置N-bit位  =  FALSE
                          指定为转换路由器  =  FALSE
                 转换路由器的失效时间（s）  =  40
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPFv3区域配置（LST-OSPFV3AREA）_49961798.md`
