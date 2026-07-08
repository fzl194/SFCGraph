---
id: UNC@20.15.2@MMLCommand@ADD EXTENDCOMMUNITYFILTER
type: MMLCommand
name: ADD EXTENDCOMMUNITYFILTER（增加扩展团体属性过滤器）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: EXTENDCOMMUNITYFILTER
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
- 扩展团体属性过滤器
status: active
---

# ADD EXTENDCOMMUNITYFILTER（增加扩展团体属性过滤器）

## 功能

该命令用于添加扩展团体属性过滤器。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 扩展团体属性过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扩展团体属性过滤器名字或扩展团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，扩展团体属性过滤器名称其长度范围是1～51。<br>默认值：无<br>配置原则：扩展团体属性过滤器号为整数形式，其中基本扩展团体属性过滤器号的取值范围为1～199，高级扩展团体属性过滤器号的取值范围为200～399。扩展团体属性过滤器名称为字符串形式，区分大小写，不支持空格，长度范围是1～51，且不能都是数字。 |
| FILTERTYPE | 过滤器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤器类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- basic：基础。<br>- advanced：高级。<br>默认值：无 |

## 操作的配置对象

- [扩展团体属性过滤器（EXTENDCOMMUNITYFILTER）](configobject/UNC/20.15.2/EXTENDCOMMUNITYFILTER.md)

## 使用实例

增加扩展团体属性过滤器：

```
ADD EXTENDCOMMUNITYFILTER:NAME="a",FILTERTYPE=basic;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加扩展团体属性过滤器（ADD-EXTENDCOMMUNITYFILTER）_50121094.md`
