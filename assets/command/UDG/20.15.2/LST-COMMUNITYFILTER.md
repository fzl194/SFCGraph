---
id: UDG@20.15.2@MMLCommand@LST COMMUNITYFILTER
type: MMLCommand
name: LST COMMUNITYFILTER（查询团体属性过滤器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: COMMUNITYFILTER
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 团体属性过滤器
status: active
---

# LST COMMUNITYFILTER（查询团体属性过滤器）

## 功能

该命令用来查询团体属性过滤器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMNTYNAMEORNUM | 团体属性过滤器名字或号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性过滤器名字或团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无<br>配置原则：团体属性过滤器号为整数形式，其中基本团体属性过滤器号的取值范围为1～99，高级团体属性过滤器号的取值范围为100～199。团体属性过滤器名称为字符串形式，区分大小写，长度范围是1～51，且不能都是数字。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@COMMUNITYFILTER]] · 团体属性过滤器（COMMUNITYFILTER）

## 使用实例

查询团体属性过滤器：

```
LST COMMUNITYFILTER:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
团体属性过滤器类型    团体属性过滤器名字或号
高级                  100
基础                  a
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-COMMUNITYFILTER.md`
