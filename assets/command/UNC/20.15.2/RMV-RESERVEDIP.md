---
id: UNC@20.15.2@MMLCommand@RMV RESERVEDIP
type: MMLCommand
name: RMV RESERVEDIP（删除预留IP资源）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RESERVEDIP
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
- 预留IP资源
status: active
---

# RMV RESERVEDIP（删除预留IP资源）

## 功能

![](删除预留IP资源（RMV RESERVEDIP）_32789633.assets/notice_3.0-zh-cn_2.png)

- 执行此命令后立即出现IP不通，请谨慎操作。
- 此命令不能动态生效，需要执行“RST VNFC”重启服务。

**适用NF：NCG**

该命令用于删除当前RU上已添加的预留IP资源。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPRID | 预留IP资源标识 | 可选必选说明：必选参数<br>参数含义：用于表示一个预留IP资源对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESERVEDIP]] · 预留IP资源（RESERVEDIP）

## 使用实例

删除标识为IP_66_Reserved_1st的预留IP资源，示例如下：

```
RMV RESERVEDIP: IPRID="IP_66_Reserved_1st";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RESERVEDIP.md`
