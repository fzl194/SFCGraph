---
id: UDG@20.15.2@MMLCommand@ADD BASICCOMMUNITYNODE
type: MMLCommand
name: ADD BASICCOMMUNITYNODE（增加基础团体属性过滤器节点）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: BASICCOMMUNITYNODE
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
- 基础团体属性过滤器节点
status: active
---

# ADD BASICCOMMUNITYNODE（增加基础团体属性过滤器节点）

## 功能

该命令用来增加基本团体属性过滤器节点。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD COMMUNITYFILTER配置了基本团体过滤器。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODESEQUENCE | 团体属性过滤器节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性过滤器节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| CMNTYNAMEORNUM | 团体属性过滤器名字或号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性过滤器名字或团体属性过滤器号。<br>数据来源：本端规划<br>取值范围：字符串类型，团体属性过滤器名称其长度范围是1～51。<br>默认值：无<br>配置原则：基本团体属性过滤器号为整数形式，取值范围为1～99。基本团体属性过滤器名称为字符串形式，区分大小写，不支持空格，长度范围是1～51，且不能都是数字。 |
| MATCHMODE | 匹配模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |
| STRINGVALUE1 | 字符串1 | 可选必选说明：必选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE2 | 字符串2 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE3 | 字符串3 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE4 | 字符串4 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE5 | 字符串5 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE6 | 字符串6 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE7 | 字符串7 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE8 | 字符串8 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE9 | 字符串9 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE10 | 字符串10 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE11 | 字符串11 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE12 | 字符串12 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE13 | 字符串13 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE14 | 字符串14 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE15 | 字符串15 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE16 | 字符串16 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE17 | 字符串17 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE18 | 字符串18 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE19 | 字符串19 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |
| STRINGVALUE20 | 字符串20 | 可选必选说明：可选参数<br>参数含义：该参数用于指定团体属性值。支持三种格式：（1）数字形式，取值范围0～4294967295。（2）aa:nn形式，aa和nn的取值范围都是0～65535。（3）知名团体属性，internet，no-export-subconfed，no-advertise，no-export。<br>数据来源：本端规划<br>取值范围：字符串类型，长度范围是1～20。数字形式，取值范围0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BASICCOMMUNITYNODE]] · 基础团体属性过滤器节点（BASICCOMMUNITYNODE）

## 使用实例

增加基本团体属性过滤器节点：

```
ADD BASICCOMMUNITYNODE:NODESEQUENCE=10,CMNTYNAMEORNUM="a",MATCHMODE=permit,STRINGVALUE1="1:1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-BASICCOMMUNITYNODE.md`
