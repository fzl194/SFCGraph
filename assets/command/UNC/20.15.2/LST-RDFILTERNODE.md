---
id: UNC@20.15.2@MMLCommand@LST RDFILTERNODE
type: MMLCommand
name: LST RDFILTERNODE（查询RD路由过滤节点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RDFILTERNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- RD路由过滤节点
status: active
---

# LST RDFILTERNODE（查询RD路由过滤节点）

## 功能

该命令用来查询一个RD属性过滤器。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | RD过滤器索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RD过滤器索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1024。<br>默认值：无 |
| NODESEQUENCE | RD过滤索引节点号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RD过滤索引节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [RD路由过滤节点（RDFILTERNODE）](configobject/UNC/20.15.2/RDFILTERNODE.md)

## 使用实例

查询RD属性过滤器：

```
LST RDFILTERNODE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
    RD过滤器索引   =  1
RD过滤索引节点号   =  10
        匹配模式   =  拒绝
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RD路由过滤节点（LST-RDFILTERNODE）_50121262.md`
