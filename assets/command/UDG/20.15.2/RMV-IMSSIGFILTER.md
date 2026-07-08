---
id: UDG@20.15.2@MMLCommand@RMV IMSSIGFILTER
type: MMLCommand
name: RMV IMSSIGFILTER（删除IMS分类器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IMSSIGFILTER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- VOLTE管理
- IMS信令分类器
status: active
---

# RMV IMSSIGFILTER（删除IMS分类器）

## 功能

**适用NF：PGW-U、UPF**

![](删除IMS分类器（RMV IMSSIGFILTER）_86526216.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认删除规则后合法的IMS信令报文都能命中其中一条规则。

该命令用于删除系统设备IMS分配器配置信息。在网络中规划IMS业务，对话的IMS分类器信息变化或者不需要时，需要使用该命令根据优先级删除指定类型的分配器信息。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令时，请确认是否会对IMS业务造成影响，操作不当，可能会造成语音业务不通。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于设置静态分组过滤优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IMS分类器（IMSSIGFILTER）](configobject/UDG/20.15.2/IMSSIGFILTER.md)

## 使用实例

当运营商规划IMS网络，配置IMS分配器信息，在不需要接入IMS网络，使用该命令删除指定优先级的IMS分类器的配置信息，举例：“PRIORITY”为“2”：

```
RMV IMSSIGFILTER:PRIORITY=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除IMS分类器（RMV-IMSSIGFILTER）_86526216.md`
