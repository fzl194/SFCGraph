---
id: UDG@20.15.2@MMLCommand@LST RDSTRING
type: MMLCommand
name: LST RDSTRING（查询RD字符）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RDSTRING
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- RD字符
status: active
---

# LST RDSTRING（查询RD字符）

## 功能

该命令用来查询RD属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | RD过滤器索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RD过滤器索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1024。<br>默认值：无 |
| NODESEQUENCE | RD过滤器节点号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RD过滤器节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| STRINGVALUE | 字符值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RD属性值，支持如下4种格式： 1. IPv4地址:nn，如10.1.1.1:200。 2. aa:nn，如100:1。 3. IPv4地址:*，通配格式。如10.1.1.1:*表示匹配所有以10.1.1.1开头的RD。 4. aa:*，通配格式。如100:*表示匹配所有以100开头的RD。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～21。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RDSTRING]] · RD字符（RDSTRING）

## 使用实例

查询RD属性：

```
LST RDSTRING:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  RD过滤器索引  =  55
RD过滤器节点号  =  10
        字符值  =  1:1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询RD字符（LST-RDSTRING）_50121066.md`
