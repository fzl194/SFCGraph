---
id: UNC@20.15.2@MMLCommand@RMV NGACCCHRPRCTMPL
type: MMLCommand
name: RMV NGACCCHRPRCTMPL（删除NG接入CHR流程控制模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGACCCHRPRCTMPL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- CHR管理
- NG接入CHR流程控制模板
status: active
---

# RMV NGACCCHRPRCTMPL（删除NG接入CHR流程控制模板）

## 功能

**适用NF：AMF**

该命令用于删除NG接入CHR流程控制模板，用以控制CHR的采集流程。

## 注意事项

- 该命令执行后立即生效。

- 系统初始运行，会默认创建索引为0和1的NGACCCHRPRCTMPL配置，分别用于高性能CHR服务器和低性能CHR服务器的采集流控控制。这两条默认配置无法被删除，只能修改。
- 如果NGACCCHRPRCTMPL被NGSRCHRCFG引用，则不允许删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMPLIDX | 流程控制模板索引 | 可选必选说明：必选参数<br>参数含义：流程控制模板索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>该参数值非0和1，需要使用SET NGACCCHRCFG命令设置NG接入CHR上报策略。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGACCCHRPRCTMPL]] · NG接入CHR流程控制模板（NGACCCHRPRCTMPL）

## 使用实例

删除索引为10的NG接入CHR流程控制模板：

```
RMV NGACCCHRPRCTMPL:TMPLIDX=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NG接入CHR流程控制模板（RMV-NGACCCHRPRCTMPL）_34945606.md`
