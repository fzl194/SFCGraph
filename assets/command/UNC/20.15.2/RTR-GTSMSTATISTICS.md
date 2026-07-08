---
id: UNC@20.15.2@MMLCommand@RTR GTSMSTATISTICS
type: MMLCommand
name: RTR GTSMSTATISTICS（清除GTSM统计）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: GTSMSTATISTICS
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- GTSM
status: active
---

# RTR GTSMSTATISTICS（清除GTSM统计）

## 功能

该命令用于清除GTSM统计计数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于清除指定资源单元的GTSM统计。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。通过DSP RU命令可以查询资源单元信息。<br>默认值：无<br>配置原则：<br>- 当该参数为空时会清除所有资源单元的GTSM统计。<br>- 可以指定某一资源单元进行清除统计。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTSMSTATISTICS]] · GTSM统计（GTSMSTATISTICS）

## 使用实例

- 清除某一资源单元的统计信息：
  ```
  RTR GTSMSTATISTICS:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
  ```
- 清除所有资源单元的统计信息：
  ```
  RTR GTSMSTATISTICS:;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-GTSMSTATISTICS.md`
