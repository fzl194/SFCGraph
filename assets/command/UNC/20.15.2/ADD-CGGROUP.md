---
id: UNC@20.15.2@MMLCommand@ADD CGGROUP
type: MMLCommand
name: ADD CGGROUP（添加CG组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CGGROUP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- CG组
status: active
---

# ADD CGGROUP（添加CG组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来增加CG组，配置CG组描述信息。此命令为离线计费的基本配置，CG组用来绑定CG。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为32。
- 如果要使用该CG组则必须绑定到离线计费模板下或设置为全局CG组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CGGRPID | CG组ID | 可选必选说明：必选参数<br>参数含义：CG组的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：无 |
| DESCRIPTION | CG组描述 | 可选必选说明：可选参数<br>参数含义：CG组的描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CGGROUP]] · CG组（CGGROUP）

## 关联任务

- [[UNC@20.15.2@Task@0-00012]]

## 使用实例

增加一条CG组配置，其中CG组ID为1，CG组描述为“CGGroup1”：

```
ADD CGGROUP: CGGRPID=1, DESCRIPTION="CGGroup1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/添加CG组（ADD-CGGROUP）_09896879.md`
