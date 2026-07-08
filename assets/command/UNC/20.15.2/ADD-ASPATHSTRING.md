---
id: UNC@20.15.2@MMLCommand@ADD ASPATHSTRING
type: MMLCommand
name: ADD ASPATHSTRING（增加替换AS路径值）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ASPATHSTRING
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
- 替换AS路径值
status: active
---

# ADD ASPATHSTRING（增加替换AS路径值）

## 功能

该命令用来增加AS路径属性的操作值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，需要通过ADD APPLYASPATH配置应用as-path属性。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| SEQUENCENUMBER | AS属性值序列号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定AS属性值序列号。序列号只能是1~63之间的数字。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～63。<br>默认值：无 |
| STRINGVALUE | AS路径值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定AS属性值。支持两种格式的AS值： 1.整数形式，取值范围是1~4294967295。 2.点分式，形式为number<1-65535>.number<0-65535>。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～11。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ASPATHSTRING]] · 替换AS路径值（ASPATHSTRING）

## 使用实例

增加AS路径属性的操作值：

```
ADD ASPATHSTRING:POLICYNAME="a",NODESEQUENCE=10,SEQUENCENUMBER=7,STRINGVALUE="20";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-ASPATHSTRING.md`
