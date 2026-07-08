---
id: UNC@20.15.2@MMLCommand@SET SFEPASSGREFRAG
type: MMLCommand
name: SET SFEPASSGREFRAG（设置SFE透传GRE分片报文使能配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SFEPASSGREFRAG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE透传GRE分片
status: active
---

# SET SFEPASSGREFRAG（设置SFE透传GRE分片报文使能配置）

## 功能

该命令用来设置SFE透传GRE分片报文使能配置。

该功能开启后，重组板不是本板的GRE分片报文，会立刻被SFE发送至目标重组板上，进行GRE分片报文重组。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 该命令适用于非池化和池化场景。（池化：将VNRS、CSLB、网元转发面合并部署，将物理分散的资源整合为逻辑统一池，提升系统资源利用率）

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PASSGREFRAGEN | 透传GRE分片报文使能标记 | 可选必选说明：必选参数<br>参数含义：SFE透传GRE分片报文使能标记。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>初始值：FALSE<br>默认值：无<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SFEPASSGREFRAG]] · SFE透传GRE分片报文使能配置（SFEPASSGREFRAG）

## 使用实例

设置SFE透传GRE分片报文使能配置：

```
SET SFEPASSGREFRAG: PASSGREFRAGEN=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SFEPASSGREFRAG.md`
