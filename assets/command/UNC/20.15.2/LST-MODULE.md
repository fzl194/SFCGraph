---
id: UNC@20.15.2@MMLCommand@LST MODULE
type: MMLCommand
name: LST MODULE（查询业务模块）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MODULE
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 业务模块
status: active
---

# LST MODULE（查询业务模块）

## 功能

**适用NF：NCG**

该命令用于查询NCG RU上的业务模块信息。

常见的查询方式有：

不输入参数，查询RU上添加的所有模块信息。

输入“模块名”参数，查询指定业务模块信息。

输入“接入网元分组标识”参数，查询与指定网元分组标识关联的所有业务模块信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MNAME | 模块名 | 可选必选说明：可选参数<br>参数含义：用于表示一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：无 |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| RUROLE | RU角色 | 可选必选说明：可选参数<br>参数含义：用于指定当前RU角色。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CONVERGE：汇聚RU。<br>- SERVICE：业务RU。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MODULE]] · 业务模块（MODULE）

## 使用实例

查询RU上添加的业务模块，示例如下：

```
LST MODULE:;
```

```
RETCODE = 0  操作成功。

结果如下:
--------
          模块名  =  AP66_1
接入网元分组标识  =  PS_GROUP_1
          RU角色  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MODULE.md`
