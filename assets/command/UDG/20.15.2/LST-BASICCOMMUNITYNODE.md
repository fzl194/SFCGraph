---
id: UDG@20.15.2@MMLCommand@LST BASICCOMMUNITYNODE
type: MMLCommand
name: LST BASICCOMMUNITYNODE（查询基础团体属性过滤器节点）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BASICCOMMUNITYNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 基础团体属性过滤器节点
status: active
---

# LST BASICCOMMUNITYNODE（查询基础团体属性过滤器节点）

## 功能

该命令用于列出基础团体属性过滤器节点。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMNTYNAMEORNUM | 团体属性过滤器名字或号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性过滤器名字或团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BASICCOMMUNITYNODE]] · 基础团体属性过滤器节点（BASICCOMMUNITYNODE）

## 使用实例

查询基本团体属性过滤器：

```
LST BASICCOMMUNITYNODE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
    团体属性过滤器节点ID  =  10
  团体属性过滤器名字或号  =  1
                匹配模式  =  允许
                 字符串1  =  2:2
                 字符串2  =  NULL
                 字符串3  =  NULL
                 字符串4  =  NULL
                 字符串5  =  NULL
                 字符串6  =  NULL
                 字符串7  =  NULL
                 字符串8  =  NULL
                 字符串9  =  NULL
                字符串10  =  NULL
                字符串11  =  NULL
                字符串12  =  NULL
                字符串13  =  NULL
                字符串14  =  NULL
                字符串15  =  NULL
                字符串16  =  NULL
                字符串17  =  NULL
                字符串18  =  NULL
                字符串19  =  NULL
                字符串20  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-BASICCOMMUNITYNODE.md`
