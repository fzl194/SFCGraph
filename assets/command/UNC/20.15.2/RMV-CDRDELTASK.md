---
id: UNC@20.15.2@MMLCommand@RMV CDRDELTASK
type: MMLCommand
name: RMV CDRDELTASK（删除话单删除任务）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CDRDELTASK
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
- 话单删除
status: active
---

# RMV CDRDELTASK（删除话单删除任务）

## 功能

![](删除话单删除任务（RMV CDRDELTASK）_51174265.assets/notice_3.0-zh-cn_2.png)

话单删除任务删除后，其配置的目录下如果还有话单文件，将不会再被过期删除。

**适用NF：NCG**

该命令用于删除已添加的话单删除任务。

执行任务之前，可执行 [**LST CDRDELTASK**](查询话单删除任务（LST CDRDELTASK）_51174267.md) 命令查询当前系统中需要删除的话单删除任务情况，找到对应的删除任务标识。

## 注意事项

- 话单删除任务删除后，NCG不再自动删除其配置的目录下的过期话单文件。
- 此命令可以动态生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRDELTASKID | 删除任务标识 | 可选必选说明：必选参数<br>参数含义：话单删除任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CDRDELTASK]] · 话单删除任务（CDRDELTASK）

## 使用实例

删除任务标识为“cdr_deltask1”的话单删除任务：

```
RMV CDRDELTASK: CDRDELTASKID="cdr_deltask1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CDRDELTASK.md`
