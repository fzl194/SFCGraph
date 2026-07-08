---
id: UNC@20.15.2@MMLCommand@LST MATCHTAG
type: MMLCommand
name: LST MATCHTAG（查询Tag匹配路由策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MATCHTAG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配路由标签
status: active
---

# LST MATCHTAG（查询Tag匹配路由策略）

## 功能

该命令用于查询匹配路由标签值的配置结果。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MATCHTAG]] · Tag匹配路由策略（MATCHTAG）

## 使用实例

查询匹配路由标签值配置信息：

```
LST MATCHTAG:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  路由策略名字  =  a
路由策略节点号  =  19
         Tag值  =  4
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MATCHTAG.md`
