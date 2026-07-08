---
id: UNC@20.15.2@MMLCommand@ADD RDSTRING
type: MMLCommand
name: ADD RDSTRING（增加RD字符）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RDSTRING
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- RD字符
status: active
---

# ADD RDSTRING（增加RD字符）

## 功能

该命令用来增加RD属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1024。
- 配置该命令前，必须已经通过ADD RDFILTERNODE配置了RD过滤器。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | RD过滤器索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RD过滤器索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1024。<br>默认值：无 |
| NODESEQUENCE | RD过滤器节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RD过滤器节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| STRINGVALUE | 字符值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RD属性值，支持如下4种格式： 1. IPv4地址:nn，如10.1.1.1:200。 2. aa:nn，如100:1。 3. IPv4地址:*，通配格式。如10.1.1.1:*表示匹配所有以10.1.1.1开头的RD。 4. aa:*，通配格式。如100:*表示匹配所有以100开头的RD。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～21。<br>默认值：无<br>配置原则：IP<X.X.X.X>:NN<0-65535>或者IP< X.X.X.X>:*或者AS<0-65535>:NN<0-4294967295>或者AS<65536-4294967295>:NN<0-65535>或者AS<0-4294967295>:*或者AS<0-65535>.<0-65535>:NN<0-65535>或者AS<0-65535>.<0-65535>:*。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSTRING]] · RD字符（RDSTRING）

## 使用实例

添加RD属性：

```
ADD RDSTRING:INDEX=55,NODESEQUENCE=10,STRINGVALUE="1:1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-RDSTRING.md`
