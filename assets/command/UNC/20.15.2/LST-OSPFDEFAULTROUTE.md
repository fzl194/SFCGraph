---
id: UNC@20.15.2@MMLCommand@LST OSPFDEFAULTROUTE
type: MMLCommand
name: LST OSPFDEFAULTROUTE（查询OSPF默认宣告路由配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFDEFAULTROUTE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF默认宣告路由配置
status: active
---

# LST OSPFDEFAULTROUTE（查询OSPF默认宣告路由配置）

## 功能

该命令用于查询OSPF默认宣告路由配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFDEFAULTROUTE]] · OSPF默认宣告路由配置（OSPFDEFAULTROUTE）

## 使用实例

查询OSPF默认宣告路由配置：

```
LST OSPFDEFAULTROUTE:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                    进程号  =  1
                  拓扑标识  =  0
             外部LSA开销值  =  100
          引入外部路由类型  =  Type2
                  使能度量  =  TRUE
          缺省路由使能类型  =  FALSE
延迟发布聚合路由的时间（s） =  NULL
          默认路由发布标志  =  默认路由宣告
              计算默认路由  =  FALSE
                  路由策略  =  RtPolicy
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OSPFDEFAULTROUTE.md`
