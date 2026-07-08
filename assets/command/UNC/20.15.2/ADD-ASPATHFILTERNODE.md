---
id: UNC@20.15.2@MMLCommand@ADD ASPATHFILTERNODE
type: MMLCommand
name: ADD ASPATHFILTERNODE（增加AS路径过滤节点）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ASPATHFILTERNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- AS路由过滤节点
status: active
---

# ADD ASPATHFILTERNODE（增加AS路径过滤节点）

## 功能

该命令用来增加一个AS路径过滤器表项。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | AS路径过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定AS路径过滤器名字或号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～51。<br>默认值：无<br>配置原则：区分大小写，不支持空格。如果是数字则取值范围为1-256。 |
| NODESEQUENCE | AS路径过滤器节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定AS路径过滤器节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| MATCHMODE | 匹配模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |
| REGULAR | 正则表达式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定正则表达式。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：支持空格，不支持单空格。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ASPATHFILTERNODE]] · AS路径过滤节点（ASPATHFILTERNODE）

## 使用实例

增加AS路径过滤器：

```
ADD ASPATHFILTERNODE: NAME ="a",NODESEQUENCE=1, MATCHMODE=permit, REGULAR="[1-9]";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加AS路径过滤节点（ADD-ASPATHFILTERNODE）_00600769.md`
