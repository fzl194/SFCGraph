---
id: UNC@20.15.2@MMLCommand@MOD SBIAPLE
type: MMLCommand
name: MOD SBIAPLE（修改服务化接口本端实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SBIAPLE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口本端实体管理
status: active
---

# MOD SBIAPLE（修改服务化接口本端实体）

## 功能

该命令用于修改服务化接口本端实体的描述信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务化接口本端实体的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于配置服务化接口本端实体的描述信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBIAPLE]] · 服务化接口本端实体（SBIAPLE）

## 使用实例

若运营商想修改索引为1的服务化接口本端实体的描述信息为"smf"，可以执行如下命令：

```
MOD SBIAPLE: INDEX=1, DESCRIPTION="smf";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改服务化接口本端实体（MOD-SBIAPLE）_83813638.md`
