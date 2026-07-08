---
id: UNC@20.15.2@MMLCommand@SET ELECTIONABILITY
type: MMLCommand
name: SET ELECTIONABILITY（设置业务进程选举能力）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ELECTIONABILITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET ELECTIONABILITY（设置业务进程选举能力）

## 功能

该命令已废弃。

该命令用于设置业务进程选举能力的开关。仅当无损升级脚本不可用时，手动执行该命令设置业务进程的选举能力。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MODE |
| --- |
| ENABLE |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODE | 业务进程选举能力使能开关 | 可选必选说明：必选参数<br>参数含义：该参数表示客户端选举能力的使能状态。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（开启）”：业务进程选举能力为可用<br>- “DISABLE（关闭）”：业务进程选举能力为不可用<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ELECTIONABILITY]] · 业务进程选举能力（ELECTIONABILITY）

## 使用实例

- 设置业务进程选举能力为不可用。
  ```
  SET ELECTIONABILITY:MODE=DISABLE;
  ```
- 设置业务进程选举能力为可用。
  ```
  SET ELECTIONABILITY:MODE=ENABLE;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-ELECTIONABILITY.md`
