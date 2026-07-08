---
id: UDG@20.15.2@MMLCommand@LST BATCHPARA
type: MMLCommand
name: LST BATCHPARA（查询批量调度参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: BATCHPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 数据转发控制
- 批量处理控制功能
status: active
---

# LST BATCHPARA（查询批量调度参数）

## 功能

**适用NF：UPF**

该命令用于查询设置的批量调度参数。

## 注意事项

如果没有记录，则当前的批量调度参数为系统初始默认的参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STAGENAME | 数据转发阶段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据转发阶段。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FASTSTAGE：包保序转发阶段。<br>- CPLXSTAGE：流保序转发阶段。<br>- SQTLSTAGE：用户保序转发阶段。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BATCHPARA]] · 批量调度参数（BATCHPARA）

## 使用实例

查询包保序转发阶段的批量调度参数：

```
LST BATCHPARA: STAGENAME=FASTSTAGE;
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-BATCHPARA.md`
