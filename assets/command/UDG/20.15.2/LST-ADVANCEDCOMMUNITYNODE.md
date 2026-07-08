---
id: UDG@20.15.2@MMLCommand@LST ADVANCEDCOMMUNITYNODE
type: MMLCommand
name: LST ADVANCEDCOMMUNITYNODE（查询高级团体属性过滤器节点）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ADVANCEDCOMMUNITYNODE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 高级团体属性过滤器节点
status: active
---

# LST ADVANCEDCOMMUNITYNODE（查询高级团体属性过滤器节点）

## 功能

该命令用来查询高级团体属性过滤器节点。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMNTYNAMEORNUM | 团体属性过滤器名字或号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性过滤器名字或团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ADVANCEDCOMMUNITYNODE]] · 高级团体属性过滤器节点（ADVANCEDCOMMUNITYNODE）

## 使用实例

查询高级团体属性过滤器节点：

```
LST ADVANCEDCOMMUNITYNODE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
团体属性过滤器名字或号  =  a
  团体属性过滤器节点ID  =  10
            正则表达式  =  1
              匹配模式  =  拒绝
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ADVANCEDCOMMUNITYNODE.md`
