---
id: UDG@20.15.2@MMLCommand@LST SFETRACECPUFC
type: MMLCommand
name: LST SFETRACECPUFC（查询VNRS IP消息跟踪的CPU流控阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFETRACECPUFC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 跟踪管理
status: active
---

# LST SFETRACECPUFC（查询VNRS IP消息跟踪的CPU流控阈值）

## 功能

该命令用来查询VNRS IP消息跟踪的流控和恢复的CPU负载阈值参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENE | 场景 | 可选必选说明：必选参数<br>参数含义：该参数用于指定启动态阈值、运行态阈值和恢复阈值的作用场景。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Pooled_IsolCpus：池化核隔离。<br>- Unpooled_IsolCpus：非池化核隔离。<br>- Unpooled_SharedCpus：非池化非核隔离。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [VNRS IP消息跟踪的CPU流控阈值（SFETRACECPUFC）](configobject/UDG/20.15.2/SFETRACECPUFC.md)

## 使用实例

查询池化核隔离场景下VNRS IP消息跟踪的流控和恢复的CPU负载阈值参数：

```
LST SFETRACECPUFC: SCENE=Pooled_IsolCpus:;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
启动态阈值（%）  =  60
运行态阈值（%）  =  80
  恢复阈值（%）  =  60
(结果个数 = 1) 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询VNRS-IP消息跟踪的CPU流控阈值（LST-SFETRACECPUFC）_91245389.md`
