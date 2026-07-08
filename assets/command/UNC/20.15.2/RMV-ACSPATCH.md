---
id: UNC@20.15.2@MMLCommand@RMV ACSPATCH
type: MMLCommand
name: RMV ACSPATCH（删除补丁）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ACSPATCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# RMV ACSPATCH（删除补丁）

## 功能

![](删除补丁（RMV ACSPATCH）_05338959.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会影响系统的正常运行，请谨慎使用并联系华为支持协助操作。

该命令用于当系统中补丁存在问题时，删除系统补丁。

本命令只适用于ACS服务，其他微服务请使用RMV PATCH命令。

## 注意事项

- 该命令执行后立即生效。
- 该命令会删除系统补丁，无补丁、已加载补丁，已激活补丁，执行该操作的结果都是成功。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ACSPATCH]] · 补丁（ACSPATCH）

## 使用实例

删除系统补丁：

```
RMV ACSPATCH:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ACSPATCH.md`
