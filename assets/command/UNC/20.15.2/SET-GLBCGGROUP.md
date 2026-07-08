---
id: UNC@20.15.2@MMLCommand@SET GLBCGGROUP
type: MMLCommand
name: SET GLBCGGROUP（设置全局CG组）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GLBCGGROUP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- 全局CG组
status: active
---

# SET GLBCGGROUP（设置全局CG组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于设置全局CG组，UNC优先选择离线计费模板下绑定的CG组，当离线计费模板下没有绑定CG组或根据号段未匹配到CG组时，UNC选择全局配置的CG组。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 系统支持配置1条全局组记录。
- CG Group ID输入0表示删除全局CG Group。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CGGRPID |
| --- | --- |
| 初始值 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CGGRPID | CG组ID | 可选必选说明：必选参数<br>参数含义：指定全局CG组ID。CG组可以通过ADD CGGROUP命令配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32，其中0表示不指定全局CG组。<br>默认值：无<br>配置原则：该参数使用ADD CGGROUP命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBCGGROUP]] · 全局CG组（GLBCGGROUP）

## 使用实例

设置CG组ID为1的CG组为全局CG组，命令为：

```
SET GLBCGGROUP: CGGRPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-GLBCGGROUP.md`
