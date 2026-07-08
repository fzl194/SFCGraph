---
id: UDG@20.15.2@MMLCommand@LST EXTENDCOMMUNITYFILTER
type: MMLCommand
name: LST EXTENDCOMMUNITYFILTER（查询扩展团体属性过滤器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: EXTENDCOMMUNITYFILTER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 扩展团体属性过滤器
status: active
---

# LST EXTENDCOMMUNITYFILTER（查询扩展团体属性过滤器）

## 功能

该命令用于列出扩展团体属性过滤器。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 扩展团体属性过滤器名字或号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展团体属性过滤器名字或扩展团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，扩展团体属性过滤器名称其长度范围是1～51。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXTENDCOMMUNITYFILTER]] · 扩展团体属性过滤器（EXTENDCOMMUNITYFILTER）

## 使用实例

查询扩展团体属性过滤器：

```
LST EXTENDCOMMUNITYFILTER:;
```

```

RETCODE = 0  操作成功

结果如下
--------
扩展团体属性过滤器名字或号    过滤器类型

200                          高级
a                            基础
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询扩展团体属性过滤器（LST-EXTENDCOMMUNITYFILTER）_00840777.md`
