---
id: UNC@20.15.2@MMLCommand@RMV CDRSTAT
type: MMLCommand
name: RMV CDRSTAT（删除话单统计）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CDRSTAT
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单统计
status: active
---

# RMV CDRSTAT（删除话单统计）

## 功能

**适用NF：NCG**

该命令用于删除话单统计任务。

## 注意事项

- 执行删除操作后，会删除话单统计任务生成的结果文件，在执行删除操作之前，需确保结果文件已取走。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRSTATID | 话单统计任务标识 | 可选必选说明：必选参数<br>参数含义：话单统计任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该参数不能包含“\”。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |

## 操作的配置对象

- [话单统计（CDRSTAT）](configobject/UNC/20.15.2/CDRSTAT.md)

## 使用实例

删除话单统计任务，配置举例如下：

```
RMV CDRSTAT: CDRSTATID="cdrstat1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话单统计（RMV-CDRSTAT）_48572281.md`
