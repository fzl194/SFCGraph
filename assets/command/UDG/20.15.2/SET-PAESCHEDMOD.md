---
id: UDG@20.15.2@MMLCommand@SET PAESCHEDMOD
type: MMLCommand
name: SET PAESCHEDMOD（设置PAE Channel调度模式）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PAESCHEDMOD
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- PAE统计信息
status: active
---

# SET PAESCHEDMOD（设置PAE Channel调度模式）

## 功能

![](设置PAE Channel调度模式（SET PAESCHEDMOD）_61378197.assets/notice_3.0-zh-cn.png)

如果修改该配置可能会造成业务流量损失。

该命令用于设置PAE Channel调度模式。

## 注意事项

该命令为高危命令，如果修改该配置可能会造成业务流量损失。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCHEDMODE | PAE Channel调度模式 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定PAE Channel调度模式。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- absolute-priority：绝对优先级模式，按优先级顺序从队列收包，高优先级队列收到报文后结束收包。<br>- relative-priority：相对优先级模式，按优先级顺序依次从队列收包，直到批收满或队列遍历完为止。<br>默认值：absolute-priority。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAESCHEDMOD]] · PAE Channel调度模式（PAESCHEDMOD）

## 使用实例

设置PAE Channel调度模式为绝对优先级：

```
%%SET PAESCHEDMOD: SCHEDMODE=absolute-priority;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PAESCHEDMOD.md`
