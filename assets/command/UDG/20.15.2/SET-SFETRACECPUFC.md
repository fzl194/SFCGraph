---
id: UDG@20.15.2@MMLCommand@SET SFETRACECPUFC
type: MMLCommand
name: SET SFETRACECPUFC（设置VNRS IP消息跟踪的CPU流控阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SFETRACECPUFC
command_category: 配置类
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

# SET SFETRACECPUFC（设置VNRS IP消息跟踪的CPU流控阈值）

## 功能

![](设置VNRS IP消息跟踪的CPU流控阈值（SET SFETRACECPUFC）_91125205.assets/notice_3.0-zh-cn.png)

如果设置的跟踪流控阈值或恢复阈值不合理，可能会导致跟踪功能不可用或业务呼损。

该命令用来设置VNRS IP消息跟踪的流控和恢复的CPU负载阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 该命令存在系统初始记录（NP卡加速模式场景无需关注此初始记录），参数的初始设置值如下表：
    - 虚机场景
      | SCENE | STARTTHD | RUNTIMETHD | RECOVERYTHD |
      | --- | --- | --- | --- |
      | Pooled_IsolCpus | 50 | 70 | 50 |
      | Unpooled_IsolCpus | 72 | 90 | 65 |
      | Unpooled_SharedCpus | 92 | 97 | 92 |
    - 裸机场景
      | SCENE | STARTTHD | RUNTIMETHD | RECOVERYTHD |
      | --- | --- | --- | --- |
      | Pooled_IsolCpus | 50 | 70 | 50 |
      | Unpooled_IsolCpus | 82 | 90 | 65 |
      | Unpooled_SharedCpus | 99 | 100 | 92 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENE | 场景 | 可选必选说明：必选参数<br>参数含义：该参数用于指定启动态阈值、运行态阈值和恢复阈值的作用场景。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Pooled_IsolCpus：池化核隔离。<br>- Unpooled_IsolCpus：非池化核隔离。<br>- Unpooled_SharedCpus：非池化非核隔离。<br>默认值：无<br>配置原则：无 |
| STARTTHD | 启动态阈值（%） | 可选必选说明：必选参数<br>参数含义：该参数用于指定启动态阈值。当创建VNRS IP消息跟踪任务时，如果转发核CPU占用率大于该阈值，则停止跟踪触发流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~100。<br>默认值：无<br>配置原则：<br>**启动态阈值（%）**<br>必须小于<br>**运行态阈值（%），**<br>且必须大于等于<br>**恢复阈值（%）**<br>。 |
| RUNTIMETHD | 运行态阈值（%） | 可选必选说明：必选参数<br>参数含义：该参数用于指定运行态阈值。正在执行<br>VNRS IP<br>消息跟踪任务期间，<br>如果转发核CPU占用率大于该阈值，则停止跟踪触发流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~100。<br>默认值：无<br>配置原则：<br>**运行态阈值**<br>**（%）**<br>必须分别大于<br>**启动态阈值**<br>**（%）**<br>和<br>**恢复阈值（%）**<br>。 |
| RECOVERYTHD | 恢复阈值（%） | 可选必选说明：必选参数<br>参数含义：该参数用于指定恢复阈值。在触发流控停止跟踪后，如果<br>转发核CPU占用率小于该阈值，则恢复跟踪。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~100。<br>默认值：无<br>配置原则：<br>**恢复阈值（%）**<br>必须小于<br>**运行态**<br>**阈值**<br>**（%），**<br>且必须小于等于<br>**启动态阈值（%）**<br>。 |

## 操作的配置对象

- [VNRS IP消息跟踪的CPU流控阈值（SFETRACECPUFC）](configobject/UDG/20.15.2/SFETRACECPUFC.md)

## 使用实例

```
设置池化核隔离场景下VNRS IP消息跟踪的启动态阈值为60%，运行态阈值为80%，恢复阈值为60%：
SET SFETRACECPUFC: SCENE=Pooled_IsolCpus, STARTTHD=60, RUNTIMETHD=80, RECOVERYTHD=60; 
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置VNRS-IP消息跟踪的CPU流控阈值（SET-SFETRACECPUFC）_91125205.md`
