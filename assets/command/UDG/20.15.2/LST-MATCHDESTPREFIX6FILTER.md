---
id: UDG@20.15.2@MMLCommand@LST MATCHDESTPREFIX6FILTER
type: MMLCommand
name: LST MATCHDESTPREFIX6FILTER（查询匹配IPv6地址前缀列表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MATCHDESTPREFIX6FILTER
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配IPv6地址前缀列表
status: active
---

# LST MATCHDESTPREFIX6FILTER（查询匹配IPv6地址前缀列表）

## 功能

该命令用于查询基于IPv6信息的前缀过滤器匹配目的地址的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：可选参数<br>参数含义：配置操作的路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MATCHDESTPREFIX6FILTER]] · 匹配IPv6地址前缀列表（MATCHDESTPREFIX6FILTER）

## 使用实例

查询匹配前缀过滤器配置信息：

```
LST MATCHDESTPREFIX6FILTER:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
    路由策略名字  =  a
  路由策略节点号  =  19
IPv6前缀列表名字  =  a
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MATCHDESTPREFIX6FILTER.md`
