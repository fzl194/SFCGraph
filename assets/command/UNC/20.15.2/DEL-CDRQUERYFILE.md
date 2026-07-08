---
id: UNC@20.15.2@MMLCommand@DEL CDRQUERYFILE
type: MMLCommand
name: DEL CDRQUERYFILE（删除话单查询结果文件）
nf: UNC
version: 20.15.2
verb: DEL
object_keyword: CDRQUERYFILE
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 话单查询
status: active
---

# DEL CDRQUERYFILE（删除话单查询结果文件）

## 功能

**适用NF：NCG**

该命令用于删除话单查询结果文件。

## 注意事项

- 该命令执行后即时生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 查询任务标识 | 可选必选说明：必选参数<br>参数含义：该参数用来表示查询任务标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：<br>- 该参数只能由字母、数字、“-”、“.”组成。 |

## 操作的配置对象

- [话单查询结果文件（CDRQUERYFILE）](configobject/UNC/20.15.2/CDRQUERYFILE.md)

## 使用实例

删除“查询任务标识”为“task”的话单查询结果文件。示例如下：

```
DEL CDRQUERYFILE: TASKID="task";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话单查询结果文件（DEL-CDRQUERYFILE）_81172390.md`
