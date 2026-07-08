---
id: UDG@20.15.2@MMLCommand@LST ASPATHFILTERNODE
type: MMLCommand
name: LST ASPATHFILTERNODE（查询AS路径过滤节点）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ASPATHFILTERNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- AS路由过滤节点
status: active
---

# LST ASPATHFILTERNODE（查询AS路径过滤节点）

## 功能

该命令用来查询一个AS路径过滤器表项。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | AS路径过滤器名字或号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定AS路径过滤器名字或号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～51。<br>默认值：无 |

## 操作的配置对象

- [AS路径过滤节点（ASPATHFILTERNODE）](configobject/UDG/20.15.2/ASPATHFILTERNODE.md)

## 使用实例

查询AS路径过滤器：

```
LST ASPATHFILTERNODE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
AS路径过滤器名字或号  =  a
  AS路径过滤器节点号  =  10
            匹配模式  =  允许
          正则表达式  =  [1-9]
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询AS路径过滤节点（LST-ASPATHFILTERNODE）_00840729.md`
