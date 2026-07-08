---
id: UNC@20.15.2@MMLCommand@LST MATCHEXTCOMMUNITYFILTER
type: MMLCommand
name: LST MATCHEXTCOMMUNITYFILTER（查询匹配扩展团体属性过滤器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MATCHEXTCOMMUNITYFILTER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配扩展团体属性过滤器
status: active
---

# LST MATCHEXTCOMMUNITYFILTER（查询匹配扩展团体属性过滤器）

## 功能

该命令用于列出匹配扩展团体属性过滤器。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MATCHEXTCOMMUNITYFILTER]] · 匹配扩展团体属性过滤器（MATCHEXTCOMMUNITYFILTER）

## 使用实例

查询基于扩展团体属性过滤器的匹配规则：

```
LST MATCHEXTCOMMUNITYFILTER:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
              路由策略名字  =  a
            路由策略节点ID  =  19
扩展团体属性过滤器名字或号  =  aa
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MATCHEXTCOMMUNITYFILTER.md`
