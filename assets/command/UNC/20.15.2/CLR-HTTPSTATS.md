---
id: UNC@20.15.2@MMLCommand@CLR HTTPSTATS
type: MMLCommand
name: CLR HTTPSTATS（清除HTTP统计信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: HTTPSTATS
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP统计管理
status: active
---

# CLR HTTPSTATS（清除HTTP统计信息）

## 功能

该命令用于清除缓存中的HTTP统计信息。当不指定模块类型时，该命令执行以后SBILINK、HTTPLINK模块中统计缓存区中记录的统计信息会全部清零。如果指定模块类型为SBILINK或HTTPLINK，则只清空对应模块的统计缓存区中的记录的统计信息。当维护人员发现问题需要通过查询统计进行定界定位时，为方便观察，可以使用此命令清空统计区数据，重新开始计数，更有利于问题定位分析。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MT | 模块类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要清除统计信息的模块。<br>数据来源：本端规划<br>取值范围：<br>- “HTTPLINK（HTTPLINK）”：服务化接口报文转发处理<br>- “SBILINK（SBILINK）”：服务化接口链路管理控制<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HTTPSTATS]] · HTTP统计信息（HTTPSTATS）

## 使用实例

若运营商想要清除HTTP中HTTPLINK模块中统计缓存区中记录的统计信息，可以用如下命令：

```
CLR HTTPSTATS: MT= HTTPLINK;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-HTTPSTATS.md`
