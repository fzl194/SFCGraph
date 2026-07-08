---
id: UDG@20.15.2@MMLCommand@RMV SIGNADBRULE
type: MMLCommand
name: RMV SIGNADBRULE（删除特征库规则配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SIGNADBRULE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 延迟生效
is_dangerous: true
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- 更新特征库规则
status: active
---

# RMV SIGNADBRULE（删除特征库规则配置）

## 功能

**适用NF：PGW-U、UPF**

![](删除特征库规则配置（RMV SIGNADBRULE）_25895980.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定特征库规则或所有特征库规则，可能影响业务识别结果，导致计费或控制策略发生变化，请谨慎使用。

该命令用于删除特征库中应用协议、应用子协议的动态识别规则。

## 注意事项

- 为了防止频繁刷新规则对系统造成性能影响，识别规则添加、修改、删除后，不会立即生效，当最后一次执行本命令的90秒后所有规则才生效。
- 该命令与LOD SIGNATUREDB命令建议间隔5分钟，否则可能会导致加载知识库失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SIGNADBRULENAME | 特征库规则协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置特征库规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：设置该参数时表示删除指定名称的动态识别规则，未设置该参数时表示删除系统中所有的动态识别规则。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SIGNADBRULE]] · 特征库规则配置（SIGNADBRULE）

## 使用实例

假如运营商想要删除名称为test_sigrule的动态识别规则：

```
RMV SIGNADBRULE:SIGNADBRULENAME="test_signadbrule";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SIGNADBRULE.md`
