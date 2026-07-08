---
id: UDG@20.15.2@MMLCommand@LST OSPFAREA
type: MMLCommand
name: LST OSPFAREA（查询OSPF区域配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFAREA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF区域配置
status: active
---

# LST OSPFAREA（查询OSPF区域配置）

## 功能

该命令用于查询在OSPF进程下区域配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域号 | 可选必选说明：可选参数<br>参数含义：OSPF区域号。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：规划的邻居所在的区域必须一致。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFAREA]] · OSPF区域配置（OSPFAREA）

## 使用实例

查询在OSPF进程下区域配置：

```
LST OSPFAREA:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                                    进程号  =  1
                                    区域号  =  0.0.0.0
                                  区域描述  =  NULL
                                  区域类型  =  普通区域
                  产生缺省7类LSA到NSSA区域  =  FALSE
                            不引入外部路由  =  FALSE
        禁止ABR向NSSA区域内发送Summary LSA  =  FALSE
                               配置N-bit位  =  FALSE
    转换后生成的Type5 LSA的FA配置为0.0.0.0  =  FALSE
                                转换路由器  =  FALSE
                              失效时间（s） =  40
          将生成的Type7 LSA的FA置为0.0.0.0  =  FALSE
        禁止ABR向Stub区域内发送Summary LSA  =  FALSE
 发送到Stub或NSSA区域的Type3缺省路由的开销  =  1
                     使能LDP和OSPF同步功能  =  TRUE
                        保持最大开销值标志  =  TRUE
                保持最大开销值时间间隔（s） =  800
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF区域配置（LST-OSPFAREA）_49801990.md`
