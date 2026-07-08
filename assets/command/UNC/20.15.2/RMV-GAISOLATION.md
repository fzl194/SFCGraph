---
id: UNC@20.15.2@MMLCommand@RMV GAISOLATION
type: MMLCommand
name: RMV GAISOLATION（删除Ga业务隔离配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GAISOLATION
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
- 业务隔离
status: active
---

# RMV GAISOLATION（删除Ga业务隔离配置）

## 功能

![](删除Ga业务隔离配置（RMV GAISOLATION）_99921349.assets/notice_3.0-zh-cn_2.png)

此命令不能动态生效，需要执行RST RU生效。删除隔离配置会导致隔离AP恢复接收话单，允许链路迁入。

**适用NF：NCG**

该命令用于删除已添加的Ga隔离配置。

## 注意事项

- 命令操作后，需要执行[**RST RU**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/重启资源单元（RST RU）_59103467.md)命令重启生效，恢复Ga口业务，生效后才允许Ga链路迁入。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GAISOLATIONID | Ga隔离标识 | 可选必选说明：必选参数<br>参数含义：话单存储对象标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该参数只能由字母、数字、下划线、中划线组成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GAISOLATION]] · Ga业务隔离配置（GAISOLATION）

## 使用实例

删除Ga隔离标识为“iso1”的Ga隔离配置，示例如下：

```
RMV GAISOLATION:GAISOLATIONID="iso1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Ga业务隔离配置（RMV-GAISOLATION）_99921349.md`
