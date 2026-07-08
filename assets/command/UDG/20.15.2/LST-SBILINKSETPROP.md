---
id: UDG@20.15.2@MMLCommand@LST SBILINKSETPROP
type: MMLCommand
name: LST SBILINKSETPROP（查询SBI链路集策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SBILINKSETPROP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路集策略管理
status: active
---

# LST SBILINKSETPROP（查询SBI链路集策略）

## 功能

该命令用于查询服务化接口链路配置属性信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SBI链路集策略的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SBI链路集策略（SBILINKSETPROP）](configobject/UDG/20.15.2/SBILINKSETPROP.md)

## 使用实例

若运营商想查询配置的所有SBI链路集策略，可以执行如下命令：

```
LST SBILINKSETPROP:;

%%LST SBILINKSETPROP:;%%
RETCODE = 0  操作成功

结果如下
------------------------
索引  =  1  
链路数量  =  2
策略  =  Turns
StreamId数量数组  =  [10000 10000]
权重数组  =  NULL
优先级数组  =  NULL
描述  =  NULL
NF IP是否与NFService端口号组合 = FALSE
进程内链路集故障阈值 = 0
系统内链路集故障阈值 = 0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SBI链路集策略（LST-SBILINKSETPROP）_28971843.md`
