---
id: UNC@20.15.2@MMLCommand@LST OSPFV3DEFAULTROUTE
type: MMLCommand
name: LST OSPFV3DEFAULTROUTE（查询OSPFv3默认路由宣告配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFV3DEFAULTROUTE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3默认路由宣告配置
status: active
---

# LST OSPFV3DEFAULTROUTE（查询OSPFv3默认路由宣告配置）

## 功能

该命令用于查询OSPFv3默认路由宣告配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFV3DEFAULTROUTE]] · OSPFv3默认路由宣告配置（OSPFV3DEFAULTROUTE）

## 使用实例

查询OSPFv3默认路由宣告配置：

```
LST OSPFV3DEFAULTROUTE:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
              OSPFv3进程号  =  1
                  拓扑标识  =  0
                  使能度量  =  TRUE
             外部LSA开销值  =  100
          缺省路由使能类型  =  FALSE
          引入外部路由类型  =  Type2
延迟发布缺省路由的时间（s） =  NULL
          默认路由发布标志  =  默认路由宣告
              计算默认路由  =  FALSE
                  路由策略  =  NULL
          缺省路由使能标签  =  TRUE
                  路由标签  =  10
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OSPFV3DEFAULTROUTE.md`
