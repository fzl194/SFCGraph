---
id: UDG@20.15.2@MMLCommand@LST ADVEXTCOMMUNITYNODE
type: MMLCommand
name: LST ADVEXTCOMMUNITYNODE（查询高级扩展团体属性过滤器节点）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ADVEXTCOMMUNITYNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 高级扩展团体属性过滤器节点
status: active
---

# LST ADVEXTCOMMUNITYNODE（查询高级扩展团体属性过滤器节点）

## 功能

该命令用于列出高级扩展团体属性过滤器节点。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAMEORNUM | 高级扩展团体属性过滤器名字或号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定高级扩展团体属性过滤器名字或高级扩展团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～51。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ADVEXTCOMMUNITYNODE]] · 高级扩展团体属性过滤器节点（ADVEXTCOMMUNITYNODE）

## 使用实例

查询高级扩展团体属性过滤器节点：

```
LST ADVEXTCOMMUNITYNODE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
高级扩展团体属性过滤器名字或号  =  aa
  高级扩展团体属性过滤器节点ID  =  10
                    正则表达式  =  1
                      匹配模式  =  拒绝
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ADVEXTCOMMUNITYNODE.md`
