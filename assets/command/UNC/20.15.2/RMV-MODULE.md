---
id: UNC@20.15.2@MMLCommand@RMV MODULE
type: MMLCommand
name: RMV MODULE（删除业务模块）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MODULE
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
- 业务模块
status: active
---

# RMV MODULE（删除业务模块）

## 功能

![](删除业务模块（RMV MODULE）_51174291.assets/notice_3.0-zh-cn_2.png)

此命令不能动态生效，需要执行“RST VNFC”重启服务，并且删除业务模块会导致该业务模块功能不可用。

在BI收敛开关开启的情况下，如果执行完"RMV MDOULE"命令之后需要执行"ADD MDOULE"命令，必须在执行完最后一个"RMV MDOULE"命令之后执行“RST VNFC”重启服务，待服务恢复之后再执行"ADD MDOULE"命令添加模块。

**适用NF：NCG**

该命令用于删除已添加的业务模块。当实际应用中需要减少业务模块时执行此命令。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 删除业务模块属于危险操作，可能导致该业务模块所属的业务不可用，从而影响NCG系统整体的话单处理能力。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MNAME | 模块名 | 可选必选说明：必选参数<br>参数含义：用于表示一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MODULE]] · 业务模块（MODULE）

## 使用实例

删除已存在业务模块“AP66_1”示例：

```
RMV MODULE: MNAME="AP66_1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MODULE.md`
