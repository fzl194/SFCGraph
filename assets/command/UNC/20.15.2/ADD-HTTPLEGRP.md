---
id: UNC@20.15.2@MMLCommand@ADD HTTPLEGRP
type: MMLCommand
name: ADD HTTPLEGRP（增加HTTP本端实体组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HTTPLEGRP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP本端实体组管理
status: active
---

# ADD HTTPLEGRP（增加HTTP本端实体组）

## 功能

该命令用于添加HTTP本端实体组信息，可将多个HTTP本端实体配置关联到一个组。

## 注意事项

- 该命令执行后立即生效。

- 在一个HTTP本端实体组下最多只能配置32个HTTP本端实体。

- 最多可输入64条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP本端实体组的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~64。<br>默认值：无<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP本端实体组的描述。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPLEGRP]] · HTTP本端实体组（HTTPLEGRP）

## 使用实例

若想添加一组HTTP本端实体组，索引为1，描述信息为nrf：

```
ADD HTTPLEGRP: INDEX=1, DESC="nrf";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加HTTP本端实体组（ADD-HTTPLEGRP）_29213277.md`
